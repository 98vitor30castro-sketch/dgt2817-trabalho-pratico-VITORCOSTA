saida = ""

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if a == 0 or b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora(num1, num2, operacao):
    op = operacao.lower().strip()

    if op == "+" or op == "adicao" or op == "adição":
        resultado = adicao(num1, num2)
    elif op == "-" or op == "subracao" or op == "subtracao" or op == "subtração":
        resultado = subracao(num1, num2)
    elif op == "*" or op == "multiplicacao" or op == "multiplicação":
        resultado = multiplicacao(num1, num2)
    elif op == "/" or op == "divisao" or op == "divisão":
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"

    return resultado

while saida.lower() != "n":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou nome): ")

    resultado = calculadora(num1, num2, operacao)
    print("Resultado da operação: " + str(resultado))

    saida = input("Deseja continuar? (S/N): ")