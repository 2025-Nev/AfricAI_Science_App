from fastapi import FastAPI
import uvicorn
from api.models import questions
from api.models import quiz

app = FastAPI()


@app.get("/")
def index() -> str:
    return "AfricAI Quiz!"


@app.get("/get_question")
def get_question() -> dict:
    questions = get_questions()
    current_question = questions[0]
    return {"question_text": current_question.question_text, "answer_choices": current_question.answer_choices}


@app.post("/answer_question")
def answer_question(answer: str) -> bool:
    questions = get_questions()
    current_question = questions[0]
    return quiz.answer_question(answer)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
