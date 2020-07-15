q=1
Bank_Account={
    'Account Number':12345678,
    'PIN':7777
}
BALANCE= 100000  
ACCOUNTS= ["Priyangi","Neville","Niksh","Rushil","Sathvik","Advaith"]
ACCOUNTNumber= int(input("Enter the account number:"))
if ACCOUNTNumber==Bank_Account['Account Number']:
  PinNumber= int(input("Enter the pin:"))
  if PinNumber==Bank_Account['PIN']:                       
    print("The current balance is Rs.",BALANCE)
    while q==1:
     print(" CURRENT BALANCE-0   WITHDRAWAL-1    DEPOSIT- 2   TRANSFER- 3    EXIT - 4   ")
     Transaction = int(input("Select your choice: "))
     if Transaction==1:
      WD= int(input("Enter the money you want to collect:"))
      if BALANCE>WD:
        BALANCE= BALANCE-WD
        print("The balance is Rs.",BALANCE)
      else:
        print("Not enough money")
     elif Transaction==2:
      DT= int(input("Enter the money you want to deposit:"))
      BALANCE= BALANCE+DT
      print("The balance is Rs.",BALANCE)
     if Transaction==3:
      print("Accounts Available:")
      print("Priyangi")
      print("Neville")
      print("Rushil")
      print("Sathvik")
      print("Advaith")
      transfer_account= str(input("Enter the account:"))
      if transfer_account=="Priyangi":
         Transfer= int(input("Enter the amount you want to tranfer: "))
         if Transfer<=BALANCE:
          BALANCE= BALANCE-Transfer
          print("Transfer SUCESSFUL!!")
         else:
           print("Not possible") 
      if transfer_account=="Neville":
         Transfer= int(input("Enter the amount you want to tranfer: "))
         if Transfer<=BALANCE:
          BALANCE= BALANCE-Transfer
          print("Transfer SUCESSFUL!!")
         else:
           print("Not possible") 
      if transfer_account=="Niksh":
         Transfer= int(input("Enter the amount you want to tranfer: "))
         if Transfer<=BALANCE:
          BALANCE= BALANCE-Transfer
          print("Transfer SUCESSFUL!!")
         else:
           print("Not possible")         
      if transfer_account=="Rushil":
         Transfer= int(input("Enter the amount you want to tranfer: "))
         if Transfer<=BALANCE:
          BALANCE= BALANCE-Transfer
          print("Transfer SUCESSFUL!!")
         else:
           print("Not possible")  
      if transfer_account=="Rushil":
         Transfer= int(input("Enter the amount you want to tranfer: "))
         if Transfer<=BALANCE:
          BALANCE= BALANCE-Transfer
          print("Transfer SUCESSFUL!!")
         else:
           print("Not possible")
      if transfer_account=="Priyangi":
         Transfer= int(input("Enter the amount you want to tranfer: "))
         if Transfer<=BALANCE:
          BALANCE= BALANCE-Transfer
          print("Transfer SUCESSFUL!!")
         else:
           print("Not possible")  
     if Transaction==0:
       print("The balance is",BALANCE) 
     if Transaction==4:
      print("THANK YOU !!")
      break
  else:
    print("INCORRECT PIN")
else:
  print("ACCOUNT DOESNT EXIST")