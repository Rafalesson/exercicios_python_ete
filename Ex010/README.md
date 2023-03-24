## Escreva um programa que solicite ao usuário a nota de três provas e exiba a média aritmética das notas.

### <center> Explicando o código: </center>

---

- A primeira linha declara uma variável `nota1` e usa a função `input()` para exibir uma mensagem solicitando que o usuário digite a primeira nota. A função `float()` é usada para converter o valor digitado em um número decimal e o valor é armazenado na variável `nota1`.

---

- As próximas duas linhas são semelhantes, exceto que solicitam ao usuário as notas 2 e 3 e armazenam os valores digitados nas variáveis `nota2` e `nota3`.

---

- A próxima linha calcula a média aritmética das três notas, somando as três variáveis `nota1`, `nota2` e `nota3`, e dividindo a soma por 3. O resultado é armazenado na variável `media`.

---

- Por fim, a última linha usa a função `print()` para exibir a média aritmética calculada para o usuário, formatando o resultado com 2 casas decimais usando a expressão `{media:.2f}` na string de formatação.