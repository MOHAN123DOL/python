#we can play a quiz game
score=0
print("welcome to you! you want to play quiz game ")#welcome 
choice=input("yes or no   ")#to know the user interest
if (choice=="yes"):#nested if
    print("your first question is")
    question1=input("what is capital of france?  ")#question1
    if question1.lower()=="paris":
        print("wow!correct answer")
        score+=1
    else:
        print("oops!wrong,try another")

    question2=input("whice planet is know as red planet?  ")#question2
    if question2.lower()=="mars":
        print("wow!correct answer")
        score+=1
    else:
        print("oops!wrong,try another")
    question3=input("which is a largest mammal in the world?  ")#question3t
    if question3.lower()=="blue whale":
        print("wow!correct answer")
        score+=1
    else:
        print("oops!wrong,try another")
    question1=input("who wrote the play romeo and juliet  ")#question44
    if question1.lower()=="william":
        print("wow!correct answer quiz over")
        score+=1
    else:
        print("oops!quiz over")
else:
    quit()
print("your score is",score)#to tell the score
print("your got a",((score/4)*100),"%")#to tell percentagey
