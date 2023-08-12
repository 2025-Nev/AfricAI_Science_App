import random
import json
from fastapi import FastAPI

app = FastAPI()

def load_questions():
  """Loads the questions from the questions.json file."""
  with open("questions.json", "r") as f:
    questions = json.load(f)
  return questions

@app.get("/")
def get_questions():
  """Gets the list of questions."""
  questions = load_questions()
  return {"questions": questions}

@app.post("/answer")
def answer_question(question_id: int, answer: str):
  """Answers a question."""
  questions = load_questions()
  question = questions[question_id]
  if answer.lower() == question["correct_answer"].lower():
    return {"correct": True}
  else:
    return {"correct": False}

if __name__ == "__main__":
  app.run(debug=True)
