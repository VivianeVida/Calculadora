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

# Solicita os dados do usuário
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
