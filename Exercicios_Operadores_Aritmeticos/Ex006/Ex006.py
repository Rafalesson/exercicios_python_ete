# Escreva um programa que solicite ao usuário a quantidade de horas trabalhadas em um dia e o valor da hora trabalhada, e exiba o salário diário.

def CalculaSalario(hora, precoHora):
    resultado = hora * precoHora
    print(f"\nQuantidade de horas trabalhadas: {hora} horas.")
    print(f"Valor da hora trabalhada: R${precoHora}.")
    print(f"Salário ao fim do dia: R${resultado}.")

qtdHora = float(input("\nDigite a quantidade horas trabalhadas: "))
precoHora = float(input("Digite o valor da hora trabalhada: "))

CalculaSalario(qtdHora, precoHora)