temp = float(input("Enter the temperature (°C):"))
raining = input("is it raining y/n")

if temp < 0 and raining == "y":
    print("Warning: Extreme temperature!")
else:
    print("Temperature is normal.")