
# this class holds details of actions in able to implement undo/redo function
class ActionDetails:

    def __init__(self, col, row, value):
        self.row = row
        self.col = col
        self.value = value