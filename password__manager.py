#in this program you have to save the password 


from cryptography.fernet import Fernet #encrypt or decrypte out password with is module

'''
def write_key():#function definition
    key = Fernet.generate_key() #we can open the key file to store key value as bytes
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():#function definition
    file = open("key.key", "rb")#we can be read bytes in the line file can be open,read,close this file
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():#function definitionS
    with open('passwords.txt', 'r') as f:#use of with is can automatically closed the file after use
        for line in f.readlines():
            data = line.rstrip()#the space can be with is use of rstrip
            user, passw = data.split("|")#split the username and password in respected to "|""
            print("User:",user,"| Password:",
                  fer.decrypt(passw.encode()).decode()))#we can decrypt the value already encrypte
            


def add():
    name = input('user name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")#encrypte this password


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        name=input("enter the owner name to access all password or enter your name to see only other name:  ").lower()
        if name=="mohan":
            view()#fuction calling
    elif mode == "add":
        add()#fuction calling
    else:
        print("Invalid mode.")
        continue