from Tkinter import *

class Tabla(Frame):
    def __init__(self, parent, rows=10, columns=3, wid=10):
        # use black background so it "peeks through" to 
        # form grid lines
        Frame.__init__(self, parent, background="black")
	
	
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Label(self, text="%s/%s" % (row, column), 
                                 borderwidth=0, width=wid)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)