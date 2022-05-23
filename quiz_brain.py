class QuizzBrain:
    def __init__(self,q_list):
        self.q_list = q_list
        self.q_index = 0
        self.score = 0
        self.max_score = len(q_list)

    # def still have questions(self):
    def still_have_questions(self):
        return self.q_index < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_index]
        if self.q_index < len(self.q_list):
            self.q_index += 1
            answer = input(f"Q.{self.q_index} {current_question.text} (True/False)")
            self.check_answer(answer)
        else:
            print("You have finished the quiz")
            print(f"Your score: {self.score}")



    #check answer
    def check_answer(self,answer):
        if answer.lower() == self.q_list[self.q_index-1].answer.lower():
            self.score += 1
            print("Correct")
        else:
            print("Wrong")


    #check score
    def check_score(self):
        print(f"Your score: {self.score}")




