## Escreva um programa que solicite ao usuário sua altura e exiba se ele é considerado baixo, médio ou alto (levando em consideração as médias de altura para a sua idade e sexo).

### Explicando o código:
---

- O programa começa definindo uma classe `Pessoa` que tem três atributos: `nome`, `sexo` e `altura`. Em seguida, pede-se ao usuário que digite seu `nome`, `sexo` e `altura` por meio de entradas de `input()`.

---

- Depois disso, o programa tem seis variáveis ​​que representam as médias de altura para homens e mulheres em três categorias diferentes: baixa, média e alta.

---

- Em seguida, o programa cria uma instância da classe `Pessoa` com os valores que o usuário digitou e, em seguida, usa uma série de declarações condicionais `if-else` para determinar em qual das três categorias a altura do usuário se enquadra.

---

- Se o usuário é um homem, o programa verifica se sua altura é maior ou igual à altura de um homem alto, se estiver, a mensagem `Você é um homem alto` será exibida. Se sua altura estiver entre as alturas de um homem alto e baixo, a mensagem `Você é um homem de estatura média` será exibida. Se sua altura for menor ou igual a altura de um homem baixo, a mensagem `Você é um homem baixo` será exibida.

---

- Se o usuário é uma mulher, o programa verifica as mesmas condições de altura para mulheres.

---

- Finalmente, o programa exibe uma mensagem para o usuário com base em sua `altura` e `sexo`, que informa se ele é considerado baixo, médio ou alto, de acordo com as médias de altura para sua idade e sexo.