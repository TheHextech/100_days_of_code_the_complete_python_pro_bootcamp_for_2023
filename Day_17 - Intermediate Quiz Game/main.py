from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo, game_over


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print(logo)

while quiz.still_has_question():
    quiz.next_question()

print(game_over)

