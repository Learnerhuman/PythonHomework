import random

while True:
    secret = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        guess = int(input("Enter number: "))
        if guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
        attempts -= 1

    if attempts == 0:
        print("You lost. Want to play again?")
        ans = input()
        if ans.lower() not in ["y", "yes", "ok"]:
            break