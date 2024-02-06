from fastapi import APIRouter, HTTPException
from typing import List, Dict
from app.utils.data_loader import Loader
from app.utils.openai_parsings import cover_letter
from pydantic import BaseModel

router = APIRouter()


## Change this portion for other types of models
## Add the correct type hinting when completed
# def get_prediction(data_point):
#     return model.predict(data_point, load_wrapper=joblib.load, method="predict")


def read_text_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


@router.post(
    "/rag_main",
    response_model='',
    name="rag:internal",
)
async def extract_info(data_input: List):
    if not data_input:
        raise HTTPException(status_code=404, detail="invalid input")
    try:
        # retrieve relevant information from my database
        path = '/Users/yuliagoryachev/learning/langchain_course/llms/data'
        loader = Loader(path)
        load_data = loader.load_csv()
        return load_data.shape
    except Exception as e:
        print(e)


@router.post(
    "/cover_letter",
    response_model='',
    name="rag:internal",
)
def get_cover_letter(data_input: List[str]) -> str:
    """creates a cover letter from the job description and the cv text
    data_input: List[JD_path, CV_path] - the job description and the path to the cv (in docx format)
    [JD_path: str, cv_path: str]
    """
    if not data_input:
        raise HTTPException(status_code=404, detail="invalid input")
    try:
        # retrieve relevant information from my database
        loader = Loader(data_input[1])
        cv_text = loader.load_docx().text.values[0]
        jd_text = read_text_file(data_input[0])
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
