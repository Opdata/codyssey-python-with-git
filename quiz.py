class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 퀴즈 출력 메소드
    def display_quiz(self) -> None:
        print(self.question+"\n")

        for i, choice in enumerate(self.choices):
            print(f"{i+1}. {choice}")
        print("\n")

    # 정답 확인 메소드 / True or False
    def check_answer(self, answer: int) -> bool:
        return self.answer == answer
            
