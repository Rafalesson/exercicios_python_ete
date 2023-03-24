# Escreva um programa que solicite ao usuário o raio de um círculo e exiba sua área e circunferência. (Dica: use a constante pi, que é aproximadamente igual a 3,14)
import math

raio = float(input("\nDigite o raio do círculo: "))
area = math.pi * raio**2
circunferencia = 2 * math.pi * raio

print(f"\nA área do círculo é: {area:.2f}")
print(f"A circunferência do círculo é: {circunferencia:.2f}")