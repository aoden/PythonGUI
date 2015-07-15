from Tkinter import *

class MyDialog:


    def __init__(self, parent, label):

        top = self.top = Toplevel(parent)

        Label(top, text= label).pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)
        parent.wait_window(self.top)

    def ok(self):

        self.value = self.e.get()
        self.top.destroy()
