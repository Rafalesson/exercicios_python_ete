## Escreva um programa que solicite ao usuário uma letra e exiba se ela é uma vogal ou uma consoante.

### Explicando o código:
---

1. Primeiramente, o programa solicita ao usuário que digite uma letra, armazenando o valor em uma variável chamada `letra`. 
2. Em seguida, uma lista chamada `vogais` é criada contendo todas as vogais (tanto minúsculas quanto maiúsculas).
3. O if seguinte verifica se a letra digitada pelo usuário está presente na lista de vogais utilizando o operador in. 
    - Se a letra estiver presente na lista, o programa informa que ela é uma vogal: `'{letra}' é vogal'`.
    - Caso contrário, o programa informa que a `letra` é uma consoante: `'{letra}' é consoante'`.