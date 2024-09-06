*/Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.*/

def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número da operação: ")

        if opcao == '0':
            print("Saindo...")
            break
        elif opcao in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcao == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcao == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcao == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Essa opção não existe. Tente novamente.")

calculadora()
