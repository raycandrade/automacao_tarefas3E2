'''
Exercício 4
----------------------------------------------------------------------
Imprimindo um único caractere * por vez e utilizando a estrutura
de repetição for, crie um programa que imrpima no console o texto
abaixo:
*
**
***
****
*****
******
''' 
# Função para realizar as operações matemáticas com base no operador
def calcular_operacao(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
        return f"O resultado da soma é {resultado}"
    elif operador == '-':
        resultado = num1 - num2
        return f"O resultado da subtração é {resultado}"
    elif operador == '*':
        resultado = num1 * num2
        return f"O resultado da multiplicação é {resultado}"
    elif operador == '/':
        # Verifica se o segundo número não é zero antes de fazer a divisão
        if num2 != 0:
            resultado = num1 / num2
            return f"O resultado da divisão é {resultado}"
        else:
            return "Não é possível dividir por zero."
    else:
        return f"Operador '{operador}' não reconhecido. Por favor, insira um operador válido (+, -, *, /)."

# Função para receber números reais e operador do usuário
def obter_entrada():
    try:
        num1 = float(input("Digite o primeiro número real: "))
        num2 = float(input("Digite o segundo número real: "))
        operador = input("Digite o operador matemático (+, -, *, /): ")
        return num1, num2, operador
    except ValueError:
        print("Por favor, insira números reais válidos.")
        return obter_entrada()

# Programa principal
if __name__ == "__main__":
    continuar = True

    while continuar:
        # Obtém os números e operador do usuário
        numero1, numero2, operador = obter_entrada()

        # Calcula a operação e exibe o resultado
        resultado = calcular_operacao(numero1, numero2, operador)
        print(resultado)

        # Pergunta ao usuário se deseja continuar
        resposta = input("Deseja continuar calculando? (S/N): ").upper()
        if resposta != 'S':
            continuar = False

    # Imprime o padrão desejado utilizando a estrutura de repetição for
    for i in range(1, 7):
        print('*' * i)
