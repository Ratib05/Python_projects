import re 

def password_strength_checker(password):
    score = 0
    length = len(password)
    lowercase = re.search(r"[a-z]", password) is not None
    uppercase = re.search(r"[A-Z]", password) is not None
    digit = re.search(r"[0-9]", password) is not None
    special_char = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    if (length >= 8):
        score += 1
    if (uppercase == True):
        score += 1
    if (lowercase == True):
        score += 1
    if (digit == True):
        score += 1
    if (special_char == True):
        score += 1

    if (score == 5):
        return "Strong"
    elif (score >= 3):
        return "Medium"
    else:
        return "Weak"
    
password = input("Enter password: ")
print(password_strength_checker(password))