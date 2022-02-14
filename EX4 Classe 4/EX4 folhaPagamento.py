import os
import time

#EMPREGADO - CLASSE MAE
class Empregado:
    #INIT
    def __init__(self, nome):
        self.nome = nome
    #SET
    def setNome(self, nome):
        self.nome = nome
    #GET
    def getNome(self):
        return self.nome
    #PLUS
    def getPagamento(self):
        pass

#ASSALARIADO - CLASSE FILHA
class Assalariado(Empregado):
    #INIT
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario
    #SET
    def setSalario(self, salario):
        self.salario = salario
    #GET
    def getSalario(self):
        return self.salario
    #PLUS
    def getPagamento(self):
        return self.salario

#HORISTA - CLASSE FILHA
class Horista(Empregado):
    #INIT
    def __init__(self, nome, valorHora, quantidadeHoras):
        super().__init__(nome)
        self.valorHora = valorHora
        self.quantidadeHoras = quantidadeHoras
    #SET
    def setValorHora(self, valorHora):
        self.valorHora = valorHora
    def setQuantidadeHoras(self, quantidadeHoras):
        self.quantidadeHoras = quantidadeHoras
    #GET
    def getValorHora(self):
        return self.valorHora
    def getQuantidadeHoras(self):
        return self.quantidadeHoras
    #PLUS
    def getPagamento(self):
        return (self.valorHora * self.quantidadeHoras * (5*4.5))

AouH = []
nome = []
folha = []

os.system("cls")
num = int(input("Insira o número de funcionários que deseja contratar: "))
os.system("cls")

cont = 0
while cont < num:
    print(f"Defina como o {cont + 1}° empregado será pago baseado nas opções abaixo:\n\n1 - Assalariado\n2 - Horista\n")
    resp = input("Insira o número correspondente a sua resposta: ")
    if resp == "1":
        defaultA = Assalariado('zero', 00)
        os.system("cls")
        print("Você escolheu a opção 1 - Assalariado.\n")
        time.sleep(1)
        os.system("cls")
        defaultA.setNome(input("Digite o nome de seu funcionario: "))
        nome.append(defaultA.getNome())
        defaultA.setSalario(float(input("Digite o salario de seu funcionario: ")))
        os.system("cls")
        folha.append(defaultA.getPagamento())
        AouH.append("assalariado")
        cont += 1
    elif resp == "2":
        defaultH = Horista('zero', 00, 00)
        os.system("cls")
        print("Você escolheu a opção 2 - Horista.\n")
        time.sleep(1)
        os.system("cls")
        defaultH.setNome(input("Digite o nome de seu funcionario: "))
        nome.append(defaultH.getNome())
        defaultH.setValorHora(float(input("Digite o quanto seu funcionario ganha p/hora: ")))
        defaultH.setQuantidadeHoras(int(input("Digite a quantidade de horas que seu funcionario trabalha p/semana: ")))
        os.system("cls")
        folha.append(defaultH.getPagamento())
        AouH.append("horista")
        cont += 1

    else:
        os.system("cls")
        print("Resposta inválida, por favor tente novamente.")
        time.sleep(1)
        os.system("cls")

print("Folha Salarial\n")
cont = 0
while cont < num:
    print(f"O(a) funcionário(a) {AouH[cont]} {nome[cont]} ganha R${round(folha[cont],2)} por mês.")
    cont+=1

print(f"\nGasto mensal com funcionários: R${round(sum(folha),2)}\n")
time.sleep(5)
input("Pressione ENTER para terminar a execução\n")
os.system("cls")
