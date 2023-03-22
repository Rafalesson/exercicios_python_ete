# Escreva um programa que solicite ao usuário o valor de uma compra e calcule o valor final da compra com um desconto de 10%.

def Descontar10(valor):
    desconto = valor * 0.1
    resultado = valor - desconto
    
    print(f"\nPreço inicial: {valor}.")
    print(f"Valor do desconto: {desconto}.")
    print(f"Preço final: {resultado}.")

entrada = float(input("\nDigite o valor da compra: "))

Descontar10(entrada)