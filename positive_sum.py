op = int(input("Enter the size of the list: "))
li = []

for i in range(op):
    num = int(input(f"Enter number {i+1}: "))
    if num > 0:
        li.append(num) 

print("Sum of positive numbers is:", sum(li))
