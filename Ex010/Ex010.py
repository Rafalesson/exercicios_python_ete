# Escreva um programa que solicite ao usuário a nota de três provas e exiba a média aritmética das notas.

nota1 = float(input("\nDigite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média aritmética das notas: {media:.2f}")
