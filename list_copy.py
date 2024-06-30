#shalow copy
import
l1=[1,2,3,4]
l2=l1
print(l1)
print(l2)
l2.append(4)
print(l2)
print("************",l1)

#deep copy
l3 = copy.deepcopy(l1)

