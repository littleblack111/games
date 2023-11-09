import random

def game():
    print("choose:\n1 - rock \n2 - paper \n3 - sissor")
    player = int(input("> "))
    bot = random.randint(1,3)
    if player > bot and abs(player-bot) != 2:
        return 1
    else:
        return 0

print("Win two out of three games(1) or decide the outcome in one game(2)?")
mode = input("enter a number > ")
match mode:
    case "1":
        resultReal = 1
        for i in range(3):
            result = game()
            if result:
                print(f"player win this round!")
            else:
                print(f"bot win this round!")
            resultReal = resultReal + result
        if resultReal <= 2:
            print("\nbot win the game!")
        else:
            print("\nplayer win the game!")
    case "2":
        result = game()
        if result:
            print(f"player win!")
        else:
            print(f"bot win!")


from stdlib import *
from random import randint

def initAnswer() -> int:
    return randint(1, 3)

