from cgitb import text
from tkinter import *
from tkinter import font
root=Tk()
root.title('TIC TAC TOE GAME')
root.resizable(0,0)
Label(root,text="player 1 : X",font="Calibri 15 bold").grid(row=0,column=1)
Label(root,text="player 2 : O",font="Calibri 15 bold").grid(row=0,column=2)

panels=['panel']*10
print(panels)

def win(panels,sign):
    return ((panels[1]==panels[2]==panels[3]==sign)
    or(panels[1]==panels[4]==panels[7])
    or(panels[1]==panels[5]==panels[9])
    or(panels[2]==panels[5]==panels[8])
    or(panels[3]==panels[6]==panels[9])
    or(panels[3]==panels[5]==panels[7])
    or(panels[4]==panels[5]==panels[6])
    or(panels[7]==panels[8]==panels[9])) 
button1=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=1,column=1)
button2=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=1,column=2)
button3=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=1,column=3)
button4=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=2,column=1)
button5=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=2,column=2)
button6=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=2,column=3)
button7=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=3,column=1)
button8=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=3,column=2)
button9=Button(root,width=10,height=5,font="Calibri 15 bold").grid(row=3,column=3)
root.mainloop()
