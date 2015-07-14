from tkintertable.Tables import TableCanvas
from table_renderer import TableRenderer
#https://github.com/dmnfarrell/tkintertable
root = Tk()
# Step 2  Adding Menu Bar
#

menubar = Menu(root)  # frame that holds the menu buttons


# Create File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT)
filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT)
filemenu.add_command(label="Save", accelerator='Ctrl+S', compound=LEFT)
filemenu.add_command(label="Save as", accelerator='Shift+Ctrl+S')
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator='Alt+F4')
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
themechoice = StringVar()
themechoice.set('1. Default White')
for k in sorted(clrschms):
    themesmenu.add_radiobutton(label=k, variable=themechoice)
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
renderer.render_table('Gui 3', 'new exel (1).xlsx',table_area)
# textPad = Text(root)
# textPad.pack(expand=YES, fill=BOTH)
# scroll=Scrollbar(textPad)
# textPad.configure(yscrollcommand=scroll.set)
# scroll.config(command=textPad.yview)
# scroll.pack(side=RIGHT,fill=Y)

root.geometry("500x300")
root.mainloop()
