password = input("Enter your password: ")

score = 0
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-+?"

if len(password) >= 8:
    score += 1

for i in range(len(password)):
    character = password[i]

    if 65 <= ord(character) <= 90:
        has_upper = True
    elif 97 <= ord(character) <= 122:
        has_lower = True
    elif 48 <= ord(character) <= 57:
        has_digit = True
    elif character in special_characters:
        has_special = True

if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

print("Here is your password's strength score:", score)

if score <= 2:
    print("Weak password strength")
elif score == 3:
    print("Medium password strength")
elif score == 4:
    print("Strong password strength")
else:
    print("Very strong password strength")
