from tkinter import *

class Application:
  def __init__ (self, master=None):
    self.font = ('Arial', '10')

    self.container1 = Frame(master)
    self.container1['pady'] = 10
    self.container1.pack()

    self.container2 = Frame(master)
    self.container2['padx'] = 20
    self.container2.pack()

    self.container3 = Frame(master)
    self.container3['padx'] = 20
    self.container3.pack()

    self.container4 = Frame(master)
    self.container4['pady'] = 20
    self.container4.pack()

    self.title = Label(self.container1, text='Dados do Usuário')
    self.title['font'] = self.font + ('bold',)
    self.title.pack()

    self.nameLabel = Label(self.container2, text='Nome', font=self.font)
    self.nameLabel.pack(side=LEFT)

    self.name = Entry(self.container2)
    self.name['width'] = 30
    self.name['font'] = self.font
    self.name.pack(side=LEFT)

    self.passwordLabel = Label(self.container3, text='Senha', font=self.font)
    self.passwordLabel.pack(side=LEFT)

    self.password = Entry(self.container3)
    self.password['width'] = 30
    self.password['font'] = self.font
    self.password['show'] = '*'
    self.password.pack(side=LEFT)

    self.button = Button(self.container4, text='Entrar')
    self.button['font'] = ('Calibri', '14')
    self.button['width'] = 18
    self.button['command'] = self.verifyPassword
    self.button.pack()

    self.message = Label(self.container4, text='')
    self.message.pack()

  def verifyPassword (self):
    name = self.name.get()
    password = self.password.get()

    if name == 'ygor' and password == 'senha':
      self.message['text'] = 'Autenticado'
    else:
      self.message['text'] = 'Usuario ou senha incorreta'

root = Tk()
Application(root)
root.mainloop()
