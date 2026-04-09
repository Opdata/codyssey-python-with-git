import file_handler

class IOHandler:
    def __init__(self):
        pass

    def _valid_question_input(self, value: str):
        # TODO: 퀴즈 입력의 경우 null, undefined, None, False, True, "", " " 이런건 다 공통으로
        pass

    # 숫자 검증
    def _validate_number_input(self, value: str, min: int, max: int) -> tuple[int | None, str]:
        sanitized = value.strip()

        if not sanitized:
            return None, "empty"

        if not sanitized.isdigit():
            return None, "not_digit"

        num = int(sanitized)

        if not (min <= num <= max):
            return None, "out_of_range"

        return num, "success"

    # 예외에 따른 메시지 출력
    def _print_number_warning(self, reason: str, min: int, max: int) -> None:
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
            result, reason = self._validate_number_input(value, min, max)

            if reason != "success":
                self._print_number_warning(reason, min, max)
                continue

            return result

    def display_menu(self, quizzes, score) -> None:
        print("========================================")
        print("            🎯 나만의 퀴즈 게임 🎯           ")
        print("========================================")
        if len(quizzes) > 0 or score > 0:
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {score}점)")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 보기")
        print("5. 종료")
        print("========================================")

    def select_menu(self) -> int:
        return self._input_number("선택 : ", 1, 5)

    def select_answer(self) -> int:
        return self._input_number("정답 : ", 1, 4)
