# Escreva um programa que solicite ao usuário um número e exiba se ele é par ou ímpar.

numero = int(input("\nDigite um número: "))

if(numero % 2 == 0):
    print(f"\n{numero} é par.")
else:
    print(f"\n{numero} é ímpar.")