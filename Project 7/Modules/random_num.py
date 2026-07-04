import random

def random_num():
    try:
        start = int(input("Enter Starting Range: "))
        end = int(input("Enter Ending Range: "))

        result = random.randint(start, end)
        
        print(f"Random Integer is: {result}")
            
    except ValueError:
        print("Dont be ovesmart, Enter Valid Integers..🤚🤚🤚")

def random_list():
    try:
        count = int(input("Total numbers You Want In Your List? "))
        start = int(input("Enter Starting Range: "))
        end = int(input("Enter End Range: "))

        random_list = [random.randint(start, end) for _ in range(count)]
        
        print(f"Generated List: {random_list}")
            
    except ValueError:
        print("Dont be ovesmart, Enter Valid Integers..🤚🤚🤚")

def generate_password():
    try:
        length = int(input("Enter password length: "))

        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        symbols = "!@#$%^&*()-_=+"
        
        characters = letters + digits + symbols

        password = ''.join(random.choice(characters) for _ in range(length))
        
        print(f"Your random password is: {password}")
            
    except ValueError:
        print("Dont be ovesmart, Enter a valid integer for the length.🤚🤚🤚")

def generate_otp():
    
    digits = "0123456789"
    otp = ""

    for i in range(6):
        otp = otp + random.choice(digits)
        
    print(f"Your Generated OTP is: {otp}")