num = int(input(("Enter the num of op : ")))
money = float(input(("Enter your money : ")))

for i in range(0,num):
    op = float(input("Enter the op : "))
    money+=op 

print("your money is : ",money)
