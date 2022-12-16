print("Welcome to SBI \n Insert your card")
username = "Amulya"
password = 1234
Balance = 50000
pin = int(input("Enter Pin: "))
if pin == password:
    print(""" 1. Deposit
              2. Withdrawl
              3. Balance
              4. mini_statement """)
    option = int(input("Enter Option: "))
    if option == 1:
        Deposit = int(input("Enter Amount: "))
        Balance+=Deposit
        print(Balance)
    elif option == 2:
        Withdrawl = int(input("Enter Amount: "))
        Balance-=Withdrawl
        print(Balance)
    elif option == 3:
        print("Total Balance : ",Balance)
    elif option == 4:
        print("******ATM******")
        print(username)
        print(Balance)
        print("THANK YOU \n VISIT AGAIN")
else:
    print("Enter Correct Pin")