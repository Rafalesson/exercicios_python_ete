# Escreva um programa que solicite ao usuário um número e exiba se ele é primo ou não (um número é primo se é divisível apenas por 1 e por ele mesmo).

def ehPrimo(numero):
    if numero == 2:
        print(f"\n{numero} é um número primo.")   
    elif numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                print(f"\n{numero} não é um número primo.")
                break
            else:
                print(f"\n{numero} é um número primo.")
                break
    else:
        print(f"\n{numero} não é um número primo.")

numero = int(input("\nDigite um número: "))

ehPrimo(numero)


