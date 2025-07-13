def greet_user():
    name = input("👋 Hello! What is your name? → ")
    print("Welcome,",name)
    print("Lets start this quiz")
    return name

def ask_question(question,option,correct_number):
    print(question)
    for i in range(len(option)):
        print(f"{i+1}. {option[i]}")

    while True:
        user_answer = input("Enter an answer from 1 to 4")
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if 1 <= user_answer <= 4:
                break
            else:
                print("Enter a value in between or equel to 1 and 4")
        else:
            print("Not a valid answer, please try again")

    if user_answer == correct_number:
        return 1
    else:
        return 0

def run_quiz():
    score = 0

    score += ask_question(
        "What is the capital of France? ",
        ["Berlin", "Madrid", "Paris", "Rome"],
        3
    )

    score += ask_question(
        "Which number is even? ",
        ["3", "7", "10", "9"],
        3
    )

    score += ask_question(
        "Which language are we using? ",
        ["Java", "C++", "Python", "HTML"],
        3
    )

    return score


name = greet_user()
total_score = run_quiz()
print(f"Thanks for playing, {name}! You scored {total_score}/3.")
