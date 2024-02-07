from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import CohereEmbeddings
from langchain.retrievers.document_compressors import CohereRerank
from langchain.retrievers import ContextualCompressionRetriever
import cohere
from cohere import Client
from langchain.retrievers import BM25Retriever
from langchain.schema import Document
from app.utils.data_loader import Loader
from dotenv import load_dotenv, find_dotenv, dotenv_values

path_to_keys = '/Users/yuliagoryachev/learning/langchain_course/llms/keys.env'
temp = dotenv_values(path_to_keys)
cohere_api_key = temp["COHERE_API_KEY"]


def prepare_data(data_path) -> list[Document]:
    # Load the data
    # data_path = '/Users/yuliagoryachev/learning/langchain_course/llms/data/'
    loader = Loader(data_path)
    csv_data = loader.load_csv()
    docs = [Document(page_content=desc, metadata={'url': url}) for desc, url in
            zip(csv_data.Description, csv_data['Detail URL'])]
    return docs


def get_bm25_retriever(docs: list[Document]) -> BM25Retriever:
    # Create a BM25 retriever
    retriever = BM25Retriever(docs, k=100)
    return retriever


def get_cohere_retriever(docs: list[Document]) -> ContextualCompressionRetriever:
    class CustomCohereRerank(CohereRerank):
        class Config(CohereRerank.Config):
            arbitrary_types_allowed = True

    CustomCohereRerank.update_forward_refs()
    compressor = CustomCohereRerank(cohere_api_key=cohere_api_key, client=Client, top_n=100)
    retriever = get_bm25_retriever(docs)
    # Create a Cohere retriever
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )
    return compression_retriever
