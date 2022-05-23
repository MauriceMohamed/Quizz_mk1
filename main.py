#import question model and data
from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

#create a list of Question objects
question_bank = []

#loop through question_data and create Question objects
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quizz = QuizzBrain(question_bank)
while quizz.still_have_questions():
    quizz.next_question()
    quizz.check_score()

print("You have finished the quiz")
print(f"Your score: {quizz.score}")

