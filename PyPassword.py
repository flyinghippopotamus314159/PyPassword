def num_check(password):
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
def num_verif(checkDigits,password):
  checkTo=num_check(password)
  if checkTo==str(checkDigits):
    verif=True
  else:
    verif=False
  return(verif)
