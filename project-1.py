import random
import string
from tkinter import *

def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(length))
    return result_str

window=Tk()
window.title("**PASSWORD GENERATOR APP**")
window.geometry('500x200')
l=Label(window,text="\t\twelcome to password generator done by python\n\t\tEnter the Size Of Password : ")
l.grid(column=0,row=0)
txt=Entry(window,width=4)
txt.grid(column=0,row=1)
def clicked():
    l.configure(text=f"\tButton was clicked !!\n\t\tyour generated password is : {get_random_string(int(txt.get()))}\n\t\tEnter the Size of Password :")
btn = Button(window, text="GENERATE", command=clicked)
btn.grid(column=0, row=2)
window.mainloop()