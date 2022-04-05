class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.score = 0
        self.num_of_question_asked = 0
        self.total_questions = len(self.q_list)
        self.on_game = True


    def quiz(self, diff_lvl, category):
        self.new_question = []
        for question in self.q_list:
            if question["difficulty"] == diff_lvl and question["category"] == category:
                answer = input(f'\n{question["question"]}. (True/False): ')
                self.num_of_question_asked += 1

                if answer == question["correct_answer"]:
                    self.score += 1
                    print (f"{answer}! is correct")
                    print(f"Your score is {self.score}/{self.num_of_question_asked}")
                else:
                    print (f"{answer}! is wrong")
                    print(f"Your score is {self.score}/{self.num_of_question_asked}")


        self.on_game = False

