from tkinter import *

class Application(Frame):
    """A GUI Application with three buttons"""

    def __init__(self,master):
        """ Initialize the Frame """
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Creates three buttons that do nothing"""
        #create first button
        self.inst_lbl = Label(self,text = "Enter password for the secret of longevity")
        self.inst_lbl.grid(row = 0,column = 0, columnspan = 3, sticky = E)

        #create label for password
        self.esp_lbl = Label(self, text = "prodesp: ")
        self.esp_lbl.grid(row =1 ,column = 0 , sticky = W)

        #create entry widget to accept password
        self.esp_ent = Entry(self,  show="*")
        self.esp_ent.grid(row = 1, column =1 , sticky = W)

        #create label for password
        self.produser_lbl = Label(self, text = "username: ")
        self.produser_lbl.grid(row =2 ,column = 0 , sticky = W)

        #create entry widget to accept password
        self.produser_ent = Entry(self)
        self.produser_ent.grid(row = 2, column =1 , sticky = W)


        #create submit button
        self.submit_bttn = Button(self,text = "Submit",command = self.reveal)
        self.submit_bttn.grid(row = 3, column =0 , sticky = W)

        #create text widget
        self.secret_text = Text(self,width = 35 , height =5, wrap = WORD)
        self.secret_text.grid(row = 4 , column = 0 , columnspan = 2, sticky = W)



    def reveal(self):
        """ Display message based on password """
        ESP_contents = self.esp_ent.get()
        USER_contents = self.produser_ent.get()
        message = "EspProd = " + ESP_contents + \
                  "\nUser    = " + USER_contents

        self.secret_text.delete(0.0,END)
        self.secret_text.insert(0.0,message)

    def sel(self):
        selection = "You selected the option " + str(var.get())
        label.config(text = selection)


        var = IntVar()
        Radiobutton(root, text="Option 1", variable=var, value=1, command=sel).pack(anchor=W)
        Radiobutton(root, text="Option 2", variable=var, value=2, command=sel).pack(anchor=W)
        Radiobutton(root, text="Option 3", variable=var, value=3, command=sel).pack(anchor=W)
        label = Label(root)
        label.pack()



#Main
root = Tk()
root.title("First GUI")
root.geometry("290x190")

#object because of the class
app = Application(root)

root.mainloop()
