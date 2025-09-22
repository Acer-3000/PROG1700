pin = input("Enter PIN: ") 
pin = True if pin == "4321" else False
if False 


if True:
    options = input("Balance, Withdraw, Deposit: ")
    if options == "Balance":
        print("Your balance is $500")
    elif options == "Withdraw":
        amount = int(input("Enter amount to withdraw: "))
        if amount > 500:
            print("Insufficient funds")
        else:
            print(f"You have withdrawn ${amount}")
            print(f"Your new balance is ${500 - amount}")





