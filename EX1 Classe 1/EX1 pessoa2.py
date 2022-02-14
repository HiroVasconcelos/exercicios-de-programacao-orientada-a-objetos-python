def pulaLinha():
    print()

class Pessoa:
    def __init__(self, nome, idade, endereco, sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.sexo = sexo
    def setNome(self, nome):
        self.nome = nome
    def setIdade(self, idade):
        self.idade = idade
    def setEndereco(self, endereco):
        self.endereco = endereco
    def setSexo(self, sexo):
        self.sexo = sexo
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getEndereco(self):
        return self.endereco
    def getSexo(self):
        return self.sexo

p1 = Pessoa('Maria', 36, 'Nova Santa Rita', 'Feminino')
p2 = Pessoa('Gabriel', 52, 'Porto Alegre', 'Masculino')
p3 = Pessoa('Eurico', 30, 'Canoas', 'Masculino')

print (p1.getNome())
print (p1.getIdade())
print (p1.getEndereco())
print (p1.getSexo())
pulaLinha()
print (p2.getNome())
print (p2.getIdade())
print (p2.getEndereco())
print (p2.getSexo())
pulaLinha()
print (p3.getNome())
print (p3.getIdade())
print (p3.getEndereco())
print (p3.getSexo())
