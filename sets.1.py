user_numbers = set()
while True:
    if len(user_numbers) >=7
      break 
    try:
         user_input = int(input("Enter a number: \n"))

         if user_input in user_numbers:
             print("You already entered that number")

else:
        user_numbers.add(user_input)
    expect ValueError:
    print("Please enter only numbers")
print("Your lottery numbers are:")
for number in user_numbers:
     print(number)