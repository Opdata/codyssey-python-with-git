import file_handler

class IOHandler:
    def __init__(self):
        pass

    def _valid_question_input(self, value: str):
        # TODO: 퀴즈 입력의 경우 null, undefined, None, False, True, "", " " 이런건 다 공통으로
        pass

    # 숫자 검증
    def _validate_number_input(self, value: str, min: int, max: int) -> tuple[str, int | None]:
        sanitized = value.strip()

        if not sanitized:
            return "empty", None

        if not sanitized.isdigit():
            return "not_digit", None

        num = int(sanitized)

        if not (min <= num <= max):
            return "out_of_range", None

        return "success", num

    # 예외에 따른 메시지 출력
    def _display_number_warning(self, reason: str, min: int, max: int) -> None:
        messages = {
            "empty":        "⚠️ 값을 입력해주세요.",
            "not_digit":    "⚠️ 숫자만 입력해주세요.",
            "out_of_range": f"⚠️ {min}~{max} 사이의 숫자를 입력해주세요.",
        }
        print(messages.get(reason, "⚠️ 올바르지 않은 입력입니다."))

    # 숫자 입력, args string / min / max(range)
    # 정상 범위의 숫자가 아닐시 경고 출력
    def _input_number(self, prompt: str, min: int, max: int) -> int:
        while True:
            value = input(prompt)
            reason, result = self._validate_number_input(value, min, max)

            if reason != "success":
                self._display_number_warning(reason, min, max)
                continue

            return result

    # 메뉴 출력 및 데이터 존재 시 안내 메시지 출력
    def display_menu(self, load, quizzes, high_score) -> None:
        print("========================================")
        print("            🎯 나만의 퀴즈 게임 🎯           ")
        print("========================================")
        if load:
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {high_score}점)")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 보기")
        print("5. 종료")
        print("========================================")

    # 메뉴 선택 
    def select_menu(self) -> int:
        return self._input_number("선택 : ", 1, 5)

    # 정답 선택
    def select_answer(self) -> int:
        return self._input_number("정답 : ", 1, 4)

    # 최고 점수 출력
    def display_score(self, score) -> None:
        if score == 0:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {score}점")
    
    # 퀴즈 출력
    def display_quiz(self, quiz) -> None:
        print(quiz.question)
        for i, choice in enumerate(quiz.choices):
            print(f"{i + 1}. {choice}")

    # 퀴즈 목록 출력
    def display_quiz_list(self, quizzes) -> None:
        if len(quizzes) == 0:
            print("아직 퀴즈가 없습니다.")
        else:
            print(f"등록된 퀴즈 목록 (총 {len(quizzes)}개)")
            for i, quiz in enumerate(quizzes):
                print(f"{i + 1}. {quiz.question}")

    # 정답 메시지 출력
    def display_correct(self) -> None:
        print("✅ 정답입니다!")

    # 오답 메시지 출력
    def display_wrong(self) -> None:
        print("❌ 땡!")

    def _display_new_high_score(self, score, existing_score) -> None:
        if score > existing_score:
            print("새로운 최고 점수 입니다!")

    # 맞힌 문제 개수, 점수 출력
    def dispaly_result(self, answer_count, score) -> None:
        # 점수 계산 필요 => 식 : (맞긴 문제 개수 / 총 문제 수(저장된 문제의 길이가 5보다 크면 5로 고정이고, 작다면 문제의 길이) * 100)
        quizzes, existing_score = file_handler.load_existing()
        if len(quizzes) >= 5:
            total_questions = 5
        else:
            total_questions = len(quizzes)
        score = (answer_count // total_questions) * 100
        print("========================================")
        print(f"결과: 5문제 중 {answer_count}문제 정답! ({score}점)")
        self._display_new_high_score(score, existing_score)
        print("========================================")
    
    # 퀴즈 추가
    def display_add_quiz(self) -> None:
        quiz = {
            "question": "",
            "choices": [],
            "answer": 0
        }
        print("\n")
        print("🎯 새로운 퀴즈를 추가합니다.\n")
        quiz["question"] = input("문제를 입력하세요 : ")
        for i in range(4):
            quiz["choices"].append(input(f"선택지 {i+1}: "))
        quiz["answer"] = self._input_number("정답 번호 (1-4):", 1, 4)
        
        reason, result = file_handler.save_quiz(quiz)
        if reason == 'success':
            print("\n✅ 퀴즈가 추가되었습니다.")
        else:
            print("\n❌ 퀴즈 추가에 실패했습니다.")

    def display_save_error(_state):
        if _state == 'success':
            print("\n✅ 데이터 저장에 성공했습니다.")
        else:
            print("\n❌ 데이터 저장에 실패했습니다.")