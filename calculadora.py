num1 = float(input("Digite um número: "))
num2 = float(input("Digite o segundo número: "))
calculo = input("Digite a operação (+ , -, *, /): ")

if calculo == "+":
    resultado = num1 + num2
    print("O resultado é:" ,resultado)
elif calculo == "-":
    resultado = num1 - num2
    print("O resultado é:" ,resultado)
elif calculo == "*":
    resultado = num1 * num2
    print("O resultado é:" ,resultado)
elif calculo == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("O resultado é:", resultado)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")