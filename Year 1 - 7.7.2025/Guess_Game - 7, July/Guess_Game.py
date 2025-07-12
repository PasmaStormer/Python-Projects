
def Guess_Game():
    import random
    secret_number = random.randint(1, 10)
    guess = 0
    tries = 1

    print("I am thinking of a number from 1 to 10")
    print("You only have 3 tries!")

    while guess != secret_number and tries <= 3:
        guess = int(input("Take a guess: "))
        if guess > secret_number:
            print("The number is too big, guess a smaller one")
            tries += 1
        elif guess < secret_number:
            print("The number is too small, guess a bigger one")
            tries += 1
        else:
            print("You got it right!")
            print("It took you ", tries, " tries!")
            break

    if guess != secret_number:
        print("You lost, it took more than 3 tries")
        print("The number was ", secret_number)


while True:
    Guess_Game()
    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != "yes":
        print("Thanks for playing!")
        break








