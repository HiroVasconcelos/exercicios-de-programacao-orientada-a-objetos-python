def pulaLinha():
    print()

#FUNCIONARIO - CLASSE MAE
class Funcionario:
    #INIT
    def __init__(self, nome, cpf, salario, departamento):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento
    #SET
    def setNome(self, nome):
        self.nome = nome
    def setCpf(self, cpf):
        self.cpf = cpf
    def setSalario(self, salario):
        self.salario = salario
    def setDepartamento(self, departamento):
        self.departamento = departamento
    #GET    
    def getNome(self):
        return self.nome
    def getCpf(self):
        return self.cpf
    def getSalario(self):
        return self.salario
    def getDepartamento(self):
        return self.departamento
    #PLUS
    def bonificar(self):
        self.salario = (self.salario*0.1)+self.salario
        return self.salario

#GERENTE - CLASSE FILHA
class Gerente(Funcionario):
    #INIT
    def __init__(self, nome, cpf, salario, departamento, senha, numFuncionarios):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        self.numFuncionarios = numFuncionarios
    #SET
    def setSenha(self, senha):
        self.senha = senha
    def setNumFuncionarios(self, numFuncionarios):
        self.numFuncionarios = numFuncionarios
    #GET
    def getSenha(self):
        return self.senha
    def getNumFuncionarios(self):
        return self.numFuncionarios
    #PLUS
    def bonificar(self):
        self.salario = (self.salario*0.15)+self.salario
        return self.salario
    def autenticarSenha(self, senha):
        if self.senha == senha:
            return True
        else:
            return False

#VENDEDOR - CLASSE FILHA
class Vendedor(Funcionario):
    #INIT
    def __init__(self, nome, cpf, salario, departamento, quantidadeVendas, comissao):
        super().__init__(nome, cpf, salario, departamento)
        self.quantidadeVendas = quantidadeVendas
        self.comissao = comissao
    #SET
    def setQuantidadeVendas(self, quantidadeVendas):
        self.quantidadeVendas = quantidadeVendas
    def setComissao(self, comissao):
        self.comissao = comissao
    #GET
    def getQuantidadeVendas(self):
        return self.quantidadeVendas
    def getComissao(self):
        return self.comissao
    #PLUS
    def atualizaQuantidadeVendas(self,quantidadeVendas):
        self.quantidadeVendas = self.quantidadeVendas + quantidadeVendas
    def calculaSalario(self):
        self.salario = self.salario + self.comissao
        return self.salario

#TESTE - FUNCIONARIOS
f1 = Funcionario('Fernando', '3040009401', 1600.0, 'Funcionario')
#TESTE - GERENTE
g1 = Gerente('Claudia', '4320006508', 4700.0, 'Gerente', 'clau5670', 78)
#TESTE - VENDEDOR
v1 = Vendedor('Marcio', '1240007504', 1450.0, 'Vendedor', 34, 200.0)

#PRINT - FUNCIONARIO
print("=-=-=-=-=-=")
print("FUNCIONARIO")
print("=-=-=-=-=-=")

print("[NOME]")
print(f1.getNome())

print("[CPF]")
print(f1.getCpf())

print('[SALARIO]')
print (f1.getSalario())

print("[DEPARTAMENTO]")
print(f1.getDepartamento())

print("[BONIFICACAO]")
print(f1.bonificar())
pulaLinha()
#PRINT - GERENTE
print("=-=-=-=")
print("GERENTE")
print("=-=-=-=")

print("[NOME]")
print(g1.getNome())

print("[CPF]")
print(g1.getCpf())

print('[SALARIO]')
print (g1.getSalario())

print("[DEPARTAMENTO]")
print(g1.getDepartamento())

print("[SENHA]")
print(g1.getSenha())

print("[NUMERO DE FUNCIONARIOS]")
print(g1.getNumFuncionarios())

print("[VALIDACAO DE SENHA]")
print(g1.autenticarSenha("senha"))

print("[BONIFICACAO]")
print(g1.bonificar())
pulaLinha()
#PRINT - VENDEDOR
print("=-=-=-=-=")
print("VENDEDOR")
print("=-=-=-=-=")

print("[NOME]")
print(v1.getNome())

print("[CPF]")
print(v1.getCpf())

print('[SALARIO]')
print (v1.getSalario())

print("[DEPARTAMENTO]")
print(v1.getDepartamento())

print("[QUANTIDADE DE VENDAS]")
print(v1.getQuantidadeVendas())

print("[COMISSAO]")
print(v1.getComissao())

v1.atualizaQuantidadeVendas(8)
print("[QUANTIDADE DE VENDAS ATUALIZADA]")
print(v1.getQuantidadeVendas())

print("[SALARIO TOTAL]")
print(v1.calculaSalario())
