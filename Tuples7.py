# import june4function as j
#
# j.add()
#
# from june4function import add
# add()

import math

#...............................................................
# s1 = 'math'
# s2 = 'science'
# s3 = 'english'
#
# n1 = float(input(f"enter the marks of {s1}:"))
# n2 = float(input(f"enter the mark of {s2}:"))
# n3 = float(input(f"enter the mark of {s3}:"))
#
# total = n1+n2+n3
# per = total/3
# per = per.__round__(2)
#
# print("total is:", total)
# print("percentage is:", per)

#............................................................

# print(2+3)
# print(2+3)
# print(2 ** 4)
#
# print(pow(2, 3))
#
# print(math.ceil(3.1))
# print(math.floor(2.9))

#...........................................................

# l1 = [["ram", 22, 77.5], ["shyam", 25, 88], ["hari", 30, 90]]
#
# print(l1)
# print(len(l1))
#
# l1.append(["sita", 22, 65])
# print(l1)

#tuple............................................................
#tuples are immutable.
#list inside tuple supports immutable.

# t1 = (["sunday", "monday", "tuesday"], "wednesday", "sunday")
# print(t1)
#
# t1[0][1] = "mango"
# print(t1)

#...............................................................

t1 = [["ram", 22, 77],["shyam", 26, 80],["hari", 30, 90]]

print(t1)
t1.append(["sita", 19, 50])
print(t1)

l1 = []
n = int(input("enter the number:"))


for i in range(n):
    new = []
    name = input("enter the name:")
    age = int(input("enter the age:"))
    mark = float(input("enter the mark:"))
    new.append(name)
    new.append(age)
    new.append(mark)
    l1.append(new)

print(l1)



#...............................................................





