from tkinter import *

class Application:
  def __init__(self, master=None):
    self.widget1 = Frame(master)
    self.widget1.pack()

    self.msg = Label(self.widget1, text="Meu texto")
    self.msg['font'] = ('Verdana', '10', 'italic', 'bold')
    self.msg.pack()

    self.sair = Button(self.widget1)
    self.sair['text'] = 'Sair'
    self.sair['font'] = ('Calibri', '10')
    self.sair['width'] = 5
    self.sair.bind('<Button-1>', self.mudarTexto)
    self.sair.pack()

  def mudarTexto(self, event):
    print(event)
    if self.msg['text'] == 'Meu texto':
      self.msg['text'] = 'Meu widget clicado'
    else:
      self.msg['text'] = 'Meu texto'

root = Tk()
Application(root)
root.mainloop()
