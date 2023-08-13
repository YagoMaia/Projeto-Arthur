from tkinter import *

root = Tk()

class MyLabel(Frame):
  def __init__(self, master, name, percentage, domain):
    Frame.__init__(self, master, bd=2, relief='raised')
    Label(self, text='%3d%%'%percentage, font=('Arial', 24), fg='#88F', width=4, anchor='e').grid(row=0, column=0, rowspan=2)
    Label(self, text=name, font=('Aria', 16, 'bold'), fg='black', width=15, anchor='w').grid(row=0, column=1)
    Label(self, text=', '.join(domain), font=('Aria', 10), fg='black').grid(row=1, column=1, sticky='w')
    Button(self, text='View', fg='white', bg='#44F').grid(row=0, column=2, rowspan=2, padx=10)
    self.columnconfigure(1, weight=1)

class MyLabel2(Frame):
  def __init__(self, master, name, percentage, domain):
    Frame.__init__(self, master, bd=2, relief='raised')
    Label(self, text='%3d%%'%percentage, font=('Arial', 24), fg='#88F', width=4, anchor='e').grid(row=0, column=0, rowspan=2)
    Label(self, text=name, font=('Aria', 16, 'bold'), fg='black', width=15, anchor='w').grid(row=0, column=1)
    Label(self, text=', '.join(domain), font=('Aria', 10), fg='black').grid(row=1, column=1, sticky='w')
    Button(self, text='View', fg='white', bg='#44F').grid(row=0, column=2, rowspan=2, padx=10)
    self.columnconfigure(1, weight=1)

name = ['vj', 'aj', 'bon', 'hi']
percentage = [96, 85, 90, 65]
domain = [['html','css','js'], ['java','kotlin','python'], ['html','python'], ['java','html','css','js']]

for i, n in enumerate(name):
    print(i, n)

for i, n in enumerate(name):
  MyLabel(root, n, percentage[i], domain[i]).pack(expand=True, fill='x')

for i, n in enumerate(name):
  MyLabel2(root, n, percentage[i], domain[i]).pack(expand=True, fill='x')

root.mainloop()