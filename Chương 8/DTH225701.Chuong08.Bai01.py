from tkinter import *
def tiepAction():
    stringHSA.set(" ")
    stringHSB.set(" ")
    stringKQ.set(" ")

def giaiAction():
    a=float(stringHSA.get)
    b=float(stringHSB.get)
    if a==0 and b == 0:
        stringKQ().set("Vô số nghiệm")
    elif a==0 and b!=0:
        stringKQ().set("Vô nghiệm")
    else: 
        stringKQ().set("x="+str((-b/a)))
    root = Tk()
    stringHSA = stringVar()
    stringHSB = stringVar()
    stringKQ = stringVar()

    root.title("PTB1-facebook.com/duythanhcse")
    root.minsize(height=130,width=250)
    root.resizable(height=True,width=True)

    Label(root,text ="Phuong trinh bac 1",fg="red",font=("tohama",16),justify = CENTER).grid(row=0,columnspan=2)





