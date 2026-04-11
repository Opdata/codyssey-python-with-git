from file_handler import FileHandler
from io_handler import IOHandler

io = IOHandler()

default_quizzes = [
    {
        "question": "블록체인에서 각 블록에 포함되지 않는 것은?",
        "choices": ["이전 블록의 해시값", "거래 데이터", "타임스탬프", "사용자의 개인 비밀번호"],
        "answer": 4
    },
    {
        "question": "비트코인을 처음 제안한 사람(또는 그룹)의 이름은?",
        "choices": ["일론 머스크", "사토시 나카모토", "비탈릭 부테린", "닉 재보"],
        "answer": 2
    },
    {
        "question": "블록체인에서 새로운 블록의 유효성을 검증하고 체인에 추가하는 과정을 무엇이라고 하는가?",
        "choices": ["암호화 (Encryption)", "토큰화 (Tokenization)", "채굴 (Mining)", "포킹 (Forking)"],
        "answer": 3
    },
    {
        "question": "이더리움이 비트코인과 구별되는 가장 큰 특징은?",
        "choices": ["더 빠른 거래 속도", "스마트 컨트랙트 지원", "더 낮은 수수료", "중앙화된 관리 방식"],
        "answer": 2
    },
    {
        "question": "블록체인의 핵심 특성이 아닌 것은?",
        "choices": ["탈중앙화", "투명성", "불변성", "단일 서버 저장"],
        "answer": 4
    }
]

quizzes = []
high_score = 0
is_state_loaded = False

def set_quizzes():
    load_quizzes, load_score = FileHandler.load_existing()

    if len(load_quizzes) > 0:
        quizzes = load_quizzes
        is_state_loaded = True
    else:
        quizzes = default_quizzes
        is_state_loaded = False
    if load_score > 0:
        high_score = load_score
        is_state_loaded = True
    else:
        high_score = 0
        is_state_loaded = False

try:
    while True:
        set_quizzes()
        io.display_menu(is_state_loaded, quizzes, high_score)
        choice = io.select_menu()
        
        quiz_list = []
        for quiz in quizzes:
            quiz_list.append(Quiz(quiz["question"], quiz["choices"], quiz["answer"]))

        if choice == 1:
            quiz_game = QuizGame(quiz_list, high_score)
            quiz_game.play_quiz()
            
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