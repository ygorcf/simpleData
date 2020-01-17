from tkinter import Label, Frame, LEFT, FLAT
from model.DataTable.TableData import TableData

class DataTable():
  def __init__(self, container, headers=[]):
    self._value = None
    self.lists = []
    self.headers = None
    self.listsContainer = Frame(container)
    self.listsContainer['relief'] = FLAT
    self.listsContainer['padx'] = 0
    self.listsContainer['pady'] = 0
    self.listsContainer['bg'] = '#000'
    self.listsContainer.pack()

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if not type(value) == TableData and value != None:
      raise TypeError

    print(self.lists)

  @property
  def headers(self):
    return self._headers

  @headers.setter
  def headers(self, value):
    self._headers = value
    self.value = None

    self.lists = []
    if value != None:
      for val in value:
        listbox = Frame(self.listsContainer)
        listbox['relief'] = FLAT
        listbox['borderwidth'] = 0
        listbox.pack(side=LEFT)

        text = Label(listbox, text = val)
        text['borderwidth'] = 1
        text.pack()

        self.lists.append(listbox)
