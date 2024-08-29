import math
'''
Anna Beatriz Vieira Sousa: 538758
Bruna Gomes Carneiro - 537993
'''

#todas as funções x_pontos implementam Gauss Legendre com a qtde x de pontos

def dois_pontos(a, b, epsilon):
    r = math.sqrt(1/3)
    raizes = [-r, r]
    w = 1
    pesos = [1, 1]
    return integracao(2, pesos, raizes, epsilon, a, b)

def tres_pontos(a, b, epsilon):
    r = math.sqrt(3/5)
    raizes = [-r, 0, r]
    pesos = [5/9, 8/9, 5/9]
    return integracao(3, pesos, raizes, epsilon, a, b)

def quatro_pontos(a, b, epsilon):
    r1 = math.sqrt((15 + 2*math.sqrt(30))/35)
    r2 = math.sqrt((15 - 2*math.sqrt(30))/35)
    raizes = [r1, -r1, r2, -r2]
    p1 = 0.347856
    p2 = 0.65214
    pesos = [p1, p1, p2, p2]
    return integracao(4, pesos, raizes, epsilon, a, b)
    
def f(x):
    return (math.sin(2*x) + 4*x**2 + 3*x)**2

def x(sk, xi, xf):
    x = (xi + xf) / 2 + ((xf - xi) / 2) * sk
    return x

def integracao(n_pontos, pesos, raizes, epsilon, a, b):
    xi = 0
    xf = 0
    erro = 0
    resultado = 0
    aux = 0 
    N = 1
    while True:
        resultado_anterior = resultado
        aux = resultado
        resultado = 0
        iteracoes = 0        
        delta = (b - a) / N
        for i in range(N):
            xi = a + i*delta
            xf = xi + delta
            somatorio = 0
            for j in range(n_pontos):
                somatorio += (pesos[j] * f(x(raizes[j], xi, xf)))
            resultado  += ((xf - xi) / 2) * somatorio
            iteracoes += 1
        N = N*2
        resultado_anterior = aux
        erro = abs((resultado_anterior - resultado)/2)
     
        if (erro < epsilon): 
            break
    
    return iteracoes, resultado

a = 0 
b = 1
erro = 10**(-6)

while True:
    entrada = input("Deseja obter o resultado para Gauss Legendre com quandos pontos? ([s]Sair): ")
    if entrada == '2':
        iteracoes, resultado = dois_pontos(a, b, erro)
        print("Iterações: ", iteracoes, "\nResultado: ", resultado)
    elif entrada == '3':
        iteracoes, resultado = tres_pontos(a, b, erro)
        print("Iterações: ", iteracoes, "\nResultado: ", resultado)
    elif entrada == '4':
        iteracoes, resultado = quatro_pontos(a, b, erro)
        print("Iterações: ", iteracoes, "\nResultado: ", resultado)
    elif entrada == 's':
        break
    else:
        print("Resposta inválida, tente novamente")
    