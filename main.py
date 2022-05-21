from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

#print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question(): #checks if there are more question left in the list
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")