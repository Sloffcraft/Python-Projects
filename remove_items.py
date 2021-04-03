#removing duplicated value 

num = [3,4,2,3,2,6,2,3,3]

while num.count(3) > 1 or num.count(2) > 1:
    num.remove(3)
    num.remove(2)
print(num)