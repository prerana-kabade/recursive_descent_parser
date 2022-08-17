from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from recpar import par 
root1=Tk()
root1.geometry('1000x720+250+50')
root1.resizable(0,0)
bgg=ImageTk.PhotoImage(file="images\parsu2.jpeg")
myc1=Canvas(root1,width=1000,height=720,bd=0,highlightthickness=0)
myc1.pack(fill='both',expand=True)
myc1.create_image(0,0,image=bgg,anchor="nw")
myc1.create_text(200,20,text="Recursive-Descent Parser",anchor="nw",font="times 40 bold underline",fill="black")
myc1.create_text(350,120,text="Grammer :",anchor="nw",font="times 30 bold underline",fill="black")
myc1.create_text(400,180,text="E->TE'\nE'->+TE'/@\nT->FT'\nT'->*FT'/@\nF->(E)/i\n",anchor="nw",font="times 25 bold",fill="black")
em=Entry(myc1,font="times 20 bold",fg="grey",width=25)
em.place(x=300,y=420)
em.insert(0,"Enter the String")
v=myc1.create_text(370,500,text="",anchor="nw",font="times 25 bold")

def exp(e):
    if(em.get()=="Enter the String"):
        em.delete(0,END)
        em.configure(fg="black")
em.bind("<Button-1>",exp)
def parsefun():
    a=em.get()
    s=par(a)
    if(s):
        myc1.itemconfigure(v,text="String is Accepted",fill="#80ff80")
    else:
        myc1.itemconfigure(v,text="String is not Accepted",fill="red")
submit=Button(myc1,text="Submit",bg="black",fg="white",height=0,width=7,font="times 13 bold",command=parsefun)
submit.place(x=665,y=420)
root1.mainloop()