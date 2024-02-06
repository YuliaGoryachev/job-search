from dataclasses import dataclass
import unidecode
import re
from nltk.corpus.reader.wordlist import WordListCorpusReader
from nltk.tokenize import RegexpTokenizer


@dataclass
class Cleaner:
    stopwords: WordListCorpusReader
    tokenizer: RegexpTokenizer
    lang: str = 'english'
    stop: bool = True

    def clean(self, text: str) -> str:
        """Cleans a string by removing punctuation and converting to lowercase"""
        text = re.sub(r"[_\-/]", ' ', text.lower())
        text = unidecode.unidecode(text)
        text = self.remove_newlines(self.remove_numbers(text))
        if self.stop:
            text = self.remove_stop(text)
        return text

    def remove_stop(self, text: str) -> str:
        """Removes stopwords from a string"""
        stops = set(self.stopwords.words(self.lang))
        tokenized_words = self.tokenizer.tokenize(text)
        return ' '.join([word for word in tokenized_words if word not in stops])

    @staticmethod
    def remove_newlines(text: str) -> str:
        """removes newlines from a string"""
        return re.sub(r"\n+", "\n", text)

    @staticmethod
    def remove_numbers(text: str) -> str:
        """removes numbers from a string"""
        return re.sub(r"\d+", "", text)
