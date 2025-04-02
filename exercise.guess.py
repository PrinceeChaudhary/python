import random
guess_number = random.randint(0,100)


while True:
    user_number = int(input("Enter your number between 0 & 100"))
    try:
        if(user_number == guess_number):
            print("You are correct")
            break
        elif(user_number > guess_number):
            print("guess lower number")
        else:
            print("guess higher number")
    except ValueError:
        print("Invalid")