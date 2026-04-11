# 게임 전체를 관리하는 클래스
# 메서드 : 메뉴 표시, 퀴즈 풀기, 퀴즈 추가, 목록 보기, 점수 확인, 파일 저장/불러오기 등
import file_handler as FileHandler
from io_handler import IOHandler
from quiz import Quiz
import random

class QuizGame:
    def __init__(self, quizzes: list[Quiz], high_score: int):
        self.quizzes = quizzes
        self.score = 0
        self.answer_count = 0
        self.high_score = high_score
        self.io = IOHandler()

    # 저장된 퀴즈 출제 및 입력 과 정답 확인
    def play_quiz(self):
        # 퀴즈 선정
        if len(self.quizzes) == 0:
            self.display_no_quizzes()
            return

        selected_quizzes = random.sample(self.quizzes, min(5, len(self.quizzes)))

        # 퀴즈 출제 및 입력 받고 정답 체크
        for quiz in selected_quizzes:
            self.io.display_quiz(quiz)
            inputed_answer = self.input_answer()
            self.check(quiz, inputed_answer)

        score = round((self.answer_count / len(selected_quizzes)) * 100)
        self.result(score)

    # 사용자가 정답을 입력 할 수 있다.
    def input_answer(self) -> int:
        return self.io.select_answer()

    # 정답/오답 여부를 알려준다.
    def check(self, quiz: Quiz, inputed_answer: int):
        check = quiz.check_answer(inputed_answer)

        if check:
            self.answer_count += 1
            self.io.display_correct()
        else:
            self.io.display_wrong()

    # 모든 문제를 풀면 결과 표시 및 최고 점수 저장
    def result(self,score):
        self.io.display_result(self.answer_count, score)
        if score > self.high_score:
            save_state = FileHandler.save_score(score)
            self.io.display_save_error(save_state)
        
    # 퀴즈가 없는 경우를 처리한다.
    def display_no_quizzes(self) -> None:
        print("아직 퀴즈가 없습니다.")