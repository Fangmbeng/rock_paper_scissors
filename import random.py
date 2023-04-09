import random

def start():
    choic = input("rock, paper, or scissore: ")
    return choic

def game():
    play = start()
    results = " "
    list1 = ["paper", "rock", "scissors"]
    random_chose = random.choice(list1)
    if play == random_chose:
        results += "Tie results"
        print(random_chose)
        return results
    elif play == "paper" and random_chose == "rock":
        results += "you win"
        print(random_chose)
        return results
    elif play == "paper" and random_chose == "scissors":
        results += "you loose"
        print(random_chose)
        return results
    elif play == "rock" and random_chose == "paper":
        results += "you loose"
        print(random_chose)
        return results
    elif play == "rock" and random_chose == "scissors":
        results += "you win"
        print(random_chose)
        return results
    elif play == 'scissors' and random_chose == "paper":
        results += "you win"
        print(random_chose)
        return results
    elif play == "scissors" and random_chose == 'rock':
        results += "you lose"
        print(random_chose)
        return results
    else:
        return 'Invalid Input'

def app():
    test = game()
    print(test)
    choose = input("Continue or quit: ")
    if choose.lower() == "continue":
        return app()
    elif choose.lower() == "quit":
        return "Game Ended"
    else:
        return "Invalid Syntax, Try Again" and app()


print(app())