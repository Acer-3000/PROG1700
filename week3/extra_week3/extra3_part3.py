raining = input("Is it raining? (yes/no): ")
cold = input("Is it cold outside? (yes/no): ")
windy = input("Is it windy? (yes/no): ")
stay_inside = (raining == "yes" and cold == "yes" and windy == "yes")

if stay_inside:
    print("Stay Inside!")
elif raining == "yes" and cold == "yes":
    print("Wear a raincoat and warm clothes.")
elif raining == "yes" and cold == "no":
    print("Take an umbrella.")
elif raining == "no" and cold == "yes":
    print("Wear a jacket.")
elif windy == "yes":
    print("It's windy outside.")
else:
    print("Enjoy the nice weather!")