from app.utils.cleaners import Cleaner
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


def test_cleaner():
    cleaner = Cleaner(stopwords, RegexpTokenizer(r'\w+'), 'english', True)

    results = cleaner.clean("a - b / c _ d , a-b/c_d")
    expected = 'b c b c'
    assert results == expected

    results = cleaner.clean("not a stopwordsless test")
    expected = "stopwordsless test"
    assert results == expected

    results = cleaner.clean("I am number 1 self-taught and have made applications \n\n with Java/Python.")
    expected = "number self taught made applications java python"
    assert results == expected
