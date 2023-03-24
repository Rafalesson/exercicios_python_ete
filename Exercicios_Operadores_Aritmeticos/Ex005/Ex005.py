# Escreva um programa que solicite ao usuário a temperatura em graus Celsius e exiba a temperatura em graus Fahrenheit. (Dica: a fórmula para converter Celsius em Fahrenheit é F = C * 1,8 + 32)

def CelsiusParaFahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    print(f"\n{celsius}°C em Fahrenheit é igual a {fahrenheit}°F")

entrada = float(input("\nDigite a temperatura em Celsius: "))

CelsiusParaFahrenheit(entrada)

