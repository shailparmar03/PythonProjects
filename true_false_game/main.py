from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

ques_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    ques_bank.append(new_question)

quiz=QuizBrain(ques_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

