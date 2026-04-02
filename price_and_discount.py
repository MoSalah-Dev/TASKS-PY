price = float(input("Enter the price : "))
discount = float(input("Enter the discount : "))

fin = (discount*price) / 100
pr = price - fin

print("the price after discount = ",pr)
