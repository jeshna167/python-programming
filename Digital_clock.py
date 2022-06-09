from time import strftime
#t=strftime("%H %M  %S  %p (am, pm)  %a (weekday) %b (month) %Y (year)  %X (all)")
#print(t)
from tkinter import *
root=Tk()
root.title("Digital Clock")
root.geometry("800x800+50+50")
root.resizable(0,0)
def clock():
    # tick=strftime("%H:%M:%S %p %a %b %Y")
    tick=strftime("%H:%M:%S %p %A %B %d, %Y")
    label1.config(text=tick)
    label1.after(1000,clock)
label=Label(root,font=("arial",50),background="blue",text="time",foreground="white")
label.pack()
label1=Label(root,font=("arial",30),background="pink",foreground="black")
label1.pack()
clock()
root.mainloop()