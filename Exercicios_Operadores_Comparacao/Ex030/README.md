## Escreva um programa que solicite ao usuário um número e exiba se ele é primo ou não (um número é primo se é divisível apenas por 1 e por ele mesmo).

### Explicando o código:
---

1. O programa começa com a definição de uma função chamada `ehPrimo()`, que recebe um argumento `numero`.

2. Dentro da função, o primeiro teste condicional é para verificar se o número recebido é igual a 2. Se for, o programa imprime que o número é primo e retorna.

3. Caso o número não seja igual a 2, o próximo teste condicional verifica se o número é maior do que 1. Se for, o programa entra em um loop `for`.

4. O loop `for` começa com um `range` que vai de 2 até o número recebido menos 1.

5. Dentro do loop, o programa verifica se o número é divisível por cada um dos valores no range. Se o número for divisível por algum deles, o programa imprime que o número não é primo e sai do loop usando a instrução `break`.

6. Se o número não for divisível por nenhum dos valores no range, o programa imprime que o número é primo e sai do loop usando a instrução `break`.

7. Se o número recebido não for maior do que 1, o programa imprime que o número não é primo.

8. Em seguida, o programa solicita ao usuário um número e passa esse número como argumento para a função `ehPrimo()`.

9. A função `ehPrimo()` verifica se o número recebido é primo e imprime o resultado correspondente.