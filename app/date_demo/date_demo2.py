

from tkinter import *
from datetime import datetime

root = Tk()
root.title('daily')

root.geometry('400x200')

up_start = datetime(2019, 10, 19)
meet_start = datetime(2020, 11, 15)
entry_start = datetime(2022, 4, 15)
today = datetime.now()


label1 = Label(root, text='五道口纳什', font=('Arial Bold', 30)).grid(row=0, column=0)
label2 = Label(root, text='成为up: {}'.format((today - up_start).days + 1), font=('Arial Bold', 25)).grid(row=1, column=1)
label3 = Label(root, text='相识: {}'.format((today - meet_start).days + 1), font=('Arial Bold', 25)).grid(row=2, column=1)
label4 = Label(root, text='入职: {}'.format((today - entry_start).days + 1), font=('Arial Bold', 25)).grid(row=3, column=1)
root.mainloop()