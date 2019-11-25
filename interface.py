from tkinter import *
import sqlite3
import tkinter.messagebox

root1 = Tk()


def newwindow():
    root = Tk()
    root.title("GUI Example")
    root.geometry('300x100')
    def buttonPushed():

        if label1['text'] == "Text A":
            label1['text'] = "Text B"
        else:
            label1['text'] = "Text A"
    myButton1 = Button(root, text="Change", command=buttonPushed)
    myButton1.pack(side=BOTTOM)
    label1 = Label(root, text="Text A")
    label1.pack(side=BOTTOM)



def exit():
    sys.exit()



root1.title("Login")
root1.geometry("400x500")


def login():
    db = sqlite3.connect('database.db')
    user = entry1.get()
    passwd= entry2.get()

    result = db.execute('SELECT * FROM Login WHERE USERNAME = ? AND PASSWORD = ?', (user, passwd))


    if (result.fetchall()):
        tkinter.messagebox.showinfo(title="Great", message="Valid User")
        newwindow()
        root1.destroy()

    else:
        tkinter.messagebox.showinfo(title="Login Failed", message="Invalid User")




lbl1 = Label(root1, text="Username")
lbl1.place(x=100, y=200, width=100, height=30)

lbl2 = Label(root1, text="Password")
lbl2.place(x=100, y=250, width=100, height=30)

entry1 = Entry(root1)
entry1.place(x=200, y=200, width=100, height=30)

entry2 = Entry(root1, show="*")
entry2.place(x=200, y=250, width=100, height=30)

btn1=Button(root1,text="Login", command= login)
btn1.place(x=100, y=300, width=100, height=30)

btn2=Button(root1,text="Exit", command=exit)
btn2.place(x=250, y=300, width=100, height=30)


root1.mainloop()