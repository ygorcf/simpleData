from Users import Users
from tkinter import *

class Application:
  def __init__ (self, master=None):
    self.font = ('Verdana', '8')

    self.container1 = Frame(master)
    self.container1['pady'] = 10
    self.container1.pack()
    self.container2 = Frame(master)
    self.container2['padx'] = 20
    self.container2['pady'] = 5
    self.container2.pack()
    self.container3 = Frame(master)
    self.container3['padx'] = 20
    self.container3['pady'] = 5
    self.container3.pack()
    self.container4 = Frame(master)
    self.container4['padx'] = 20
    self.container4['pady'] = 5
    self.container4.pack()
    self.container5 = Frame(master)
    self.container5['padx'] = 20
    self.container5['pady'] = 5
    self.container5.pack()
    self.container6 = Frame(master)
    self.container6['padx'] = 20
    self.container6['pady'] = 5
    self.container6.pack()
    self.container7 = Frame(master)
    self.container7['padx'] = 20
    self.container7['pady'] = 5
    self.container7.pack()
    self.container8 = Frame(master)
    self.container8['padx'] = 20
    self.container8['pady'] = 10
    self.container8.pack()
    self.container9 = Frame(master)
    self.container9['pady'] = 15
    self.container9.pack()

    self.title = Label(self.container1, text='Informe os dados:')
    self.title['font'] = self.font + ('bold',)
    self.title.pack()

    self.lblIdUsuario = Label(self.container2, text='idUsuario:', font=self.font, width=10)
    self.lblIdUsuario.pack(side=LEFT)

    self.txtIdUsuario = Entry(self.container2, font=self.font, width=10)
    self.txtIdUsuario.pack(side=LEFT)

    self.btnBuscar = Button(self.container2, text="Buscar", font=self.font, width=10)
    self.btnBuscar["command"] = self.findUser
    self.btnBuscar.pack(side=RIGHT)

    self.lblNome = Label(self.container3, text='Nome:', font=self.font, width=10)
    self.lblNome.pack(side=LEFT)

    self.txtNome = Entry(self.container3, font=self.font, width=25)
    self.txtNome.pack(side=LEFT)

    self.lblTelefone = Label(self.container4, text='Telefone:', font=self.font, width=10)
    self.lblTelefone.pack(side=LEFT)

    self.txtTelefone = Entry(self.container4, font=self.font, width=25)
    self.txtTelefone.pack(side=LEFT)

    self.lblEmail = Label(self.container5, text='Email:', font=self.font, width=10)
    self.lblEmail.pack(side=LEFT)

    self.txtEmail = Entry(self.container5, font=self.font, width=25)
    self.txtEmail.pack(side=LEFT)

    self.lblUsuario = Label(self.container6, text='Usuario:', font=self.font, width=10)
    self.lblUsuario.pack(side=LEFT)

    self.txtUsuario = Entry(self.container6, font=self.font, width=25)
    self.txtUsuario.pack(side=LEFT)

    self.lblSenha = Label(self.container7, text='Senha:', font=self.font, width=10)
    self.lblSenha.pack(side=LEFT)

    self.txtSenha = Entry(self.container7, font=self.font, width=25, show="*")
    self.txtSenha.pack(side=LEFT)

    self.btnInsert = Button(self.container8, text="Inserir", font=self.font, width=12)
    self.btnInsert["command"] = self.insertUser
    self.btnInsert.pack(side=LEFT)

    self.btnUpdate = Button(self.container8, text="Alterar", font=self.font, width=12)
    self.btnUpdate["command"] = self.updateUser
    self.btnUpdate.pack(side=LEFT)

    self.btnDelete = Button(self.container8, text="Excluir", font=self.font, width=12)
    self.btnDelete["command"] = self.deleteUser
    self.btnDelete.pack(side=LEFT)

    self.message = Label(self.container9, text='')
    self.message["font"] = ("Verdana", "9", "italic")
    self.message.pack()

  def insertUser (self):
    user = Users()

    user.nome = self.txtNome.get()
    user.telefone = self.txtTelefone.get()
    user.email = self.txtEmail.get()
    user.usuario = self.txtUsuario.get()
    user.senha = self.txtSenha.get()

    self.message["text"] = user.insertUser()

    if user.idUsuario != 0:
      self.txtIdUsuario["text"] = user.idUsuario
    else:
      self.txtIdUsuario.delete(0, END)

    self.txtNome.delete(0, END)
    self.txtTelefone.delete(0, END)
    self.txtEmail.delete(0, END)
    self.txtUsuario.delete(0, END)
    self.txtSenha.delete(0, END)

  def updateUser (self):
    user = Users()

    user.idUsuario = self.txtIdUsuario.get()
    user.nome = self.txtNome.get()
    user.telefone = self.txtTelefone.get()
    user.email = self.txtEmail.get()
    user.usuario = self.txtUsuario.get()
    user.senha = self.txtSenha.get()

    self.message["text"] = user.updateUser()

    self.txtIdUsuario.delete(0, END)
    self.txtNome.delete(0, END)
    self.txtTelefone.delete(0, END)
    self.txtEmail.delete(0, END)
    self.txtUsuario.delete(0, END)
    self.txtSenha.delete(0, END)

  def deleteUser (self):
    user = Users()

    user.idUsuario = self.txtIdUsuario.get()

    self.message["text"] = user.deleteUser()

    self.txtIdUsuario.delete(0, END)
    self.txtNome.delete(0, END)
    self.txtTelefone.delete(0, END)
    self.txtEmail.delete(0, END)
    self.txtUsuario.delete(0, END)
    self.txtSenha.delete(0, END)

  def findUser (self):
    user = Users()

    idusuario = self.txtIdUsuario.get()

    self.message["text"] = user.getUser(idusuario)

    self.txtIdUsuario.delete(0, END)
    self.txtIdUsuario.insert(INSERT, user.idUsuario)
    self.txtNome.delete(0, END)
    self.txtNome.insert(INSERT, user.nome)
    self.txtTelefone.delete(0, END)
    self.txtTelefone.insert(INSERT, user.telefone)
    self.txtEmail.delete(0, END)
    self.txtEmail.insert(INSERT, user.email)
    self.txtUsuario.delete(0, END)
    self.txtUsuario.insert(INSERT, user.usuario)
    self.txtSenha.delete(0, END)
    self.txtSenha.insert(INSERT, user.senha)

root = Tk()
Application(root)
root.mainloop()
