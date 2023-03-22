# Escreva um programa que solicite ao usuário a idade de uma pessoa em anos e exiba a idade em meses e em dias. (Dica: um ano tem 12 meses e um mês tem aproximadamente 30 dias)

def AnosParaMesesDias(idade):
    meses = idade * 12
    dias = meses * 30
    
    if(idade == 1):
        print(f"\n{idade} ano represeta {meses} meses e aproximadamente {dias} dias.")
    else:
        print(f"\n{idade} anos represetam {meses} meses e aproximadamente {dias} dias.")

entrada = float(input("\nDigite a idade: "))

AnosParaMesesDias(entrada)