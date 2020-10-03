import tkinter as tk

root= tk.Tk()

root.resizable(0, 0)

root.title("Square root")

canvas1 = tk.Canvas(root, width = 500, height = 400,  relief = 'raised',bg="white")
canvas1.pack()

label1 = tk.Label(root, text='Calculate the Square and square root of number')
label1.config(font=('helvetica', 14),bg="white")
canvas1.create_window(250, 25, window=label1)

label2 = tk.Label(root, text='Enter the Number:')
label2.config(font=('helvetica', 12),bg="white")
canvas1.create_window(130, 100, window=label2)

entry1 = tk.Entry (root, font = ('helvetica', 12, 'bold'), borderwidth=2) 
canvas1.create_window(330, 100, window=entry1)


def getSquareRoot ():
    
    x1 = entry1.get()
    
    label3 = tk.Label(root, text= 'The Square Root of ' + x1 + ' is:',font=('helvetica', 14),bg="white")
    canvas1.create_window(190, 250, window=label3)
    
    label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 14, 'bold'),bg="white")
    canvas1.create_window(350, 250, window=label4)
    
def getSquare ():
    
    x1 = entry1.get()
    
    label5 = tk.Label(root, text= 'The Square of ' + x1 + ' is:',font=('helvetica', 14),bg="white")
    canvas1.create_window(180, 300, window=label5)
    
    label6 = tk.Label(root, text= float(x1)**2,font=('helvetica', 14, 'bold'),bg="white")
    canvas1.create_window(350, 300, window=label6)
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot, bg='black', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(150, 180, window=button1)

button2 = tk.Button(text='Get the Square', command=getSquare, bg='black', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(350, 180, window=button2)

root.mainloop()
