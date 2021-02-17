class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.list = list
        self.score = 0

    def next_question(self):
        current_question = self.list[self.question_number]
        question_text = current_question.text
        question_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q:{self.question_number}: {question_text} (True/False)?: ")
        self.check_answer(user_answer, question_answer)

    def still_has_questions(self):
        return self.question_number < len(self.list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You answered correctly!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

