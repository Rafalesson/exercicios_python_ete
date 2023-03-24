# Escreva um programa que solicite ao usuário o valor de um empréstimo, a taxa de juros mensal e o número de meses do empréstimo, e exiba o valor total a ser pago (incluindo juros).

valor_emprestimo = float(input("\nInforme o valor do empréstimo: "))
taxa_juros_decimal = float(input("Informe a taxa de juros mensal (%): ")) / 100
num_meses = int(input("Informe o número de meses do empréstimo: "))

# juro simples
juros_acumulados = valor_emprestimo * taxa_juros_decimal * num_meses
valor_total = valor_emprestimo + juros_acumulados

# juro composto
# fator_crescimento = (1 + taxa_juros_decimal) ** num_meses
# valor_total = valor_emprestimo * fator_crescimento

print(f"\nValor do empréstimo: {valor_emprestimo:.2f}")
print(f"Valor do juro simples: {juros_acumulados:.2f}")
# print(f"Valor do juro composto: {fator_crescimento * valor_emprestimo - valor_emprestimo:.2f}")
print(f"Valor toral a ser pago: {valor_total:.2f}")