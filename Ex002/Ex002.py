# Escreva um programa que solicite ao usuário um número e exiba seu dobro, triplo e quadrado.

# Função que dobra o valor
def Dobrar(valor):
    resultado = valor * 2;
    print(f"\nO dobro de {valor} é igual a: {resultado}.");

# Função que triplica o valor
def Triplicar(valor):
    resultado = valor * 3;
    print(f"\nO triplo de {valor} é igual a: {resultado}.");

# Função que quadruplica o valor
def Quadruplicar(valor):
    resultado = valor * 4;
    print(f"\nO quadrado de {valor} é igual a: {resultado}.");

# Entrada do dado
entrada = int(input("\nDigite um valor: "));

# Chamando as funções
Dobrar(entrada);
Triplicar(entrada);
Quadruplicar(entrada);

