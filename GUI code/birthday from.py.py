from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("birthday wish app")


Fullname=StringVar()
Email=StringVar()
Birthdate=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   birthdate=Birthdate.get()
   conn = sqlite3.connect('birth.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Birthdate TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Birthdate) VALUES(?,?,?)',(name1,email,birthdate))
   conn.commit()
   
   
             
label_0 = Label(root, text=" Birthday Wish App",width=20,bg='yellow',fg='black',font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Birthdate",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root,textvar=Birthdate)
entry_3.place(x=240,y=230)


Button(root, text='Done',width=20,bg='green',fg='black',command=database).place(x=180,y=380)

root.mainloop()

