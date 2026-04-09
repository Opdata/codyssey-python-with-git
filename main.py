from io_handler import IOHandler

io = IOHandler()
quizzes = []
score = 0

try:
    while True:
        io.display_menu(quizzes, score)
        choice = io.select_menu()

        if choice == 1:
            pass  # 퀴즈 풀기
        elif choice == 2:
            pass  # 퀴즈 추가
        elif choice == 3:
            pass  # 퀴즈 목록
        elif choice == 4:
            pass  # 점수 보기
        elif choice == 5:
            break
        
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")
except EOFError:
    print("\n프로그램을 종료합니다.")