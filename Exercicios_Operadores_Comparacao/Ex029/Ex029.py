# Escreva um programa que solicite ao usuário um número e exiba se ele é múltiplo de 3 e/ou de 5.

numero = int(input("\nDigite um número: "))

if(numero % 3 == 0 and numero % 5 == 0):
    print(f"\n'{numero}' é múltiplo de 3 e 5.")

elif(numero % 5 == 0):
    print(f"\n'{numero}' é múltiplo de 5.")

elif(numero % 3 == 0):
    print(f"\n'{numero}' é múltiplo de 3.")

else:
    print(f"\n'{numero}' não é múltiplo de 3 nem de 5.")