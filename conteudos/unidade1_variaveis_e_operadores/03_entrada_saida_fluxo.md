# 📥 Entrada e Saída de Dados (I/O)

Em Python, podemos usar a função `input()` para obter entrada do usuário e a função `print()` para exibir saída na tela.

* **`input()`:** Abre o prompt para o usuário digitar algo. **Importante:** Tudo o que entra pelo `input()` chega no Python como formato de texto (`str`). Se precisar de números para realizar cálculos, deve-se fazer a conversão explícita de tipo (ex: `int()` ou `float()`).
* **`print()`:** É usada para exibir informações na tela. Podemos passar múltiplos argumentos ou usar strings formatadas (**f-strings**) para incluir variáveis no texto de forma elegante.

## 💻 Exemplo Prático

```python
# Coletando os dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) # Convertendo o texto digitado para número inteiro

# Exibindo os dados usando f-string (forma moderna e limpa)
print(f"Olá, {nome}! Você tem {idade} anos de idade.")

```

Esse programa pede ao usuário para digitar seu nome e sua idade, converte a idade para um número inteiro e, em seguida, exibe uma saudação personalizada utilizando uma f-string.

Você não deve ter percebido mas acabou de presenciar um **algoritmo**. Afinal o que é um algoritmo? De forma bem simples é uma sequência de passos finitos para resolver um problema.

No nosso dia a dia, nós seguimos algoritmos o tempo todo sem perceber:
* 🎂 **Uma receita de bolo:** Tem os ingredientes (entradas), as instruções passo a passo (processamento) e o bolo pronto (saída).
* 🗺️ **O GPS/Waze:** Recebe sua localização atual e o destino, calcula o trajeto curva por curva e te leva até lá.

Em programação, o algoritmo é a **lógica** por trás da solução. O Python é apenas a ferramenta (a linguagem) que usamos para traduzir essa lógica de um jeito que o computador consiga entender e executar.

## 🧱 Os Três Pilares de um Algoritmo
Todo programa de computador segue este fluxo básico:

1. **Entrada (Input):** Os dados que o programa precisa para começar (ex: o usuário digitando algo).
2. **Processamento:** O que o programa faz com esses dados (ex: cálculos matemáticos, comparações).
3. **Saída (Output):** O resultado final entregue ao usuário (ex: um texto ou valor na tela).

---

⬅️ [Tópico anterior: 02. Operadores Matemáticos e Lógicos](./02_operadores.md) | [Voltar para o Sumário do Módulo](./readme.md) ➡️