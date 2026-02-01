#question 2
#break → stops the loop completely.
#continue → skips the current iteration and moves to the next one.
#question3
#for loop	
#Used when number of iterations is known.
#Iterates over sequences.
#while loop
#Used when condition-based repetition
#Iterates over sequences	Repeats while condition is True.
#question4
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
#homeworktask1
from collections import Counter

def uncommon(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for k in c1:
        if k not in c2:
            result += [k] * c1[k]
        else:
            diff = c1[k] - c2[k]
            if diff > 0:
                result += [k] * diff

    for k in c2:
        if k not in c1:
            result += [k] * c2[k]
        else:
            diff = c2[k] - c1[k]
            if diff > 0:
                result += [k] * diff

    return result
#homeworktask2
n = 5
for i in range(1, n):
    print(i*i)
#homeworktask3
vowels = "aeiou"

def transform(txt):
    result = ""
    count = 0

    for i in range(len(txt)):
        result += txt[i]
        count += 1

        if count == 3 and i != len(txt)-1:
            if txt[i] in vowels or (i+1 < len(txt) and txt[i+1] == "_"):
                continue
            result += "_"
            count = 0

    return result
#homeworktask4
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
#homeworktask5
pwd = input("Enter password: ")

if len(pwd) < 8:
    print("Password is too short.")
elif not any(c.isupper() for c in pwd):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")
#homeworktask6
for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
#bonus
import random

choices = ["rock", "paper", "scissors"]
player = 0
computer = 0

while player < 5 and computer < 5:
    user = input("rock / paper / scissors: ").lower()
    comp = random.choice(choices)
    print("Computer:", comp)

    if user == comp:
        print("Draw")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win this round")
        player += 1
    else:
        print("Computer wins this round")
        computer += 1

    print("Score:", player, ":", computer)

if player == 5:
    print("You won the match!")
else:
    print("Computer won the match!")
