from tkinter import *
from tkinter import ttk #theme
from tkinter import messagebox

GUI = Tk()
GUI.title('Knowledge Notions')
GUI.geometry('800x600')

B1 = ttk.Button(GUI, text='Balance')
B1.pack(ipadx=10,ipady=10)

def Button2():
    text = 'Your Account has money 300 Baht.'
    messagebox.showinfo('Account Balance', text)

FB1 = Frame(GUI)
FB1.place(x=100, y=100)
B2 = ttk.Button(FB1, text='Balance', command=Button2)
B2.pack(ipadx=10,ipady=10)


GUI.mainloop()