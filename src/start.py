from Users import Users
from DataTable import DataTable
from model.DataTable.TableData import TableData
from model.DataTable.TableLine import TableLine

from tkinter import *

class Application:
  def __init__ (self, master=None):
    data = TableData()
    data.insertLine(TableLine())
    data.data[0].data = ['asd', 'dsa']

    self.datatable = DataTable(master)
    self.datatable.headers = ['nome', 'idade']

root = Tk()
Application(root)
root.mainloop()
