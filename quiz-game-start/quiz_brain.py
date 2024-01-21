# TODO 1: Asking the Questions
# TODO 2: Checking if the answer was correct
# TODO 3: Checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The Correct answer was : {correct_ans}.")
        print(f"Your Current Score is : {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        correct_ans = current_question.ans
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_ans,correct_ans)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


