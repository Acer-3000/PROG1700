print("What size pizza?")
order = input("small, meduim, large")
if order == "small":
    print("Extra cheese")
    cheese = input("y/n")
    if "y":
        print("Total is $10")
    else:
        print("Total is $8")
    
    
if order == "meduim":
    print("$10")
if order == "large":
    print("$12")
