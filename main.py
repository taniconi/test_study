import random
import time

# 質問と回答を持ってくる
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

# 質問と答え読み込んであげる
questions = load_data('test_study/data/answers.txt')
answers = load_data('test_study/data/questions.txt')

def play_quiz():
    while True:
        # ランダムに質問
        index = random.randint(0, len(questions) - 1)

        print(questions[index])
        user_answer = input("入力せよ: ")

        if user_answer.lower() == answers[index].lower():
            print("せいかい")
        else:
            print(f"こたえ「{answers[index]}」")

play_quiz()