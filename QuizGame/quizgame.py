from data import logo, question_data
from quizbrain import QuizBrain
q_list = question_data
new_question = []


print(logo)


quizbrain = QuizBrain(q_list)
def start_quiz():
    diff_lvl = input("Choose a difficulty level: 'Easy' 'Medium' 'Hard': ").lower()
    category = input("Choose a Category: 'Computer' 'Math' 'Health': ").lower()

    while quizbrain.on_game:
        quizbrain.quiz(diff_lvl, category)
    else:
        print("\nNO MORE QUESTIONS AVAILABLE!!!")
        print(f"Your final score is {quizbrain.score}/{quizbrain.num_of_question_asked}")


on_admin = True
new_question = {}
while on_admin:
    admin = input("\nAdd user or Play: ").lower()
    if admin == "add":
        new_question["category"] = input("category: ")
        new_question["difficulty"] = input("difficulty: ")
        new_question["question"] = input("question: ")
        new_question["correct_answer"] = input("correct_answer: ")
        q_list.append(new_question)
        print(q_list)
    elif admin == "play":
        start_quiz()
    elif admin == "off":
        on_admin = False
    else:
        print("Invalid input")