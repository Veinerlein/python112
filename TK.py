# from tkinter import *
# from tkinter import ttk
# import time
#
# def click():
#     print("Click")
#
# def check_time():
#     btn["text"]=time.strftime("%H:%M:%S") # поточний час у форматі
#
# clicks=0
# def counter():
#     global clicks
#     clicks+=1
#     btn2["text"]=f"counter {clicks}"
#     root.title(f"Назва Вікна {clicks}")
#
# root = Tk()
# root.title("Назва Вікна")
# # root.iconbitmap("посилання на фконку")
# root.geometry("300x300+300+300")
# btn = Button(root,text="Check time", command=check_time)
# btn.pack()
#
# btn2 = Button(root,command=counter, text=f"counter {clicks}")
# btn2.pack()
#
# root.mainloop()

# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.geometry("300x300+300+300")
# root.resizable(False,False)
#
# l = Label(root,anchor=W,width=40,fg="#fff",bg="red",justify=LEFT,font=('Comic Sans MS',10,'bold'),text="Text in string "
#                                                                                                   "line 1 \nText 2 "
#                                                                                   "\nText " \
#                                                                             "3\nText 4 "
#                                                                 "\nText 5 \nText6")
# l.pack()
# img=PhotoImage(file=r"F:\1програмування\Woman_about_python\html\Verstka\my World.png")
# l_logo = Label(root, image=img, pady=110,padx=10)
# l_logo.pack()
#
# """На відміну від CSS тут нижній код іде на низ, а не
# накладається на верх"""
#
#
#
# root.mainloop()

# Entry
from tkinter import *

root = Tk()
root.geometry("300x300+300+300")

def add_str():
    e.insert(END,'Hello')

def del_str():
    e.delete(0,END)

def get_str():
    l2["text"]=e.get()

l = Label(root, text="Pole entry")
l.pack()
e = Entry(root, show="*")
e.insert(0,"World ")
e.insert(END,"Hello")
e.pack()

btn_add = Button(root, text="AddSTR", command=add_str)
btn_del = Button(root, text="DELstr", command=del_str)
btn_get = Button(root, text="GetStr", command=get_str)

btn_add.pack()
btn_del.pack()
btn_get.pack()

l2 = Label(root, background="blue", fg="#999")
l2.pack(fill=X)


root.mainloop()




