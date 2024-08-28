#polinômio de interpolação de grau 1, que interpola 2 pontos aplica a regra do trapézio aberta
from math import sin

def f(x):
    return (sin(2*x) + 4*(x**2) + 3*x)**2

def grau1_aberta(a, b, f):
    h = (b - a)/3
    delta = 3*h/2
    return delta * (f(a + h) + f(a + 2*h))

#polinômio de interpolação de grau 2, que interpola 3 pontos aplica a regra de Milne aberta
def grau2_aberta(a, b, f):
    h = (b - a)/4
    delta = 4*h/3
    return delta * (2*f(a + h) - f(a + 2*h) + 2*f(a + 3*h))

#polinômio de interpolação de grau 3, que interpola 4 pontos
def grau3_aberta(a, b, f):
    h = (b - a)/5
    delta = 5*h/24
    return delta * (11*f(a + h) + f(a + 2*h) + f(a + 3*h) + 11*f(a + 4*h))

#polinômio de interpolação de grau 4, que interpola 5 pontos
def grau4_aberta(a, b, f):
    h = (b - a)/6
    delta = 3*h/10
    return delta * (11*f(a + h) - 14*f(a + 2*h) + 26*f(a + 3*h) - 14*f(a + 4*h) + 11*f(a + 5*h))


def newton_cotes(a, b, f, epsilon):
    resultado_anterior = 0
    resultado = 0
    iteracoes = 0
    N = 2
    while True:
        iteracoes += 1
        delta = (b-a)/N
        integral = 0
        for i in range(N):
            Xi = a + i*delta
            Xf = Xi + delta
            integral += grau2_aberta(Xi, Xf, f)
        N = N*2
        resultado_anterior = resultado
        resultado = integral
        erro = abs(resultado_anterior - resultado)
        
        if (erro < epsilon): 
            break

    return iteracoes, resultado

a = 0
b = 1
epsilon = 10**(-6)
iteracoes, teste = newton_cotes(a, b, f, epsilon)
print(iteracoes)
print(teste)