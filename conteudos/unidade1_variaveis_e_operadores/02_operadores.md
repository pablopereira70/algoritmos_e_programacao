# 🧮 Operadores Aritméticos

São os símbolos que usamos para realizar operações matemáticas. Veja a tabela abaixo:

| Operador | Descrição | Exemplo | Resultado |
| :---: | :--- | :---: | :---: |
| `+` | Adição | `2 + 3` | `5` |
| `-` | Subtração | `5 - 2` | `3` |
| `*` | Multiplicação | `2 * 3` | `6` |
| `/` | Divisão | `6 / 2` | `3.0` |
| `//` | Divisão Inteira | `7 // 2` | `3` |
| `%` | Módulo (Resto da divisão) | `7 % 2` | `1` |
| `**` | Exponenciação (Potência) | `2 ** 3` | `8` |

Faremos uso deles mais à frente, mas é importante já ter uma noção de como eles funcionam. Abaixo está uma breve explicação sobre os operadores de divisão inteira e módulo, pois eles podem ser um pouco confusos no começo.

## 🔍 Entendendo a Divisão Inteira e o Módulo

O segredo está em lembrar daquela divisão de chave da escola:

* **Divisão inteira (`//`):** Retorna apenas a parte inteira do resultado, descartando o que vem após a vírgula. Ex: `7 // 2` resulta em `3` (porque o 2 cabe 3 vezes inteiras dentro do 7).
* **Módulo (`%`):** Retorna o **resto** que sobrou dessa divisão. Ex: `7 % 2` resulta em `1` (já que 2 * 3 = 6, e para chegar em 7 falta 1).

---

# ⚖️ Operadores Relacionais

Os operadores relacionais são usados para realizar comparações entre valores. Eles retornam um valor booleano (`True` ou `False`) dependendo do resultado da comparação.

| Operador | Descrição | Exemplo | Resultado |
| :---: | :--- | :---: | :---: |
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Maior que | `5 > 3` | `True` |
| `<` | Menor que | `3 < 5` | `True` |
| `>=` | Maior ou igual a | `5 >= 5` | `True` |
| `<=` | Menor ou igual a | `3 <= 5` | `True` |

Esses operadores são muito úteis para tomar decisões em nossos programas. Por exemplo, podemos usar um operador relacional para verificar se um número é maior que outro e, com base nisso, executar um bloco de código específico.

> ⚠️ **Atenção:** Não confunda `=` (atribuição de valor) com `==` (comparação de igualdade)!

---

# 🧠 Operadores Lógicos

Os operadores lógicos são usados para combinar expressões booleanas. Eles também retornam um valor booleano (`True` ou `False`) dependendo do resultado da combinação.

| Operador | Descrição | Regra Prática | Exemplo |
| :---: | :--- | :--- | :---: |
| `and` | E lógico | Só retorna `True` se **todas** as condições forem verdadeiras. | `True and False` -> `False` |
| `or` | OU lógico | Retorna `True` se **pelo menos uma** condição for verdadeira. | `True or False` -> `True` |
| `not` | Negação | Inverte o estado lógico (o que é `True` vira `False` e vice-versa). | `not True` -> `False` |

Esses operadores são essenciais para criar condições mais complexas em nossos programas. Por exemplo, podemos usar o operador `and` para verificar se duas condições são verdadeiras ao mesmo tempo, ou o operador `or` para verificar se pelo menos uma condição é verdadeira.

---

⬅️ [Tópico Anterior: 01. Variáveis](./01_variaveis_e_tipos.md) | [Próximo Tópico: 03. Entrada e Saída](./03_entrada_saida_fluxo.md) ➡️