#!/usr/bin/env python3
__author__ = "Wreck-it Kenny"
__copyright__ = "Copyright 2019, The Python Projects"
__version__ = "1.0.0"
__email__ = "tung.tran.3295@gmail.com"
__status__ = "Production"
__doc__ = "A countdown timer written in Python3"


from tkinter import *
# import Pmw
import winsound

## Callbacks
def limitEntry(*arg):
        E1 = e1.get()
        E2 = e2.get()
        E3 = e3.get()
        if len(E1) > 2: e1.set(E1[:2])
        if len(E2) > 2: e2.set(E2[:2])
        if len(E3) > 2: e3.set(E3[:2])


## Objects
global count
count = 0
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("pyCountDown")
        self.master.geometry("320x180")
        self.master.resizable(False, False)
        self.master.iconbitmap(r'C:\\Program Files\\pyCountDown\\icon.ico')
        self.showTime()

    def showTime(self):
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.master, textvariable=self.t)
        self.lb.config(font=("Courier 40 bold"))                
        self.lb.place(x=30, y=8)

        # self.c1 = Pmw.Counter(self.master, labelpos=W, label_text='Hour:', 
        #                       orient=HORIZONTAL, entry_width=2, entryfield_value=0,
        #                       entryfield_validate={'validator' : 'integer', 'min' : 0, 'max' : 23})
        # self.c1.place(x=57, y=80)

        # self.c2 = Pmw.Counter(self.master, labelpos=W, label_text='Minute:', 
        #                       orient=HORIZONTAL, entry_width=2, entryfield_value=0,
        #                       entryfield_validate={'validator' : 'integer', 'min' : 0, 'max' : 59})
        # self.c2.place(x=46, y=110)

        # self.c3 = Pmw.Counter(self.master, labelpos=W, label_text='Second:', 
        #                       orient=HORIZONTAL, entry_width=2, entryfield_value=0,
        #                       entryfield_validate={'validator' : 'integer', 'min' : 0, 'max' : 59})
        # self.c3.place(x=45, y=140)
        global e1, e2, e3
        e1 = StringVar()
        e2 = StringVar()
        e3 = StringVar()
        e1.trace('w', limitEntry)
        e2.trace('w', limitEntry)
        e3.trace('w', limitEntry)

        Label(self.master, text='Hour: ', font=("Courier 10 bold")).place(x=55, y=80)
        self.e1 = Entry(self.master, width=5, justify=CENTER, relief=RIDGE, borderwidth=2, textvariable=e1)
        self.e1.insert(0, '0')
        self.e1.place(x=100, y=80)
        Label(self.master, text='Minute: ', font=("Courier 10 bold")).place(x=40, y=110)
        self.e2 = Entry(self.master, width=5, justify=CENTER, relief=RIDGE, borderwidth=2, textvariable=e2)
        self.e2.insert(0, '0')
        self.e2.place(x=100, y=110)
        Label(self.master, text='Second: ', font=("Courier 10 bold")).place(x=40, y=140)
        self.e3 = Entry(self.master, width=5, justify=CENTER, relief=RIDGE, borderwidth=2, textvariable=e3)
        self.e3.insert(0, '0')
        self.e3.place(x=100, y=140)

        self.bt1 = Button(self.master, text='Set', width=10, command=self.setTime).place(x=195, y=77)
        self.bt2 = Button(self.master, text='Count', width=10, command=self.start).place(x=195, y=107)
        self.bt3 = Button(self.master, text='Reset', width=10, command=self.resetTime).place(x=195, y=137)

    def setTime(self):
        self.h = e1.get().zfill(2)
        self.m = e2.get().zfill(2)
        self.s = e3.get().zfill(2)
        self.setValue = self.h + ':' + self.m + ':' + self.s
        self.t.set(self.setValue)

    def start(self):
        global count
        count = 0
        # endtime = int(self.h)*3600 + int(self.m)*60 + int(self.s)
        self.startTime()

    def startTime(self):
        global count
        self.count()
        if count == 1:
            winsound.PlaySound('C:\\Program Files\\pyCountDown\\Sound\\timesup.wav', winsound.SND_FILENAME)

    def resetTime(self):
        global count
        count = 2
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e1.insert(0, '0')
        self.e2.insert(0, '0')
        self.e3.insert(0, '0')
        self.t.set("00:00:00")

    def count(self):
        # global endtime
        # if endtime > 0:
        #     m, s = divmod(endtime, 60)
        #     h, m = divmod(m, 60)
        #     setValue = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
        #     endtime -= 1
        #     self.t.set(setValue)
        global count
        if count == 0:
            self.tmp = str(self.t.get())
            hour, minute, second = map(int, self.tmp.split(':'))
            if second > 0:
                second -= 1
            elif second == 0:
                if minute > 0:
                    second = 59
                    minute -= 1
                elif minute == 0:
                    if hour > 0:
                        minute = 59
                        hour -= 1
                    elif hour == 0:
                        count = 1
            self.setValue = str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)
            self.t.set(self.setValue)
            if count == 0:
                self.master.after(1000,self.startTime)


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()