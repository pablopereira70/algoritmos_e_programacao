# 📦 Variáveis e Tipos de Dados

Antes de tudo, é importante saber o que é uma variável. Em programação, pense numa variável como uma **caixa de correio com uma etiqueta** onde você pode guardar um valor. Você pode colocar um número, uma palavra ou até mesmo uma frase dentro dessa caixa. E o melhor de tudo é que você pode mudar o que está dentro dela sempre que quiser!

## 💻 Exemplo Prático
```python
# Criamos uma caixa chamada "caixa_de_correio" e guardamos a frase "Olá, mundo!"
caixa_de_correio = "Olá, mundo!"

# Agora, mudamos o conteúdo da mesma caixa para o número 42
caixa_de_correio = 42

# O sinal de igual (=) é o operador de ATRIBUIÇÃO. 
# Ele pega o valor do lado direito e o guarda na variável do lado esquerdo.
```

## 🚫 Regras para Nomear Variáveis

Para o Python entender o nome da sua "caixa", existem 5 regras obrigatórias:

1. **Deve começar** com uma letra ou um sublinhado (`_`).
2. **Pode conter** letras, números e sublinhados, mas **nunca** espaços ou caracteres especiais (como `@`, `$`, `!`).
3. **Não pode** ser uma palavra reservada da linguagem (como `if`, `for`, `while`, etc.).
4. **Não pode** começar com números.
5. **Evite** o uso de letras acentuadas (como `ç`, `á`, `õ`) para manter a compatibilidade do código.

> 💡 **Dica de Portfólio:** Em Python, o padrão de boas práticas para nomear variáveis é o **snake_case**, onde separamos as palavras por sublinhados (ex: `limite_credito`, `nome_usuario`).

## 🏷️ Tipos de Dados Comuns

Lembra que cada caixa de correio tem uma etiqueta indicando o tipo de conteúdo? No Python, não precisamos declarar isso manualmente (chamamos isso de **tipagem dinâmica**), pois ele identifica o tipo do valor automaticamente. Os quatro tipos primitivos mais comuns são:

```python
int   # Números inteiros -> ex: 1, -5, 1024
float # Números decimais (ponto flutuante) -> ex: 3.14, -0.5, 2.0
str   # Texto (strings) -> sempre entre aspas ex: "Olá", 'Mundo'
bool  # Valores booleanos (lógicos) -> apenas True = 1 ou False = 0
```

Revisando: uma variável precisa de um nome válido para ser identificada e um valor que pode ser de diferentes tipos (`int`, `float`, `str`, `bool`, etc.). O mais importante é que o valor de uma variável pode ser alterado durante a execução do programa.

---

⬅️ [Voltar para o Sumário do Módulo](./readme.md) | [Próximo Tópico: 02. Operadores Matemáticos e Lógicos](./02_operadores.md) ➡️