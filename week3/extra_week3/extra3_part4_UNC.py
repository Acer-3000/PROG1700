card = input("Insert card (yes): ")
while attempts < 1 and card == 'yes':
    card = input("Insert card (yes): ")
if card == 'yes':
    print("Card accepted")
    
pin = input("Enter PIN: ") 
pin = True if pin == "4321" else False

print("Access granted" if pin else "Wrong PIN")
attempts = 0 
if pin:
    while attempts < 1:
        pin = input("Enter PIN: ") 
    pin = True if pin == "4321" else False
    
    print("Access granted" if pin else "Wrong PIN")
    attempts += 1
if pin == True:
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