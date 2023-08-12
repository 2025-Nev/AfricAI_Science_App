from typing import List

class Question:
  """A question in the science quiz app."""

  def __init__(self, question: str, answers: List[str], correct_answer: str):
    self.question = question
    self.answers = answers
    self.correct_answer = correct_answer

  def is_answer_correct(self, answer: str) -> bool:
    """Returns True if the answer is correct, False otherwise."""
    return answer.lower() == self.correct_answer.lower()

def load_questions() -> List[Question]:
  """Loads the questions from the questions.json file."""
  with open("questions.json", "r") as f:
    questions_json = json.load(f)
  questions = []
  for question_json in questions_json["questions"]:
    question = Question(
      question_json["question"],
      question_json["answers"],
      question_json["correct_answer"]
    )
    questions.append(question)
  return questions
