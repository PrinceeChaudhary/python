total = 0
while True:
    user_number = int(input("Enter the number"))
    if user_number == 0:
        print(f"your total is {total}")
        break
    else:
      total = total + user_number
