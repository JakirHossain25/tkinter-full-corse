# label frame widget #
from tkinter import*
win=Tk()
win.title("label frame windget")
win.geometry("450x450")
win.config(bg='green')

label=LabelFrame(win,text="label frame",bg="green",font=(5),labelanchor=N)
label.place(x=100,y=100,width=300,height=100)



win.mainloop()


