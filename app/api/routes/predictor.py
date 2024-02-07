from fastapi import APIRouter, HTTPException
from typing import List
from app.utils.langchain_retrievers import prepare_data, get_bm25_retriever, get_cohere_retriever
from app.utils.openai_parsings import cover_letter
from pydantic import BaseModel
import docx2txt

router = APIRouter()


## Change this portion for other types of models
## Add the correct type hinting when completed
# def get_prediction(data_point):
#     return model.predict(data_point, load_wrapper=joblib.load, method="predict")

def read_docx_file(path) -> str:
    """loads a docx file and returns the text"""
    text = docx2txt.process(path)
    return text


def read_text_file(file_path: str) -> str:
    """reads a text file and returns the text"""
    with open(file_path, "r") as file:
        return file.read()


@router.post(
    "/rag_main",
    response_model='',
    name="rag:internal",
)
async def extract_info(path_to_data: str, query: str):
    """return the relevant job descriptions for the query,
    expects as input the path to the csv data and the query
    """
    if not query:
        raise HTTPException(status_code=404, detail="invalid input")
    try:
        # retrieve relevant information from my database
        data = prepare_data(path_to_data)
        compress_retriever = get_cohere_retriever(data)
        return compress_retriever.get_relevant_documents(query, None)
    except Exception as e:
        print(e)


@router.post(
    "/cover_letter",
    response_model='',
    name="rag:internal",
)
def get_cover_letter(data_input: List[str]) -> str:
    """creates a cover letter from the job description and the cv text
    data_input: List[JD_path, CV_path] - path to the job description file and the path to the cv (cv has to be in docx format)
    """
    if not data_input:
        raise HTTPException(status_code=404, detail="invalid input")
    try:
        # retrieve relevant information from my database
        jd_text = read_text_file(data_input[0])
        cv_text = read_docx_file(data_input[1])
        return cover_letter(jd_text, cv_text)
    except Exception as e:
        print(e)


class HealthResponse(BaseModel):
    status: str


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
async def health():
    return HealthResponse(status="ok")
