# Escreva um programa que solicite ao usuário dois números e exiba a soma, a subtração, a multiplicação e a divisão dos dois números.

# Função que soma
def Soma(n1, n2):
    resultado = n1 + n2;
    print(f"\nA soma entre {n1} e {n2} é igual a: {resultado}.");

# Função que subtrai
def Subtracao(n1, n2):
    resultado = n1 - n2;
    print(f"\nA subtração entre {n1} e {n2} é igual a: {resultado}.");

# Função que multiplica
def Multiplicacao(n1, n2):
    resultado = n1 * n2;
    print(f"\nA multiplicação entre {n1} e {n2} é igual a: {resultado}.");

# Função que divide
def Divisao(n1, n2):
    resultado = n1 / n2;
    print(f"\nA divisão entre {n1} e {n2} é igual a: {resultado}.");

# Entrada de dados
entrada1 = int(input("\nDigite um número: "));
entrada2 = int(input("Digite outro número: "));

# Chamada das funções
Soma(entrada1, entrada2);
Subtracao(entrada1, entrada2);
Multiplicacao(entrada1, entrada2);
Divisao(entrada1, entrada2);


