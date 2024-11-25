#1
try:
    inp = input()
    with open(f"{inp}.txt","r") as file:
        line=file.readlines()
        print(line)
except OSError as e:
    print(e)

#2
import math
try:
    num = int(input())
    if(num<=0):
        raise ValueError("“Invalid Number")
    b = math.sqrt(num)
    print(b)
except (TypeError, ValueError) as e:
    print(e)
finally:
    print("Good Bye")


#3
import random
import string
import re

def validate_password(password):
    if len(password) < 8:
        raise ValueError("The password must be at least 8 characters long.")

    if not any(ele.isupper() for ele in password):
        raise ValueError("The password must contain at least one uppercase letter.")

    if not any(ele.islower() for ele in password):
        raise ValueError("The password must contain at least one lowercase letter.")

    if not any(ele.isdigit() for ele in password):
        raise ValueError("The password must contain at least one digit.")

    if not any(char in "!@#$%^&*()." for char in password):
        raise ValueError("The password must contain at least one special character (!@#$%^&*().)")

    if " " in password:
        raise ValueError("The password cannot contain spaces.")

    forbidden_words = ["password", "1234", "qwerty", "admin"]
    if any(word in password.lower() for word in forbidden_words):
        raise ValueError("The password cannot contain 'password', '1234', 'qwerty', or 'admin'.")

    return True

def generate_password(leng):
    if leng < 8:
        raise ValueError("Password length must be at least 8 characters.")

    password = ''.join(random.choices(string.ascii_lowercase, k=leng))

    index_upper = random.randint(0, len(password) - 1)
    password = password[:index_upper] + password[index_upper].upper() + password[index_upper + 1:]

    index_digit = random.randint(0, len(password) - 1)
    password = password[:index_digit] + str(random.randint(0, 9)) + password[index_digit + 1:]

    special_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    index_symbol = random.randint(0, len(password) - 1)
    symbol = random.choice(special_symbols)
    password = password[:index_symbol] + symbol + password[index_symbol + 1:]

    return password

def improve_password(password):
    if len(password) < 8:
        needed = 8 - len(password)
        password += ''.join(random.choices(string.ascii_letters + string.digits, k=needed))

    if not any(char.isupper() for char in password):
        index_upper = random.randint(0, len(password) - 1)
        password = password[:index_upper] + password[index_upper].upper() + password[index_upper + 1:]

    if not any(char.islower() for char in password):
        index_lower = random.randint(0, len(password) - 1)
        password = password[:index_lower] + password[index_lower].lower() + password[index_lower + 1:]

    if not any(char.isdigit() for char in password):
        index_digit = random.randint(0, len(password) - 1)
        password = password[:index_digit] + str(random.randint(0, 9)) + password[index_digit + 1:]

    if not any(char in "!@#$%^&*()." for char in password):
        special_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
        index_symbol = random.randint(0, len(password) - 1)
        symbol = random.choice(special_symbols)
        password = password[:index_symbol] + symbol + password[index_symbol + 1:]

    return password

try:
    user_password = input()
    validate_password(user_password)
    print("Password is valid!")

    new_password = generate_password(10)
    print("Generated Password:", new_password)

    weak_password = input()
    improved_password = improve_password(weak_password)
    print("Improved Password:", improved_password)

except Exception as e:
    print("Error:", e)
