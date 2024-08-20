# aula 25
# METODO RANGE-KUTTA 3ª ORDEM 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *

def runge_kutta(t0, v0, y0, k, m, g, delta_t):
  s0 = [v0, y0]
  y = y0
  t = t0
  v = 0

  while (s0[1] >= 0):
    v_1_2 = v0 + (delta_t/2)*(-g -(k/m * v0))
    y_1_2 = y0 + (delta_t/2)*v0

    v1 = v0 + delta_t*(-g -(k/m * v0))
    y1 = y0 + delta_t*v0

    F_s0_t0 = [-g-(k/m * v0), v0]
    F_s1_2_t1_2 = [-g-(k/m * v_1_2), v_1_2]
    F_s1_t1 = [-g-(k/m * v1), v1]

    s1 = [0, 0]
    s1[0] = s0[0] + delta_t * ((1/6)*F_s0_t0[0] + (4/6)*F_s1_2_t1_2[0] + (1/6)*F_s1_t1[0])
    s1[1] = s0[1] + delta_t * ((1/6)*F_s0_t0[1] + (4/6)*F_s1_2_t1_2[1] + (1/6)*F_s1_t1[1])

    t0 = t0 + delta_t
    v = v0
    v0 = s1[0]
    y0 = s1[1]
    s0[0] = s1[0]
    s0[1] = s1[1]

    if y0 > y:
      y = y0
      t = t0
  
  print("deltaT = ", delta_t, " segundos")
  print("altura maxima = ", y, " metros")
  print("tempo maximo = ", t, " segundos")
  print("tempo total = ", t0-delta_t, " segundos")
  print("velocidade final = ", abs(v), " m/s")
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
    runge_kutta(t_0, v_0, y_0, k, m, g, dt)
