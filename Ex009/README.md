## Escreva um programa que solicite ao usuário o valor de um empréstimo, a taxa de juros mensal e o número de meses do empréstimo, e exiba o valor total a ser pago (incluindo juros).

### Explicando o código:

---

Primeiro, o programa solicita ao usuário para inserir o ***valor do empréstimo***, a ***taxa de juros*** mensal (em percentual) e o número de ***meses do empréstimo***.

---

Depois disso, o programa calcula o valor dos juros acumulados com base no valor do empréstimo, taxa de juros e número de meses usando a fórmula de juros simples:  <center> <kbd><font color="green"> **juros_acumulados = valor_emprestimo** * **taxa_juros_decimal** * **num_meses** </font></kbd> </center> 

---

Em seguida, o programa calcula o valor total a ser pago (incluindo juros) adicionando os juros acumulados ao valor do empréstimo original: <center> <kbd ><font color="green"> **valor_total = valor_emprestimo + juros_acumulados** </font></kbd></center>

---

Finalmente, o programa imprime na tela o **valor do empréstimo original**, o **valor dos juros acumulados** usando juros simples e o **valor total a ser pago**.

---

O código também inclui um trecho comentado que mostra como calcular o valor total usando juros compostos. Basta descomentar esse trecho e comentar a linha que calcula o valor total usando juros simples. Juros compostos são calculados usando a fórmula:   <center> <kbd><font color="green"> **fator_crescimento = (1 + taxa_juros_decimal) ** num_meses** </font></kbd>  <br> e <br> <kbd><font color="green"> **valor_total = valor_emprestimo * fator_crescimento** </font></kbd> </center>  

<!-- Barra de progresso <progress value="50" max="100"> </progress> -->






