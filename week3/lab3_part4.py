user = input("Enter username: ")
password = input("Enter password: ")

if user == "Admin":
        if password == "1234":
            print("Access granted.")
        else:
            print("Wrong password.")
if user == "student":
        if password == "4321":
            print("Access granted.")
        else:
            print("Wrong password.")
#else:
    #print("Unknown user")
    