# Escreva um programa que solicite ao usuário a largura e a altura de um retângulo e exiba sua área e perímetro.

def Retangulo(largura, altura):
    area = largura * altura
    perimetro = 2 * (largura + altura)
    print(f"\nA área do retângulo é {area} e o perímetro é {perimetro}.")
    
largura = float(input("\nDigite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

Retangulo(largura, altura)