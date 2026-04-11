# json 로드, 쓸때 인코딩(utf-8), 
""" json schema
{
  "quizzes": [
    {
      "question": "",
      "choices": [],
      "answer": 1
    }
  ],    
  "score": 0
}

"""
import json

# 파일이 없으면 기본퀴즈 데이터 사용, 손상되었다면 안내메시지 출력 후, 기본 퀴즈 데이터로 복구(또는 초기화)한다.
def _load():
    try:
        with open("state.json", "r", encoding="utf-8") as f:
            return "success",json.load(f)
    except FileNotFoundError:
        return "not_found",None
    except json.JSONDecodeError:
        return "corrupted", None 

def _write(quizzes, score) -> tuple[str, None]:
    try:
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump({"quizzes": quizzes, "score": score}, f, ensure_ascii=False, indent=2)
        return "success", None
    except IOError:
        return "fail_write", None

# 퀴즈 데이터, 최고 점수 불러오기 / return 퀴즈 리스트, 최고 점수
def load_existing() -> tuple[list, int]:
    state, existing_data = _load()
    if state == "success":
        return existing_data.get("quizzes", []), existing_data.get("score", 0)
    elif state == "not_found":
        return [], 0
    else:  # corrupted
        return [], 0

# 퀴즈 저장
def save_quiz(quiz):
    existing_quizzes, existing_score = load_existing()

    new_quiz = {
        "question": quiz.question,
        "choices": quiz.choices,
        "answer": quiz.answer
    }

    state, _ = _write(existing_quizzes + [new_quiz], existing_score)
    return state

# 최고 점수 저장
def save_score(_score):
    existing_quizzes, _ = load_existing()
    state, _ = _write(existing_quizzes, _score)
    return state