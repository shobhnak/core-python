list1 = [1,10,20]
print(list1)
#print(id(list1))
list1.append("shobhna")
print(list1)
#print(id(list1))
list1[0]=100
print(list1)

for item in list:
    print(item)
    if item == "shobhna":
        print(f"{item}exit in list") 
        
for index, item in enumerate(list1):
 print(f"{item * index} is at index {index}")
 