# Escreva um programa que solicite ao usuário sua altura e exiba se ele é considerado baixo, médio ou alto (levando em consideração as médias de altura para a sua idade e sexo).

class Pessoa:
    def __init__ (self, nome, sexo, altura):
        self.nome = nome
        self.sexo = sexo
        self.altura = altura

nome = input("\nDigite seu nome: ")
sexo = input("Digite seu sexo (M ou F ou O): ")
altura = float(input("Digite sua altura: "))

homem_alto = 1.81
homem_medio = 1.80
homem_baixo = 1.69

mulher_alta = 1.71
mulher_media = 1.70
mulher_baixa = 1.59

pessoa1 = Pessoa(nome, sexo, altura)

if(pessoa1.sexo == "M" or pessoa1.sexo == "m"):
    if(pessoa1.altura >= homem_alto):
        print(f"\nOlá, {pessoa1.nome}, você tem {pessoa1.altura} de altura. És um homem alto.")

    elif(pessoa1.altura < homem_alto and pessoa1.altura > homem_baixo):
        print(f"\nOlá, {pessoa1.nome}, você tem {pessoa1.altura} de altura. És um homem de estura média.")

    else:
        print(f"\nOlá, {pessoa1.nome}, você tem {pessoa1.altura} de altura. És um homem baixo.")

elif(pessoa1.sexo == 'F' or pessoa1.sexo == 'f'):
    if(pessoa1.altura >= mulher_alta):
        print(f"\nOlá, {pessoa1.nome}, você tem {pessoa1.altura} de altura. És uma mulher alta.")

    elif(pessoa1.altura < mulher_alta and pessoa1.altura > mulher_baixa):
        print(f"\nOlá, {pessoa1.nome}, você tem {pessoa1.altura} de altura. És uma mulher de estura média.")

    else:
        print(f"\nOlá, {pessoa1.nome}, você tem {pessoa1.altura} de altura. És uma mulher baixa.")
