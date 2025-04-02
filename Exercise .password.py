correct_password = "ABCD"
number_attempts = 0
max_attempt = 3
input_password = ""
while attempt < max_attempt and input_password !=correct_password:
    input_password = input("Enter your password")
    if input_password == correct_password:
        print("Access granted")
    else:
        attempt += 1
        print(f"Incorrect password. Number of attempt {attempt}/{max_attempt}")
        if attempt == max_attempt:
            print("Too many attempts. Your acount is blocked.")