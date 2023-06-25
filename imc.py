"""
Programa: imc
Descrição: Este programa calcula seu IMC.
Data : 24/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis



h = 0
m = 0

#Entrada de dados

h = float(input("Qual sua altura? "))
m = float(input("Qual seu peso? "))

#Processamento de dados
imc = (m/(h**2))
if imc <= 18.5:
    print(f"O seu IMC é de {imc}, e você está excessivamente magro.")

elif 18.5 < imc <= 25:
    print(f"O seu IMC é de {imc}, e você está em um peso normal.")

elif 25 < imc <= 30:
    print(f"O seu IMC é de {imc}, e você está com sobrepeso.")

else:
    print(f"O seu IMC é de {imc}, e você está obeso.")
    
#Saida de dadaos