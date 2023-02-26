import tkinter as tk
import random
master=tk.Tk()
tk.Label(master,text="First Name").grid(row=0)
tk.Label(master,text="Last Name").grid(row=1)

e1=tk.Entry(master)
e2=tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
nome=e1.get()
sobrenome=e2.get()
print(sobrenome)
master.mainloop()
