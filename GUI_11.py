import csv
import tkinter as tk

def submit_handler():
    name = e1.get()
    age = e2.get()
    mark = e3.get()
    address = e4.get()
    std2 = [name,age,mark,address]
    print(f"Name:{name},Age:{age},Mark:{mark},Address:{address}")
    with open("std2.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(std2)


def gen_handler():
    if gender1.get() == 1:
        print("male clicked")
    elif gender1.get() == 2:
            print("female clicked")
    else:
        print("others clicked")

def gender_handler():
    global r1,r2,r3
    r1 = tk.Radiobutton(master, text="male", variable=gender1, value=1, command=gen_handler).grid(row=4,column=1)
    r2 = tk.Radiobutton(master, text="female", variable=gender1, value=2, command=gen_handler).grid(row=5,column=1)
    r3 = tk.Radiobutton(master, text="others", variable=gender1, value=3, command=gen_handler).grid(row=6,column=1)










master = tk.Tk()

master.geometry('700x250')
master.title("Student Detail Handler")
tk.Label(master,text="Name: ", fg='red', font=('Ariel', 15, 'bold')).grid(row=0, column=0)
tk.Label(master,text="Age: ", fg='red', font=('Ariel', 15, 'bold')).grid(row=1, column=0)
tk.Label(master,text="Mark: ", fg='red', font=('Ariel', 15, 'bold')).grid(row=2, column=0)
tk.Label(master,text="Address: ", fg='red', font=('Ariel', 15, 'bold')).grid(row=3, column=0)
tk.Label(master,text="Gender: ", fg='red', font=('Ariel', 15, 'bold')).grid(row=4, column=0)

global gender1

gender1 = tk.IntVar(master)


e1 = tk.Entry(font=('Ariel', 15, 'bold'))
e1.grid(row=0,column=1)
e2 = tk.Entry(font=('Ariel', 15, 'bold'))
e2.grid(row=1,column=1)
e3 = tk.Entry(font=('Ariel', 15, 'bold'))
e3.grid(row=2,column=1)
e4 = tk.Entry(font=('Ariel', 15, 'bold'))
e4.grid(row=3,column=1)
gender_handler()

btn1 = tk.Button(master,text="SUBMIT",command=submit_handler).grid(row=7,column=1)
btn2 = tk.Button(master,text="CANCEL",command=master.destroy).grid(row=7,column=2)



master.mainloop()

#..............................................................
import tkinter
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageOps
master = tk.Tk()

master.geometry('900x350')
master.title("SPIDER MAN")
master.config(bg="Black")
master.iconphoto(False, tk.PhotoImage(file='imgpng1.png'))

image = Image.open("img11.png")
# image = image.filter(ImageFilter.SHARPEN)
image = ImageOps.grayscale(image)


canvas = tk.Canvas(master, height=300, width=300, bg='skyblue')
canvas.pack()

left_frame = tk.Frame(master, height=200, width=200, bg='white')
left_frame.pack(side='left', fill='y')


btn1 = tkinter.Button(left_frame,text="click me")
btn1.pack(pady='25')

image = ImageTk.PhotoImage(image)
# canvas.config(height=image.height(),width=image.width())
canvas.create_image(0, 0, image=image, anchor='nw')






master.mainloop()



