user_number = set()
wining_num={10,25,32,41,43,45,50}
prize= 0

while True:
    try:
        if len(user_number) < 7:
            num= int(input("Enter the Seven lottery numbers \n"))
        if num in user_number:
            print("The Number you enter is already here in the list")
            break
        else:
            user_number.add(num)
        if len(user_number)==7:
            break
    except ValueError:
        print("Invalid. Please enter number only")

if len(user_number)==7:
    matching_num= user_number.intersection(wining_num)
    count_num = len(matching_num)
    print(f"The matching numbers are {matching_num}")

if count_num ==3:
    prize = 4
elif count_num == 4:
    prize = 15
elif count_num == 5:
    prize = 200
elif count_num == 6:
    prize = 30000
elif count_num ==7:
    prize= 500000


if prize >= 3:
    print(f"You won ${prize}")
else:
    print("Sorry, Better Luck next time")
