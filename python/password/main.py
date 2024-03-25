def special(amongus):
    specials = "!?@#$%_-"
    for x in specials:
        if x in amongus:
            return 1
    return 0

def num_char(amongus):
    uppercaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    safety = 0
    for x in uppercaseLetter:
        if x in amongus:
            safety += 1
            break
    for x in uppercaseLetter.lower():
        if x in amongus:
            safety += 1
            break
    for x in numbers:
        if x in amongus:
            safety += 1
            break
    return safety

def safety(amongus):
    return special(amongus) + num_char(amongus) 

savedPasswords = []
def similarity(amongus):
    global savedPasswords
    print(amongus)
    for x in savedPasswords:
        if amongus == x:
            return 1
    savedPasswords.append(amongus)
    return 0

while(True):
    password = input("Password input: ")
    if len(password) >= 8:
        print(f"Your password is infact usable good job :3 : {safety(password)}/5")

        if similarity(password):
            print("your password matches with another one (not saved)")
        else:
            print("your password matches with neither of your passwords (saved hash)\n")
        if input("Store a new password? [y/n]: ").upper() == 'n'.upper():
            break
    else:
        print("Password length must be atleast 8 characters long.")