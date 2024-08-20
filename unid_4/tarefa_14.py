# aula 26
# PREDITOR-CORRETOR 4ª ORDEM

#inicialização
#range-kutta de quarta ordem

#predição
#Yn+1 = Yn + h/24 (55fn - 59fn-1 + 37fn-2 - 9fn-3)
#Y4 = Y3 + h/24 (55f3 - 59f2 + 37f1 - 9f0) 

#f0 vêm de x0 e y0 (condições iniciais)
#f1 vêm de x1 e y1 (range-kutta de quarta ordem)

#correção


def runge_kutta_4(t0, v0, y0, k, m, g, delta_t):
    # Cálculo dos valores iniciais utilizando Runge-Kutta de 4ª ordem
    k1_v = delta_t * (-g - (k/m) * v0)
    k1_y = delta_t * v0

    k2_v = delta_t * (-g - (k/m) * (v0 + 0.5 * k1_v))
    k2_y = delta_t * (v0 + 0.5 * k1_y)

    k3_v = delta_t * (-g - (k/m) * (v0 + 0.5 * k2_v))
    k3_y = delta_t * (v0 + 0.5 * k2_y)

    k4_v = delta_t * (-g - (k/m) * (v0 + k3_v))
    k4_y = delta_t * (v0 + k3_y)

    s1_v = v0 + (1/6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)
    s1_y = y0 + (1/6) * (k1_y + 2*k2_y + 2*k3_y + k4_y)

    return s1_v, s1_y

def preditor_corretor_4(t0, v0, y0, k, m, g, delta_t):
    s0 = [v0, y0]
    y = y0
    t = t0
    v = 0
    
    # Inicializar com Runge-Kutta de 4ª ordem
    s1_v, s1_y = runge_kutta_4(t0, v0, y0, k, m, g, delta_t)
    s2_v, s2_y = runge_kutta_4(t0 + delta_t, s1_v, s1_y, k, m, g, delta_t)
    s3_v, s3_y = runge_kutta_4(t0 + 2 * delta_t, s2_v, s2_y, k, m, g, delta_t)

    v_vals = [v0, s1_v, s2_v, s3_v]
    y_vals = [y0, s1_y, s2_y, s3_y]

    t = t0 + 3 * delta_t

    while s3_y >= 0:
        # Passo de predição - Adams-Bashforth de 4ª ordem
        v_pred = v_vals[-1] + (delta_t/24) * (55*(-g-(k/m)*v_vals[-1]) - 59*(-g-(k/m)*v_vals[-2]) + 37*(-g-(k/m)*v_vals[-3]) - 9*(-g-(k/m)*v_vals[-4]))
        y_pred = y_vals[-1] + (delta_t/24) * (55*v_vals[-1] - 59*v_vals[-2] + 37*v_vals[-3] - 9*v_vals[-4])

        # Passo de correção - Adams-Moulton de 4ª ordem
        v_corr = v_vals[-1] + (delta_t/24) * (-9*(-g-(k/m)*v_pred) + 19*(-g-(k/m)*v_vals[-1]) - 5*(-g-(k/m)*v_vals[-2]) + (-g-(k/m)*v_vals[-3]))
        y_corr = y_vals[-1] + (delta_t/24) * (-9*v_pred + 19*v_vals[-1] - 5*v_vals[-2] + v_vals[-3])

        # Atualizar os valores
        v_vals = v_vals[1:] + [v_corr]
        y_vals = y_vals[1:] + [y_corr]
        
        t += delta_t
        s3_y = y_corr

        if y_corr > y:
            y = y_corr
            t_max = t

    print("deltaT = ", delta_t, " segundos")
    print("altura maxima = ", y, " metros")
    print("tempo maximo = ", t_max, " segundos")
    print("tempo total = ", t-delta_t, " segundos")
    print("velocidade final = ", abs(v_vals[-1]), " m/s")
    print("\n")


if __name__ == "__main__":
    t_0 = 0     # tempo inicial
    v_0 = 5     # velocidade inicial
    y_0 = 200   # altitude inicial
    k = 0.25    # constante de aerodinâmica
    m = 2       # massa do objeto
    g = 10      # gravidade

    delta_ts = [0.1, 0.01, 0.001, 0.0001]

    for dt in delta_ts:
        preditor_corretor_4(t_0, v_0, y_0, k, m, g, dt)