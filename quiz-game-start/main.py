from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_quest = Question(question["question"],question["correct_answer"])
    question_bank.append(new_quest)

# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have Completed the Quiz! ")
print(f"Your Final Score is {quiz.score}/{quiz.question_number}")

