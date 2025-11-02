# chak bocx funtion#
from tkinter import*

def x():
    print(var.get())
    
win=Tk()
win.title("this is for chakbox")
win.geometry("600x600")

var=BooleanVar()

cb=Checkbutton(win,text="shop now",bg="green",fg="black",bd="3",relief="groove",variable=var)
cb.pack()

b=Button(win,text="shop now",bg="green",fg="black",bd="3",relief="groove",command=x)
b.pack()

print(var.get())

win.mainloop()