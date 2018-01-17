import webbrowser, re

def num_check(password):  # creates a three-digit check number by converting the password to a number, finding the modulo in the base of the last three base ten digits of the rest of the number: there are 1000 possible numbers, but it will be the same for any password
    passNum = ""
    for i in range(len(password)):
        passNum = passNum + str(ord(password[i]))
    passNumTwo = passNum
    divNum = passNum[3:]
    endThree = passNumTwo[:3]
    divNumber = int(divNum)
    endNumber = int(endThree)
    storePass = divNumber % endNumber
    storeString = str(storePass)
    for i in range(3 - len(storeString)):
        storeString = "0" + storeString
    return (storeString)


def num_verif(checkDigits, password):  # verifies, with the check number from num_check(), the password inputted
    checkTo = num_check(password)
    if checkTo == str(checkDigits):
        verif = True
    else:
        verif = False
    return (verif)


def initialise():  # sets up the program when running for the first time
    file = open("PyPassword.txt", "w")
    while True:
        masterKey = input("Please set a master password:")
        masterKeyCheck = input("Please repeat for security:")
        if masterKey == masterKeyCheck:
            break
    numCheckDigit = num_check(masterKey)
    masterKey = ""     #makes it harder to view master key once program run
    file.write(str(str(numCheckDigit) + "\nwebsite:username:encryptedpassword\n"))
    file.close()
    print("Program Initialised successfully")

def gen_password(length):
    import random
    character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5']
    password = ""
    for i in range(length):
        secure_random = random.SystemRandom()
        password = password + str(secure_random.choice(character))
    return (password)


def encrypt(key, plainText):  # encrypts password with a virgenre square cipher
    cipherText = ""
    for i in range(len(plainText)):
        keyLetter = key[i]
        plainTextLetter = plainText[i]
        keyNum = ord(keyLetter)
        plainTextNum = ord(plainTextLetter)
        cipherNum = keyNum + plainTextNum
        if cipherNum >= 200:
            cipherNum = cipherNum - 200
        cipherText = cipherText + chr(cipherNum)
    return (cipherText)

def recursive_check(site,username): #some passwords can't be encrypted-finds one that can
    file = open("PyPassword.txt", "r+")  # generates and encrypts a password
    timeDelays = [0, 0, 5, 15, 60, 120, 300, 1200, 12000, 120000]  # time delay if wrong key entered
    timeDelay = 0
    import time
    while True:
        masterKey = input("Please enter the master password:")
        checkDigits = file.readline(3)  # gets check digits
        print(checkDigits)
        matching = num_verif(checkDigits, masterKey)
        if matching == True:
            break
        else:
            print("Incorrect Password")
            if timeDelays[timeDelay] != 0:
                print("Locked for ", timeDelays[timeDelay], " seconds.")
            time.sleep(timeDelays[timeDelay])
            timeDelay = timeDelay + 1
    print("Generating Password. Standby...")
    while True:
        try:
            print("...")
            password = gen_password(len(masterKey))
            encryptedPassword = encrypt(masterKey, password)
            file.close()
            textToAdd = str(str(site) + ":" + str(username) + ":" + str(encryptedPassword) + "\n")
            file = open("PyPassword.txt", "a")
            file.write(textToAdd)
            file.close()
            break
        except:
            pass
    print("Saving Password...")
    print("Your password is:", password)

def add_password(site, username):  # adds a new password
    recursive_check(site,username)
    print("Password Saved successfully (USE LAST PRINTED PASSWORD)")


def get_username(site):  # gets a username
    file = open("PyPassword.txt", "r")
    line = file.readline()
    for i in range(1000):  # gets each line, one by one
        line = file.readline()
        try:
            splitLine=re.split(r":",line)
            if splitLine[0]==site:
                return(splitLine[1])
        except:
            pass
def get_password(site):  # gets a password
    file = open("PyPassword.txt", "r")
    line = file.readline()
    for i in range(1000):  # gets each line, one by one
        line = file.readline()
        try:
            splitLine = re.split(r":", line)
            if splitLine[0] == site:
                encryptedPassword=splitLine[2]
                masterKey=input("Please enter your master key to proceed")
                decrypt=""
                for i in range((len(encryptedPassword))):
                    keyLetter = masterKey[i]
                    cipherTextLetter = encryptedPassword[i]
                    keyNum = ord(keyLetter)
                    cipherTextNum = ord(cipherTextLetter)
                    cipherNum = cipherTextNum-keyNum
                    if cipherNum<=0:
                        cipherNum=cipherNum+200
                    decrypt=decrypt+chr(cipherNum)
                    if len(encryptedPassword)-2 == i:
                        return(decrypt)
        except:
            pass

def main():
    while True:
        print("""
0. Initialise Program
1. Add a new site
2. Get a username
3. Get a password
4. Instructions 2&3
5. Quit""")
        choice=input("Please enter your choice of function:")
        if choice=="0":
            initialise()
        elif choice=="1":
            site=input("Please enter the site (URL after http://www.) for which this password is for:")
            user=input("Please enter your logon username or email for this site:")
            add_password(site,user)
        elif choice=="2":
            site = input("Please enter the site for which you want your username for:")
            print("Your username is: ",get_username(site))
            webbrowser.open_new(str("http://www."+str(site)))
        elif choice=="3":
            site=input("Please enter the site for which this password is for:")
            print("Your password is: ",get_password(site))
            webbrowser.open_new(str("http://www." + str(site)))
        elif choice=="4":
            site=input("Please enter the site you wish to access:")
            print("Your username is: ", get_username(site))
            print("Your password is: ",get_password(site))
            webbrowser.open_new(str("http://www." + str(site)))
        elif choice=="5":
            break
main()
