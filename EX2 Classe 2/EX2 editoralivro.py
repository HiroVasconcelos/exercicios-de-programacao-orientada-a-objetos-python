def pulaLinha():
    print()

class Editora:
    def __init__(self, codigoEditora, razaoSocial, contato, telefone):
        self.codigoEditora = codigoEditora
        self.razaoSocial = razaoSocial
        self.contato = contato
        self.telefone = telefone
    def setCodigoEditora(self,codigoEditora):
        self.codigoEditora = codigoEditora
    def setRazaoSocial(self,razaoSocial):
        self.razaoSocial = razaoSocial
    def setContato(self,contato):
        self.contato = contato
    def setTelefone(self,telefone):
        self.telefone = telefone
    def getCodigoEditora(self):
        return self.codigoEditora
    def getRazaoSocial(self):
        return self.razaoSocial
    def getContato(self):
        return self.contato
    def getTelefone(self):
        return self.telefone

e1 = Editora(5835677468976, 'Dark Horse', 'https://www.darkhorse.com/Help/Contact/', '(503) 652-8815')
e2 = Editora(3454638284864, 'Saraiva', 'saceditorasaraiva@somoseducacao.com.br', '(51) 3364-3406')

class Livro:
    def __init__(self, codigoLivro, descricaoLivro, codigoISBN, publicadora):
        self.codigoLivro = codigoLivro
        self.descricaoLivro = descricaoLivro
        self.codigoISBN = codigoISBN
        self.publicadora = publicadora
    def setCodigoLivro(self,codigoLivro):
        self.codigoLivro = codigoLivro
    def setDescricaoLivro(self,descricaoLivro):
        self.descricaoLivro = descricaoLivro
    def setCodigoISBN(self,codigoISBN):
        self.codigoISBN = codigoISBN
    def setEditora(self,editora):
        self.Editora = Editora
    def getCodigoLivro(self):
         return self.codigoLivro
    def getDescricaoLivro(self):
         return self.descricaoLivro
    def getCodigoISBN(self):
         return self.codigoISBN
    def getPublicadora(self):
         return self.publicadora

l1 = Livro(5432455637098, 'The Sparrow Academy', '543-2-45-563709-8', e1)
l2 = Livro(6574354756854, 'Elsware: Mundo Perdido', '657-4-35-475685-4', e2)

pulaLinha()
print ("O livro " + l1.getDescricaoLivro() + " foi publicado pela editora " + l1.publicadora.getRazaoSocial())
pulaLinha()
print ("O livro " + l2.getDescricaoLivro() + " foi publicado pela editora " + l2.publicadora.getRazaoSocial())
pulaLinha()