from chat_bot_RAG.rag_api.app.app.utils.openai_parsings import get_salary_and_responsibilities, \
    cover_letter


def test_get_salary_and_responsibilities():
    jd_text = "We are looking for a software engineer to join our team. The ideal candidate will " \
              "have experience with " \
              "Python, Java, and C++. The candidate should have a strong understanding of data structures and " \
              "algorithms."
    response = get_salary_and_responsibilities(jd_text)  # type: ignore
    assert response == {"salary": "no salary mentioned", "responsibilities":
        ["We are looking for a software engineer to join our team.",
         "The ideal candidate will have experience with Python, Java, and C++.",
         "The candidate should have a strong understanding of data structures and algorithms."]}
    assert response["salary"] == "no salary mentioned"


def test_cover_letter():
    jd_text = "We are looking for a software engineer to join our team. " \
              "The ideal candidate will have experience with " \
              "Python, Java, and C++. The candidate should have a strong understanding of data structures and " \
              "algorithms."
    cv_text = "I am a software engineer with experience in Python, Java, and C++. I have a strong understanding of " \
              "data structures and algorithms."
    response = cover_letter(jd_text, cv_text)  # type: ignore
    assert response == "Hello, I would like to submit my application for the position of software engineer, " \
                       "I am a software engineer with experience in Python, Java, and C++. I have a strong " \
                       "understanding of data structures and algorithms."
    assert response == "Hello, I would like to submit my application for the position of software engineer, " \
                       "I am a software engineer with experience in Python, Java, and C++. I have a strong " \
                       "understanding of data structures and algorithms."
