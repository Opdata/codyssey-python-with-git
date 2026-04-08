# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Codyssey Python learning assignment: a terminal-based quiz game. The goal is to build a working console app while practicing Python fundamentals, OOP, file I/O, and Git workflows.

## Running the Program

```bash
python main.py
```

No external dependencies — stdlib only. Requires Python 3.10+.

## Architecture

The program must have at least two classes:

- **`Quiz`** — represents a single quiz item with `question`, `choices` (4 options), and `answer` (int 1–4)
- **`QuizGame`** — manages the full game loop: menu display, quiz play, quiz add, list view, score tracking, and file save/load

Data is persisted to **`state.json`** at the project root (UTF-8). Schema:
```json
{
  "quizzes": [...],
  "best_score": 0
}
```

If `state.json` is missing, use hardcoded default quizzes (≥5). If it's corrupted, print a warning and fall back to defaults.

## Menu Structure

```
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
```

## Input Handling Rules

All numeric inputs must:
- Strip leading/trailing whitespace before processing
- Handle non-numeric input (show message, re-prompt)
- Handle out-of-range numbers (show message, re-prompt)
- Handle empty Enter (show message, re-prompt)
- Handle `KeyboardInterrupt` and `EOFError` gracefully — save state if possible, then exit cleanly

## Git Commit Style

```
Feat: 퀴즈 출제 기능 구현
Fix: 점수 계산 오류 수정
Docs: README 실행 방법 추가
Refactor: QuizGame 책임 분리
```
