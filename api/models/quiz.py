from typing import List
from api.models.questions import Question, get_questions


class Quiz:
    def __init__(self, questions: List[Question]):
        """Creates a new quiz."""
        self.questions = questions
        self.current_question = 0
        self.score = 0

    def get_current_question(self) -> Question:
        """Returns the current question."""
        return self.questions[self.current_question]

    def is_answer_correct(self, answer: str) -> bool:
        """Returns True if the given answer is correct for the current question, False otherwise."""
        return self.get_current_question().is_answer_correct(answer)

    def answer_question(self, answer: str) -> bool:
        """Answers the current question and returns True if the answer is correct, False otherwise."""
        if self.is_answer_correct(answer):
            self.score += 1
            self.current_question += 1
            return True
        else:
            return False

    def is_finished(self) -> bool:
        """Returns True if the quiz is finished, False otherwise."""
        return self.current_question >= len(self.questions)

    def get_score(self) -> int:
        """Returns the score for the quiz."""
        return self.score

    # Missing implementation for the get_questions function
    def get_questions() -> List[Question]:
        # Implement the function logic here
        pass
