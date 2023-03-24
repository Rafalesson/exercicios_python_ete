# Escreva um programa que declare duas variáveis inteiras e atribua a elas valores diferentes. Em seguida, atribua o valor da primeira variável à segunda variável e exiba o valor das duas variáveis.

entrada1 = int(input("\nDigite um número inteiro: "))
entrada2 = int(input("Digite outro número inteiro: "))

valor_original = entrada2
entrada2 = entrada1

print(f"\nPrimeira entrada: {entrada1}")
print(f"Segunda entrada: {valor_original}")
print(f"Valor atribuído: {entrada2}")