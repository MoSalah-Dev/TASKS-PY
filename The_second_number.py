numop = int(input("Enter the num : "))

list1 = []

for i in range (0,numop) :
    ad = int(input("Enter the numbers : "))

    list1.append(ad)
    
list1.remove(max(list1))

print("the second max number in the list = ",max(list1))
