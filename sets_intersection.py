op1 = int(input("Enter the op1 : "))
op2 = int(input("Enter the op2 : "))
x = []
for i in range (0,op1):
    list1 = int(input("Enter the list1 : "))
    x.append(list1)

x = set(x)


y = []
for i in range (0,op2):
    list2 = int(input("Enter the list2 : "))
    y.append(list2)

y = set(y)

print(x & y)
