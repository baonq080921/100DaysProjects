from Question_model import Question
from data import question_data
from quizbrain import QuizzBrain
question_bank=[]

# while is_continue:
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
quiz=QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've complete the quizz.")
print(f"Your final score is {quiz.score} out of {len(question_bank)}")

