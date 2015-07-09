from tktable import ArrayVar


def sample_test():
    from Tkinter import Tk, Scrollbar, Button
    import tktable

    def test_cmd(event):
        print ('command')

    def browsecmd(event):
        print ('browsecmd')
        #print event.__dict__

    root = Tk()
    quit = Button(root, text="QUIT", command=root.destroy)
    quit.pack(side = 'bottom')

    numrows, numcols = 10, 10

    var = ArrayVar(root)
    for y in range(numrows):
        for x in range(numcols):
            index = "%i,%i" % (y, x)
            #add data
            #var[index] = index

    table = tktable.Table(root,
                 rows=numrows+1,
                 cols=numcols+1,
                 state='normal',
                 width=6,
                 height=6,
                 titlerows=1,
                 titlecols=1,
                 roworigin=-1,
                 colorigin=-1,
                 selectmode='normal',
                 selecttype='row',
                 rowstretch='unset',
                 colstretch='last',
                 browsecmd=browsecmd,
                 flashmode='on',
                 variable=var,
                 usecommand=0,
                 command=test_cmd)

    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm
    s = Scrollbar(root, orient='vertical', command=table.yview_scroll)
    table.config(yscrollcommand=s.set)
    s.pack(side='right', fill='y')

    table.pack(expand=1, fill='both')
    table.tag_configure('sel', background = 'yellow')
    table.tag_configure('active', background = 'blue')
    table.tag_configure('title', anchor='w', bg='red', relief='sunken')

    data = ('py','t','h','o','n','','+','','Tk','')

    def add_new_data(*args):
        #table.config(state='normal')
        table.insert_rows('end', 1)
        r = table.index('end').split(',')[0] #get row number <str>
        args = (r,) + args
        idx = r + ',-1'
        table.set('row', idx, *args)
        table.see(idx)
        #table.config(state='disabled')

    root.after(3000, add_new_data, *data)
    #root.after(4000, add_new_data, *data)
    root.mainloop()

sample_test()