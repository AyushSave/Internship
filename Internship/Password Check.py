password = input("Enter your password: ")

has_number = False
has_special = False
has_uppercase = False

special_characters = "!@#$%^&*()-_+=?"

for char in password:
    if char.isdigit():
        has_number = True
    elif char.isupper():
        has_uppercase = True
    elif char in special_characters:
        has_special = True

if len(password) >= 8 and has_number and has_special and has_uppercase:
    print("Strong")
else:
    print("Weak")
