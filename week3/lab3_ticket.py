age = int(input("Age in years ")) 
student = (input("Are you Student? (y/n) "))

if age < 5:
    print("Free Ticket")
elif age >= 5 and age <= 12:
     if student == "y":
        print("Fee is $6")
     else:
        print("Fee is $8")
elif age >= 13 and age <= 64:
     if student == "y":
        print("Fee is $10")
     else:
        print("Fee is $12")
else: 
    age >= 65
    print("Fee is $6")
