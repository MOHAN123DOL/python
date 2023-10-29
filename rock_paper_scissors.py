#simple game but interesting game "rock paper scissors"
from random import randint
options=["rock","paper","scissors"]
choice=input("you want to play a game yes or no  ").lower()
if choice=="yes":
    score=0
    try1=0
    while True:
        random=randint(0,2)
        user_choice=input("what is your option = rock,paper,scissors or you want to quit  ").lower()
        try1+=1
        computer_choice=options[random]
        #rock 0 paper 1 scissors 2
        if user_choice=="quit":
           try1=try1-1
           break
        elif user_choice not in options:
            print("not in the options enter the valid options")
            continue
        elif computer_choice==user_choice:
            print("same  option try another ")
            continue
        elif user_choice=="rock" and computer_choice=="scissors":
            print("computer choice is ",computer_choice," you won")
            score+=1
            continue
        elif user_choice=="scissors" and computer_choice=="paper":
            print("computer choice is ",computer_choice," you won")
            score+=1
            continue
        elif user_choice=="paper" and computer_choice=="rock":
            print("computer choice is ",computer_choice," you won")
            score+=1
            continue
        else:
             print("computer choice is ",computer_choice," you lose")
             continue
    print("your score is ",score," out of ",try1)
        
        

        

