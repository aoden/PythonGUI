from tktable import ArrayVar


def sample_test():
    from tkinter import Tk, Scrollbar, Button
    import tkinter
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
            var[index] = index

    test = tktable.Table(root,
                 rows=numrows+1,
                 cols=numcols+1,
                 state='normal',
                 width=6,
                 height=6,
                 titlerows=1,
                 titlecols=1,
                 roworigin=-1,
                 colorigin=-1,
                 selectmode='extended',
                 selecttype='row',
                 rowstretch='unset',
                 colstretch='last',
                 browsecmd=browsecmd,
                 flashmode='on',
                 variable=var,
                 usecommand=0,
                 command=test_cmd)

    # http://effbot.org/zone/tkinter-scrollbar-patterns.htm
    s = Scrollbar(root, orient='vertical', command=test.yview_scroll)
    test.config(yscrollcommand=s.set)
    s.pack(side='right', fill='y')

    test.pack(expand=1, fill='both')
    test.tag_configure('sel', background = 'yellow')
    test.tag_configure('active', background = 'blue')
    test.tag_configure('title', anchor='w', bg='red', relief='sunken')

    data = ('py','t','h','o','n','','+','','Tk','')

    def add_new_data(*args):
        #test.config(state='normal')
        test.insert_rows('end', 1)
        r = test.index('end').split(',')[0] #get row number <str>
        args = (r,) + args
        idx = r + ',-1'
        test.set('row', idx, *args)
        test.see(idx)
        #test.config(state='disabled')

    root.after(3000, add_new_data, *data)
    root.after(4000, add_new_data, *data)
    root.mainloop()

sample_test()