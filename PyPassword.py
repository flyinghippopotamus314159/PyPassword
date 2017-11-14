def num_check(password):
  passNum=""
  for i in range(len(password)):
    passNum=passNum+str(ord(password[i]))
  passNumTwo=passNum
  divNum=passNum[3:]
  endThree=passNumTwo[:3]
  divNumber=int(divNum)
  print(divNumber)
  endNumber=int(endThree)
  print(endNumber)
  storePass=divNumber%endNumber
  storeString=str(storePass)
  for i in range(3-len(storeString)):
    storeString="0"+storeString
  return(storeString)
