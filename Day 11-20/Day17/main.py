from questionModel import Question
from data import question_data
from ques_Brain import Quiz

question_bank = []

for question in question_data:
    question_Text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_Text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.has_next():
    quiz.next()
