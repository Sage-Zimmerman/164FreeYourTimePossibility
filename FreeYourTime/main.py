from atexit import register
from tkinter import *

screen = Tk()
screen.geometry("600x470")
screen.title("Add Card")
screen.resizable(False, False)

def add_card():
    print("Card Added")

Label(screen, text="Change For the Future!", font="arial 25").pack(pady=50)

Label(text="Card Type",font=23).place(x=100,y=150)
Label(text="Card Number",font=23).place(x=100,y=200)
Label(text="Security Code",font=23).place(x=100,y=250)
Label(text="Expiration Date",font=23).place(x=100,y=300)

typeVaule=StringVar()
numberVaule=StringVar()
codeVaule=StringVar()
dateVaule=StringVar()

typeEntry = Entry(screen, textvariable=typeVaule, width=30, bd=2, font=20)
numberEntry = Entry(screen, textvariable=numberVaule, width=30, bd=2, font=20)
codeEntry = Entry(screen, textvariable=codeVaule, width=30, bd=2, font=20)
dateEntry = Entry(screen, textvariable=dateVaule, width=30, bd=2, font=20)

typeEntry.place(x=200,y=150)
numberEntry.place(x=200,y=200)
codeEntry.place(x=200,y=250)
dateEntry.place(x=200,y=300)


#check if a robot (not very inteligent system for now, I know.)
checkValue=IntVar
checkbtn=Checkbutton(text="I am not a robot", variable=checkValue)
checkbtn.place(x=200, y=340)


Button(text="Add Card", font=20, width=11, height=2, command=add_card).place(x=250,y=380)


screen.mainloop()