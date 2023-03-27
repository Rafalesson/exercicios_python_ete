# Escreva um programa que solicite ao usuário dois números e exiba se o primeiro número é maior, menor ou igual ao segundo número.

num1 = float(input("\nDigite um número: "))
num2 = float(input("Digite outro número: "))

if(num1 > num2):
    print(f"\n{num1} é maior que {num2}.")
elif(num1 == num2):
    print(f"\n{num1} é igual a {num2}.")
else:
    print(f"\n{num1} é menor que {num2}.")