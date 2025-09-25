pin = input("Enter PIN ") == "4321"
if not pin:
    print("Wrong PIN")
    pin = input("Enter PIN ") == "4321" 
if pin: 
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
if options == "Deposit":
    amount = (input("Enter amount to Deposit: "))
    print(f"You have Deposited ${amount}")
    print(f"Your new balance is ${500 + amount}")