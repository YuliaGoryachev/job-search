from fastapi import APIRouter, HTTPException
from app.utils.langchain_retrievers import prepare_data, get_cohere_retriever
from app.utils.openai_parsings import cover_letter
from pydantic import BaseModel
import docx2txt

router = APIRouter()


def read_docx_file(path) -> str:
    """loads a docx file and returns the text"""
    text = docx2txt.process(path)
    return text


def read_text_file(file_path: str) -> str:
    """reads a text file and returns the text"""
    with open(file_path, "r") as file:
        return file.read()


@router.post(
    "/rag_question",
    response_model='',
    name="rag:internal",
)
async def extract_info(path_to_data: str, query: str):
    """return the most relevant jobs for the query,
    expects as input the path to the csv data and the query
    """
    if not query or not path_to_data:
        raise HTTPException(status_code=404, detail="invalid input")
    try:
        # retrieve relevant information from my database
        data = prepare_data(path_to_data)
        compress_retriever = get_cohere_retriever(data)
        return compress_retriever.get_relevant_documents(query)
    except Exception as e:
        print(e)


@router.post(
    "/cover_letter",
    response_model='',
    name="rag:internal",
)
def get_cover_letter(path_to_jd: str, path_to_cv: str) -> str:
    """creates a cover letter from the job description and the cv text
    data_input: JD_path, CV_path - path to the job description file (text file) and the path to the cv
    (cv has to be in docx format) - there is a sample JD file in the `data` folder
    """
    if not path_to_jd or not path_to_cv:
        raise HTTPException(status_code=404, detail="invalid input")
    try:
        # retrieve relevant information from my database
        jd_text = read_text_file(path_to_jd)
        cv_text = read_docx_file(path_to_cv)
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
