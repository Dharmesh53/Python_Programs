class Quiz:
    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def has_next(self):
        return len(self.question_list) > self.question_no

    def next(self):
        current_ques = self.question_list[self.question_no]
        self.question_no = self.question_no + 1
        user_ans = str(input(f"Q.{self.question_no}: {current_ques.text} (True/False) : ")).lower()
        self.checker(current_ques.answer, user_ans)

    def checker(self, correct, user):
        if correct.lower() == user.lower():
            self.score = self.score + 1
            print("You got it right")
        else :
            print("Oops, Wrong answer")

        print(f"Your score is {self.score}/{len(self.question_list)}")
