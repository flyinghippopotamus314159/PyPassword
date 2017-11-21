def num_check(password):                                                                              #creates a three-digit check number by converting the password to a number, finding the modulo in the base of the last three base ten digits of the rest of the number: there are 1000 possible numbers, but it will be the same for any password
  passNum=""
  for i in range(len(password)):
    passNum=passNum+str(ord(password[i]))
  passNumTwo=passNum
  divNum=passNum[3:]
  endThree=passNumTwo[:3]
  divNumber=int(divNum)
  endNumber=int(endThree)
  storePass=divNumber%endNumber
  storeString=str(storePass)
  for i in range(3-len(storeString)):
    storeString="0"+storeString
  return(storeString)
def num_verif(checkDigits,password):                                                                  #verifies, with the check number from num_check(), the password inputted
  checkTo=num_check(password)
  if checkTo==str(checkDigits):
    verif=True
  else:
    verif=False
  return(verif)
def initialise():                                                                                     #sets up the program when running for the first time
  file=open("PyPassword.txt","w")
  while True:
    masterKey=input("Please set a master password:")
    masterKeyCheck=input("Please repeat for security:")
    if masterKey==masterKeyCheck:
      break
  numCheckDigit=num_check(masterKey)
  masterKey=""
  file.write(str(str(numCheckDigit)+"|username:encryptedpassword;username:encryptedpassword"))
  file.close()
def addPassword(site,username,password):                                                            #adds a new password
  file=open("PyPassword.txt","r+")
  masterKey=input("Please enter the master password:")
  
 
