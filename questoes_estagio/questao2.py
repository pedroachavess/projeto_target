def verificacaoFibonacci(numero):
    fibonacci = [0, 1]
    
    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

mensagem = verificacaoFibonacci(numero)
print(mensagem)