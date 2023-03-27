## Escreva um programa que solicite ao usuário dois números e exiba se o primeiro número é maior, menor ou igual ao segundo número.

### Explicando o código:
---

1. O programa inicia solicitando ao usuário que insira dois números usando a função `input()` e armazenando-os nas variáveis `num1` e `num2` após a conversão para um número real usando a função `float()`.
---

2. Em seguida, o programa compara os valores das duas variáveis usando a estrutura condicional `if-elif-else`.

    - Se `num1` for maior que `num2`, o programa imprimirá uma mensagem informando que `num1` é maior que `num2`.

    - Se `num1` for igual a `num2`, a condição `elif` será verdadeira. Nesse caso, o programa imprimirá uma mensagem indicando que `num1` é igual a `num2`.

    - Caso contrário, se `num1` for menor que `num2`, a condição else será verdadeira e o programa imprimirá uma mensagem informando que `num1` é menor que `num2`.