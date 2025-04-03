result = "tokyo"
user_result = ""
number_attempts=5

while True:
    user_answer=input("what is the capital city of Japan? \n")
    if (user_result == result):
        print("You gave correct answer")
        break
    else:
        number_attempts -= 1
        if number_attempts > 0:
            print(f"incorrect answer. You have {number_attempts} attempts left")
        else:
            print("reached max number of attempts")
            break
