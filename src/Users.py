from Database import Database

class Users(object):
  def __init__(self, idUsuario = 0, nome = '', telefone = '', email = '', usuario = '', senha = ''):
    self.info = {}
    self.idUsuario = idUsuario
    self.nome = nome
    self.telefone = telefone
    self.email = email
    self.usuario = usuario
    self.senha = senha

  def insertUser(self):
    database = Database()
    try:
      c = database.connection.cursor()
      c.execute("""
        INSERT INTO usuarios (nome, telefone, email, usuario, senha)
        VALUES ('{}', '{}', '{}', '{}', '{}')
      """.format(self.nome, self.telefone, self.email, self.usuario, self.senha))
      database.connection.commit()
      c.close()
      return "Usuário cadastrado com sucesso!"
    except:
      return "Ocorreu um erro ao cadastrar o usuário."

  def updateUser(self):
    database = Database()
    try:
      c = database.connection.cursor()
      c.execute("""
        UPDATE usuarios SET nome='{}', telefone='{}', email='{}',
        usuario='{}', senha='{}' WHERE idusuario={}
      """.format(self.nome, self.telefone, self.email, self.usuario, self.senha, self.idUsuario))
      database.connection.commit()
      c.close()
      return "Usuário atualizado com sucesso!"
    except:
      return "Ocorreu um erro ao atualizar o usuário."

  def deleteUser(self):
    database = Database()
    try:
      c = database.connection.cursor()
      c.execute("""
        DELETE FROM usuarios WHERE idusuario={}
      """.format(self.idUsuario))
      database.connection.commit()
      c.close()
      return "Usuário atualizado com sucesso!"
    except:
      return "Ocorreu um erro ao atualizar o usuário."

  def getUser(self, idusuario):
    database = Database()
    try:
      c = database.connection.cursor()
      c.execute("""
        SELECT * FROM usuarios WHERE idusuario={}
      """.format(idusuario))

      for line in c:
        self.idUsuario = line[0]
        self.nome = line[1]
        self.telefone = line[3]
        self.email = line[4]
        self.usuario = line[5]
        self.senha = line[6]
      c.close()
      return "Usuário buscado com sucesso!"
    except:
      return "Ocorreu um erro ao buscar o usuário."
