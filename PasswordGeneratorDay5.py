import random

varLetters = ["a","b","c","d","e","f","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
varNumbers = ["1","2","3","4","5","6","7","8","9"]
varSymbol = ["!","@","#","$","%","^","&","*"]

print("Welcome to python generator!")

varInputLetters = int(input("How many letters you would like: "))
varInputSymbols = int(input("How many symbols you would like: "))
varInputNumbers = int(input("How many numbers you would like: "))



# Letters loop
#for l in range(varInputLetters):
   # varPassword += random.choice(varLetters)

# Symbols loop
# for s in range(varInputSymbols):
# varPassword += random.choice(varSymbol)

# Numbers loop
# for n in range(varInputNumbers):
   # varPassword += random.choice(varNumbers)


#HardLevel
password_List = []
# Letters loop
for l in range(varInputLetters):
        password_List.append(random.choice(varLetters))
# Symbols loop
for s in range(varInputSymbols):
    password_List.append(random.choice(varSymbol))

# Numbers loop
for n in range(varInputNumbers):
    password_List.append(random.choice(varNumbers))
    random.shuffle(password_List)
    varPassword = ""
    for char in password_List:
            varPassword += char
            print(varPassword)