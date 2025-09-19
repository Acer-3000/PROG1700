item1 = input("Enter first item: milk ")
price1 = float(input("Enter price of first item: 1.50 "))

item2 = input("Enter second item: eggs ")
price2 = float(input("Enter price of second item: 2.00 "))

item3 = input("Enter third item: flour ")
price3 = float(input("Enter price of third item: 3.00 "))

total = price1 + price2 + price3

print("----- Receipt -----")
print(item1, ":", price1)
print(item2, ":", price2)
print(item3, ":", price3)
print("Total:", total)