from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    text = item["question"]
    ans = item["correct_answer"]
    new_ques = Question(text,ans)
    question_bank.append(new_ques)
    #qb now has question_bank = [(text,ans),(text,ans)]


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
