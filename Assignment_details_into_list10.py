import csv
import pandas as pd


student_detail = []
def get_details(num1):
    for i in range(num1):
        new_std = []
        name = input("Entrer the name of the students: ")
        age = int(input("Enter the age of the student: "))
        address = input("Enter the address of the student: ")
        mark = float(input("Enter the mark of the student: "))

        new_std.append(name)
        new_std.append(age)
        new_std.append(address)
        new_std.append(mark)
        list_as_string = ",".join(str(item) for item in new_std)
        file = open("std2.csv",'a')
        file.write(list_as_string)
        file.write("\n")
        file.close()
        student_detail.append(new_std)
    print(student_detail)


def info_display():
    with open('std2.csv','r') as f:
        data = csv.reader(f)
        for i in data:
            print(i)

user_choice = input("Enter\nread for viewing data\nwrite for entering data:\nvisualize for data visualization\n")
match user_choice:
    case 'read':
        info_display()
    case 'write':
        while j <= 5:
            try:
                n = int(input("Enter the total number of students: "))
                get_details(n)
                break
            except Exception as ex:
                j+=1
                print(ex.__doc__)
                if j == 5:
                    print("You are not sharp minded sorry!")
                if j == 6:
                    print("Ab kehi hudaina!")
    case 'visualize':
        info_display()
    case _:
        print("Invalid")