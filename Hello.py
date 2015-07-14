from Tkinter import *
from gui import Gui

class Application(Frame):
    """A GUI Application with t        #
hree buttons"""

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.var  = IntVar()
        """ Creates three buttons that do nothing"""
        # create first button
        self.inst_lbl = Label(self, text="Enter password for the secret of longevity")
        self.inst_lbl.grid(row=0, column=0, columnspan=3, sticky=E)

        # create label for password
        self.esp_lbl = Label(self, text="prodesp: ")
        self.esp_lbl.grid(row=1, column=0, sticky=W)

        # create entry widget to accept password
        self.esp_ent = Entry(self, show="*")
        self.esp_ent.grid(row=1, column=1, sticky=W)

        # create label for password
        self.produser_lbl = Label(self, text="username: ")
        self.produser_lbl.grid(row=2, column=0, sticky=W)

        # create entry widget to accept password
        self.produser_ent = Entry(self)
        self.produser_ent.grid(row=2, column=1, sticky=W)

        # create submit button
        self.submit_bttn = Button(self, text="Submit", command=self.reveal)
        self.submit_bttn.grid(row=3, column=0, sticky=W)

        self.radio_1 = Radiobutton(self, text="Gui 1", variable=self.var, value=1)
        self.radio_1.grid(row=4, column=0, sticky=W)

        self.radio_2 = Radiobutton(self, text="Gui 2", variable=self.var, value=2)
        self.radio_2.grid(row=5, column=0, sticky=W)

        self.radio_3 = Radiobutton(self, text="Gui 3", variable=self.var, value=3)
        self.radio_3.grid(row=6, column=0, sticky= W)

        # create text widget
        self.secret_text = Text(self, width=35, height=5, wrap=WORD)
        self.secret_text.grid(row=7, column=0, columnspan=2, sticky=W)

    def reveal(self):

        select_option = self.var.get()
        if (select_option == 1):
            Gui('Gui 1', 'new exel (1).xlsx')
        elif (select_option == 2):
            Gui('Gui 2', 'new exel (1).xlsx')
        elif (select_option == 3):
            Gui('Gui 3', 'new exel (1).xlsx')

# Main
root = Tk()
root.title("First GUI")
root.geometry("290x290")

# object because of the class
app = Application(root)

root.mainloop()
