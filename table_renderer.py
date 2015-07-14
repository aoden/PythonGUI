from openpyxl import *
from tkintertable.Tables import *
from tkintertable.TableModels import *

class TableRenderer:


    def render_table(self, gui_sheet_name='Gui 3', excel_file_name='new exel (1).xlsx', table_area = None):
        global k
        data = []
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
        self.table.bind('<Enter>', self.clicked)

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
    def clicked(self, event):
        try:
            rclicked = self.table.get_row_clicked(event)
            cclicked = self.table.get_col_clicked(event)
            clicks = (rclicked, cclicked)
            print 'clicks:', clicks
            self.table.redrawTable()
        except:
            print 'Error'
        if clicks:
            #Now we try to get the value of the row+col that was clicked.
            try:
                value = self.table.model.getValueAt(clicks[0], clicks[1])
                print(value)
                self.table.setValueA[0]
            except: print 'No record at:', clicks
