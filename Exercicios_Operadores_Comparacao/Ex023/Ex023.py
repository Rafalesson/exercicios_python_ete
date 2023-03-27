# Escreva um programa que solicite ao usuário sua idade e exiba se ele é maior de idade ou não (considerando a maioridade como 18 anos).

idade = int(input("\nDigita a idade: "))

if(idade >= 18):
    print(f"\n{idade} anos é considerado maior de idade.")
else:
    print(f"\n{idade} anos é considerado menor de idade.")