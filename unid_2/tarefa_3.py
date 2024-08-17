# Implemente as fórmulas Fechadas e Abertas da Aula#7 bem como as fórmulas que
# você desenvolveu para polinômios de substituição de grau 4 (Fechada e Aberta) e teste os
# resultados com tolerância de 10-6
# . O seu código (como já discutido em sala de aula)
# implementa a estratégia de partição do problema. Veja, em cada caso, quantas iterações
# foram necessárias até atingir a tolerância especificada.

#aula 8
# NEWTON-COTES ABERTA E FECHADA

import numpy as np

# Função para calcular as diferenças divididas
def divided_differences(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

    return coef[0, :]

# Função para construir o polinômio de Newton
def newton_polynomial(coef, x_data, x):
    n = len(coef)
    polynom = coef[0]
    for k in range(1, n):
        term = coef[k]
        for j in range(k):
            term = term * (x - x_data[j])
        polynom = polynom + term
    return polynom

# Função para integrar o polinômio de Newton
def integrate_newton_polynomial(coef, x_data, a, b):
    # Criar uma função anônima para o polinômio interpolador de Newton
    def polynomial(x):
        return newton_polynomial(coef, x_data, x)
    
    # Use uma integração numérica para integrar o polinômio interpolador no intervalo [a, b]
    from scipy.integrate import quad
    integral, _ = quad(polynomial, a, b)
    return integral

# Função principal que aplica a fórmula de Boole
def boole_rule_newton(f, a, b):
    h = (b - a) / 4
    x_data = np.array([a, a + h, a + 2*h, a + 3*h, b])
    y_data = np.array([f(x) for x in x_data])
    
    coef = divided_differences(x_data, y_data)
    integral = integrate_newton_polynomial(coef, x_data, a, b)
    
    return integral

# Exemplo de uso da função
if __name__ == "__main__":
    # Definindo a função a ser integrada
    def func(x):
        return (np.sin(2*x) + 4*x**2 + 3*x)**2

    # Definindo os limites de integração
    a = 0
    b = 1

    # Calculando a integral utilizando a fórmula de Boole desenvolvida através do polinômio de Newton
    result_boole = boole_rule_newton(func, a, b)
    print(f"Integral (Boole, desenvolvida com Polinômio de Newton): {result_boole}")
