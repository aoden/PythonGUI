from Tkinter import *

class MyDialog:


    def __init__(self, parent, label):

        top = self.top = Toplevel(parent)

        Label(top, text="Need to inter value at " + label).pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        print "value is", self.e.get()

        self.top.destroy()


root = Tk()
d = MyDialog(root, "dsds")

root.wait_window(d.top)
