pin = input("Enter PIN: ")

while pin == "4321":
    option = input("Choose (balance/withdraw/): ")
    if option == "balance":
        print("Your balance is $500")
    elif option == "withdraw":
        amount = int(input("Enter amount: "))
        if amount <= 500:
            print("Withdrawal successful")
        else:
            print("Insufficient funds")
    else:
        print("Invalid option")
else:
    print("Wrong PIN")
    
