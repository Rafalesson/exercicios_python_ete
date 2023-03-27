#  Escreva um programa que solicite ao usuário um número e exiba se ele é positivo, negativo ou igual a zero.

numero = int(input("\nDigite um número: "))

if(numero > 0):
    print(f"\n{numero} é positivo.")
elif(numero < 0):
    print(f"\n{numero} é negativo.")
else:
    print(f"\n{numero} é zero.")