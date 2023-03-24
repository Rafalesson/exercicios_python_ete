# Escreva um programa que declare duas variáveis inteiras e atribua a elas valores diferentes. Em seguida, multiplique o valor da primeira variável pelo valor da segunda variável e atribua o resultado à primeira variável. Exiba o valor das duas variáveis.

valor1 = 5
valor2 = 3

valor1_original = valor1
valor1 = valor1 * valor2

print(f"\nPrimeiro valor: {valor1_original}")
print(f"Segundo valor: {valor2}")
print(f"Valor final: {valor1}")