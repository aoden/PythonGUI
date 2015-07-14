from openpyxl import *
from tkintertable.Tables import *
from tkintertable.TableModels import *
from dialog import *
import re


class TableRenderer:
    def render_table(self, gui_sheet_name='Gui 3', excel_file_name='new exel (1).xlsx', table_area=None):
        global k
        data = []
        self.parent = table_area
        table_area.bind('<ButtonRelease-1>', self.clicked)
        # array contains excel column header, I only add 7 values here, you can add more if you want
        col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        wb = load_workbook(excel_file_name)
        sh = wb.get_sheet_by_name(gui_sheet_name)
        col_num = sh.get_highest_column()
        row_num = sh.get_highest_row()
        table_model = TableModel()
        # table_model.importDict(data)
        self.table = TableCanvas(table_area, model=table_model, editable=TRUE)
        self.table.createTableFrame()
        self.table.bind('<ButtonPress-1>', self.clicked)

        for j in range(0, col_num):
            self.table.addColumn(col_labels[j])

        for i in range(1, row_num + 1):
            print('enter row ' + str(i))
            for j in range(0, col_num):
                cell = sh[str(col_labels[j]) + str(i)].value
                if cell == None:
                    cell = ''
                data.append(cell)
                # print(cell)
                print(data)
            self.table.addRow()
            for k in range(0, col_num):
                self.table.model.data[i][col_labels[k]] = data[k]
            data = []
            self.table.redrawTable()

        self.change_emails()

    def clicked(self, event):
        try:
            rclicked = self.table.get_row_clicked(event)
            cclicked = self.table.get_col_clicked(event)
            clicks = (rclicked, cclicked)
            print 'clicks:', clicks
        except:
            print 'Error'
        if clicks:
            # Now we try to get the value of the row+col that was clicked.
            try:
                value = self.table.model.getValueAt(clicks[0], clicks[1])
                # check cell with value is "" or " "
                if (value == '" "' or value == '""'):
                    d = MyDialog(self.parent, "")
                    self.table.model.setValueAt(d.value, clicks[0], clicks[1])
                    self.table.redrawTable()
            except:
                print 'No record at:', clicks

    # change emails values
    def change_emails(self):

        model = self.table.model
        #loop through cells to find emails if any
        for i in range(0, model.getColumnCount() - 1):
            for j in range(0, model.getRowCount() - 1):
                if (re.match("[^@]+@[^@]+\.[^@]+", model.getValueAt(j, i))): # find email by regular expression
                    print("found " + model.getValueAt(j, i))
                    model.setValueAt('InsDataOps@lexisNexis.com', j, i) # change email value
                    self.table.redrawTable()
