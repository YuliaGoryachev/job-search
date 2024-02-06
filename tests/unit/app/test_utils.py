from app.utils.openai_parsings import get_salary_and_skills, cover_letter
import json


def test_get_salary_and_skills():
    # Ideally I should mock the OpenAI API, to avoid the costly call, and make it fully isolated
    jd_text = "We are looking for a software engineer to join our team. The ideal candidate will " \
              "have experience with " \
              "Python, Java, and C++. The candidate should have a strong understanding of data structures and " \
              "algorithms."
    response = json.loads(get_salary_and_skills(jd_text))
    assert response == {"salary": "no salary mentioned",
                        "skills": ["Python", "Java", "C++", "data structures", "algorithms"]}
    assert response["salary"] == "no salary mentioned"

