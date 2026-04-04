numop = int(input("Enter the num : "))

list1 = []

for i in range (0,numop) :
    ad = int(input("Enter the numbers : "))

    list1.append(ad)

print("max number in the list = ",max(list1))
print("min number in the list = ",min(list1))
