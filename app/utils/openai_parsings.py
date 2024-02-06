import openai
from dotenv import dotenv_values
from openai import OpenAI

path_to_keys = '/Users/yuliagoryachev/learning/langchain_course/llms/keys.env'
temp = dotenv_values(path_to_keys)
openai.api_key = temp["OPENAI_API_KEY"]
client = OpenAI(api_key=openai.api_key)


def get_salary_and_skills(jd_text: str) -> str:
    """get the salary and skills from the job description"""
    prompt_text = """
    Parse the following job description and return a json object with properties:
    { "salary": should include range, values and currency, if no salary mentioned say 'no salary mentioned'
      "skills":  should be formatted as list and include the technical skills expected from the candidate }
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a job description parser, provided with the text {jd_text}"},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0
    )
    return completion.choices[0].message.content


def cover_letter(jd_text: str, cv_text: str) -> str:
    """generate a cover letter from the job description and the cv text"""
    system_prompt = f"You are a job description parser and cover letter formulator, " \
                    f"provided with the text {jd_text} and the CV text {cv_text}"
    prompt_text = """
    Write a cover letter that combines the CV skills and experiences in the most relevant 
    way to the job description. The Cover letter should be no more than 300 words. 
    It should start with: Hello, I would like to submit my application for the position of [job title], 
    and not Dear hiring manger.
    """
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0
    )
    return completion.choices[0].message.content
