from random import randint
print("welcome to you! you want to play number game ")#welcome 
choice=input("yes or no   ")#to know the user interest
if (choice.lower()=="yes"):#nested if
    max_num=int(input("enter the maximum value to be your stop   "))
    if max_num<=0:
        print("please enter greater than zero")
        
    else:
        print("ok you have to play a game")
        name_of_user=input("enter your name  ")
    random_num=randint(0,max_num) #we can generate a random number by the module 
    loop=0
    while True: #it can run continously untill break statement arrives
        loop+=1 #we can determine the score of user
        guess_num=int(input("guess a number   "))
        if guess_num != random_num:
            print("oops wrong....! other quess")
            continue #loop run untill the user choose the correct number
        if guess_num == random_num:
            print("you done..!")
            break
    score=(max_num-loop)+1
    print(" hello",name_of_user,"your score is",str(score)+"....! out of ",max_num)
    print("your percentage is",((score/max_num)*100),"%")

else:
    quit()
        