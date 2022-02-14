class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def setNome(self, nome):
        self.nome = nome
    def setIdade(self, idade):
        self.idade = idade
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade

p1 = Pessoa('Maria', 41)
p2 = Pessoa('Gabriel', 52)
p3 = Pessoa('Eurico', 30)

print (p1.getNome())
print (p1.getIdade())
p1.setIdade(50)
print (p1.getIdade())
