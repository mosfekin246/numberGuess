import random 

def default():
    correct_answer = random.randint(0,50)
    print(correct_answer)
    round = 0
    take_input(correct_answer,round)


def restart():
    start = input("press 'y' if you want to start game again: ")
    if(start == 'y' or start == 'Y'):
        default()
    else:
        print("end game")


def compare(correct_answer,round):
    while(round<5):
        guessed_number = int(input("take a guess from 0 to 50: "))
        if(guessed_number>correct_answer):
            print("hint: correct answer is lower \nchances left: ",4-round)
        elif(guessed_number<correct_answer):
            print("hint: correct answer is higher \nchances left: ",4-round)
        else:
            print("win!!!!")
            round = 5
            restart()
        round += 1
    return round
        

def take_input(correct_answer,round):
    round = compare(correct_answer,round)
    if(round == 5):
        print("lose!!!")
        restart()

default()   




