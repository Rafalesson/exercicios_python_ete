#Escreva um programa que solicite ao usuário duas palavras e exiba se elas são iguais ou diferentes.

palavra1 = input("\nDigite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

if(palavra1 == palavra2):
    print(f"\n'{palavra1}' é igual a '{palavra2}'")
else:
    print(f"\n'{palavra1}' é diferente de '{palavra2}'")