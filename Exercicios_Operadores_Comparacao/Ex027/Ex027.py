# Escreva um programa que solicite ao usuário uma letra e exiba se ela é uma vogal ou uma consoante.

letra = input("\nDigite uma letra: ")
vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

if letra in vogais:
    print(f"\n'{letra}' é vogal.")
else:
    print(f"\n'{letra}' é consoante.")