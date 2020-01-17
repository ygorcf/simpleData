from .TableLine import TableLine

class TableData:
  def __init__(self):
    self.data = []

  def insertLine(self, line):
    if not isinstance(line, TableLine):
      raise TypeError
    self.data.append(line)
