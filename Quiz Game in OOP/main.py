from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

#for item in range(len(question_data)):
#    question_bank.append(Question(question_data[item]["text"],question_data[item]["answer"]))


for question in question_data:
    query = question["text"]
    answer = question["answer"]
    new_question = Question(query,answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.number}")