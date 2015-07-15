from tkintertable import *
from table_renderer import TableRenderer
from dialog import MyDialog

class Gui:
    def __init__(self, gui_sheet_name, excel_file_name):
        root = Tk()
        self.root = root;
        self.file_name = excel_file_name
        # Step 2  Adding Menu Bar

        menubar = Menu(root)  # frame that holds the menu buttons

        # Create File menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT, command = lambda: self.new())
        filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT, command = lambda: self.open())
        filemenu.add_command(label="Save", accelerator='Ctrl+S', compound=LEFT, command = lambda: self.save())
        filemenu.add_command(label="Save as", accelerator='Shift+Ctrl+S', command = lambda: self.save_as())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", accelerator='Alt+F4', command = lambda: self.exit())
        menubar.add_cascade(label="File", menu=filemenu)

        # Create Edit menu
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", compound=LEFT, accelerator='Ctrl+Z')
        editmenu.add_command(label="Redo", compound=LEFT, accelerator='Ctrl+Y')
        editmenu.add_separator()
        editmenu.add_command(label="Cut", compound=LEFT, accelerator='Ctrl+X')
        editmenu.add_command(label="Copy", compound=LEFT, accelerator='Ctrl+C')
        editmenu.add_command(label="Paste", compound=LEFT, accelerator='Ctrl+V')
        editmenu.add_separator()
        editmenu.add_command(label="Find", underline=0, accelerator='Ctrl+F')
        editmenu.add_separator()
        editmenu.add_command(label="Select All", underline=7, accelerator='Ctrl+A')
        menubar.add_cascade(label="Edit", menu=editmenu)

        # Create View menu
        viewmenu = Menu(menubar, tearoff=0)
        showln = IntVar()
        showln.set(1)
        viewmenu.add_checkbutton(label="Show Line Number", variable=showln)
        showinbar = IntVar()
        showinbar.set(1)
        viewmenu.add_checkbutton(label="Show Info Bar at Bottom", variable=showinbar)
        hltln = IntVar()
        viewmenu.add_checkbutton(label="Highlight Current Line", onvalue=1, offvalue=0, variable=hltln)
        themesmenu = Menu(menubar, tearoff=0)
        viewmenu.add_cascade(label="Themes", menu=themesmenu)

        # we define a color scheme dictionary containg name and color code as key value pair
        clrschms = {
            '1. Default White': 'FFFFFF',
            '2. Greygarious Grey': 'D1D4D1',
            '3. Lovely Lavender': 'E1E1FF',
            '4. Aquamarine': 'D1E7E0',
            '5. Bold Beige': 'FFF0E1',
            '6. Cobalt Blue': '333AA',
            '7. Olive Green': '5B8340',
        }

        self.colors = clrschms

        themechoice = StringVar()
        themechoice.set('1. Default White')
        for k in sorted(clrschms):
            themesmenu.add_radiobutton(label=k, variable=themechoice, command = lambda arg0=k: self.change_theme(clrschms[arg0]))
        menubar.add_cascade(label="View", menu=viewmenu)

        # Create About menu
        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="About")
        aboutmenu.add_command(label="Help")
        menubar.add_cascade(label="About", menu=aboutmenu)

        # Displaying menu on top of root.
        root.config(menu=menubar)

        shortcutbar = Frame(root, height=25, bg='light sea green')
        shortcutbar.pack(expand=NO, fill=X)
        lnlabel = Label(root, width=2, bg='antique white')
        lnlabel.pack(side=LEFT, anchor='nw', fill=Y)

        table_area = Frame(root)
        table_area.pack(side=LEFT, anchor='nw', fill=Y)
        # render table
        renderer = TableRenderer()
        renderer.render_table(gui_sheet_name, excel_file_name, table_area)
        self.table_renderer = renderer;
        # textPad = Text(root)
        # textPad.pack(expand=YES, fill=BOTH)
        # scroll=Scrollbar(textPad)
        # textPad.configure(yscrollcommand=scroll.set)
        # scroll.config(command=textPad.yview)
        # scroll.pack(side=RIGHT,fill=Y)

        # root.bind('<ButtonRelease-1>', self.clicked)

        root.geometry("500x300")
        root.protocol("WM_DELETE_WINDOW", self.on_close)
        root.mainloop()

    # def clicked(self, event):
    #     print('adsd')

    def on_close(self):
        sys.exit(0)

    def open(self):

        try:
            d1 = MyDialog(self.root, "enter file path:")
            d2 = MyDialog(self.root, "enter sheet name:")
            Gui(d2.value, d1.value)
        except:
            return
        return

    def save(self):
        try:
            self.table_renderer.workbook.save(self.file_name)
        except:
            return
        return

    def save_as(self):

        try:
            d1 = MyDialog(self.root, "enter file path:")
            self.table_renderer.workbook.save(d1.value)
        except:
            return
        return

    def exit(self):
        sys.exit(0)
        return

    def change_theme(self, value):

        print(value)