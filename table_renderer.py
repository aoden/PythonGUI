from openpyxl import *
from tkintertable import *

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
        table = TableCanvas(table_area, model=table_model)
        table.createTableFrame()
        table.redrawTable()
        for j in range(0, col_num):
            table.addColumn(col_labels[j])
        for i in range(1, row_num + 1):
            print('enter row ' + str(i))
            for j in range(0, col_num):
                cell = sh[str(col_labels[j]) + str(i)].value
                if (cell == None):
                    cell = ''
                data.append(cell)
                # print(cell)
                print(data)
            table.addRow()
            for k in range(0, col_num):
                table.model.data[i][col_labels[k]] = data[k]
            data = []
            table.redrawTable()
