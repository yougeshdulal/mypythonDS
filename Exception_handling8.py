# name = input("enter name: ")
# print(name)

#file handling.................................
#read,write,append
#steps:- open,do ,close

# f = open("test.txt", 'a')
#
# f.close()



#exception handling.............................
# try:
#     a = [11, 22, 45]
#     print(a[5])
# except Exception as z:
#     print(f"there is error {z}")
# else:
#     print("we have no problem")
# finally:
#     print("this is try except block")
#
#
#
# print("this is demo")


#.............................................................
# try:
#     f = open("text1.txt", 'r')
#     data = f.read()
#     print(data)
#     print("inside file")
#     f.close()
# except Exception as xe:
#     print(f"the error is {xe}")
# else:
#     print("inside file::")
# print("this is remaining works!")


#............................................................

# try:
#     f = open("test.txt",'r')
# except Exception as xe:
#     print(xe)
# else:
#     f.close()
# finally:
#     print("this is file")
#
# print("test")

#.june6.......................................................

# try:
#     f_age = 22
#     s_age = 33
#     if f_age < s_age:
#         raise Exception("check bau xora ko age???")
#
# except Exception as ex:
#     print(ex)
# else:
#     print(f"father age is {f_age} and sons age is {s_age}")
# finally:
#     print("age handler block you")
# print("test")


#..file.................................................
#read r,write w,append a,create x


# f = open('text.txt')
# data = f.read()
# print(data)
# print("now need to print again")
# f.close()
#
# f1 = open("text.txt", 'a')
# data = f1.write("\n some test contains")
#
#
# f2 = open("text.txt")
# f2.read()
# print(data)


#......................................................
import csv
import numpy as np

# with open("details.csv") as f:
#     data = csv.reader(f)
#     print(data)
#     for i in data:
#         print(i[0])
#
# with open("details.csv") as f:
#     wr = csv.writer(f)
#     print(wr)


a = np.array([1, 2, 3, 4, 5, 6])
print(a)














