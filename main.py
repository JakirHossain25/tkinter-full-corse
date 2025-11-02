# this is for buton#
from tkinter import*
win=Tk()
win.title("this is for button")
win.geometry("600x600")

bt=Button(win,text="shop now",bg="green",fg="white",bd="3",relief="groove")
bt.place(x=100,y=100,width=100,height=50)


win.mainloop()