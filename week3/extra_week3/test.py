pin = input('Enter PIN ')
if pin == "4321" or input("Wrong PIN    Enter PIN ") == "4321":
    options = input("Balance, Withdraw, Deposit: ")
    if options == "Balance":
        print("Your balance is $500")
    if options == "Withdraw":
        amount = int(input("Enter amount to withdraw: "))
        if amount > 500:
            print("Insufficient funds")
        else:
            print(f"You have withdrawn ${amount}")
            print(f"Your new balance is ${500 - amount}")
    if options == "Deposit":
         amount = int(input("Enter amount to deposit: "))
         print(f"You have deposited ${amount}")
         print(f"Your new balance is ${500 + amount}")
else:
    print("Locked out")