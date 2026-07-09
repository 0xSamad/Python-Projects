class QuizBrain:
    def __init__(self,q_list):
        self.number = 0
        self.question_list = q_list
        self.score =0

    def still_has_question(self):
        if self.number < len(self.question_list):
            return True
        return False

    def next_question(self):
        current_question = self.question_list[self.number]
        self.number+=1
        choice = input(f"Q. {self.number} : {current_question.text} ? (True/False)? : ")
        self.check_answer(choice,current_question.answer)

    def check_answer(self,choice,answer):
        if choice.lower()== answer.lower():
            print("You got it right")
            self.score+=1
        else:
            print("you got it wrong")
        print(f"The correct answer was {answer}")
        print(f"The current score is {self.score}/{self.number}")
        print("\n")
