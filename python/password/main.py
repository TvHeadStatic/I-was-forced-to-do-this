def num_char(ඞ):
    uppercaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    sejf = 0
    for x in uppercaseLetter:
        if x in ඞ:
            sejf += 1
            break
    for x in uppercaseLetter.lower():
        if x in ඞ:
            sejf += 1
            break
    for x in numbers:
        if x in ඞ:
            sejf += 1
            break
    return sejf

def extraspeshl(ඞ):
    specials = "!?@#$%_-"
    for x in specials:
        if x in ඞ:
            return 1
    return 0

def sejf(ඞ):
    return num_char(ඞ) + extraspeshl(ඞ) 

savedPasswords = []
def sims(ඞ):
    global savedPasswords
    print(ඞ)
    for x in savedPasswords:
        if ඞ == x:
            return 1
    savedPasswords.append(ඞ)
    return 0

while(True):
    password = input("Password input: ")
    if len(password) >= 8:
        print(f"Your password is infact usable good job :3 : {sejf(password)}/5")

        if sims(password):
            print("Dumb b1- you can't resuse passwords (no saving for you)")
        else:
            print("Holy- you are so creative good job (saved)\n")
        if input("Ya want even more passwording ?! [y/n]").upper() == 'n'.upper():
            break
    else:
        print("Yo, you funny unlock word ain't long enough try again :3")