import sqlite3

class Database():
  def __init__(self):
      self.connection = sqlite3.connect('banco.db')
      self.createTable()

  def createTable(self):
      c = self.connection.cursor()

      c.execute("""create table if not exists usuarios (
                  idusuario integer primary key autoincrement ,
                  nome text,
                  telefone text,
                  email text,
                  usuario text,
                  senha text)""")
      self.connection.commit()
      c.close()
