# Calculadora
Esta é uma simples calculadora em Python que realiza operações básicas de adição, subtração, multiplicação e divisão.

## Função calculadora

 ## Python 3.x
```python
def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
    else:
        return 0
 ## Parâmetros
num1 (float): O primeiro número para a operação.
num2 (float): O segundo número para a operação.
operacao (int): O código da operação a ser realizada.
1 para soma
2 para subtração
3 para multiplicação
4 para divisão

## Retorno
O resultado da operação, ou uma mensagem de erro em caso de divisão por zero.
## Uso
O script solicita ao usuário que insira dois números e escolha uma operação. Em seguida, ele exibe o resultado da operação escolhida.

## Exemplo de Uso

```python
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    operacao = int(input("Digite o número da operação desejada: "))
    resultado = calculadora(num1, num2, operacao)
    print(f"O resultado da operação é: {resultado}")

except ValueError:
    print("Entrada inválida! Por favor, insira números válidos.")

## Tratamento de Erros
O script trata erros de entrada inválida, solicitando que o usuário insira números válidos.



