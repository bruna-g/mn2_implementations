# dada uma função, um ponto, uma filosofia,
# a ordem de 1 a 4 e um delta, calcular a
# derivada da função

import math

def derivada_filos_forward(f, x, ordem, delta):
  if ordem == 1:
    return (f(x + delta) - f(x))/delta
  elif ordem == 2:
    return (-3*f(x) + 4*f(x + delta) - f(x + 2*delta))/(2*delta)
  elif ordem == 3:
    return (2*f(x) - 9*f(x + delta) + 18*f(x + 2*delta) - 11*f(x + 3*delta))/(6*delta)
  elif ordem == 4:
    return (-25*f(x) + 48*f(x + delta) - 36*f(x + 2*delta) + 16*f(x + 3*delta) - 3*f(x + 4*delta))/(12*delta)
  else:
    raise ValueError("Ordem não suportada")

def derivada_filos_backward(f, x, ordem, delta):
  if ordem == 1:
    return (f(x) - f(x - delta))/delta
  elif ordem == 2:
    return (3*f(x) - 4*f(x - delta) + f(x - 2*delta))/(2*delta)
  elif ordem == 3:
    return (-2*f(x) + 9*f(x - delta) - 18*f(x - 2*delta) + 11*f(x - 3*delta))/(6*delta)
  elif ordem == 4:
    return (25*f(x) - 48*f(x - delta) + 36*f(x - 2*delta) - 16*f(x - 3*delta) + 3*f(x - 4*delta))/(12*delta)
  else:
    raise ValueError("Ordem não suportada")

def derivada_filos_central(f, x, ordem, delta):
  if ordem == 1:
    return (f(x + delta) - f(x - delta))/(2*delta)
  elif ordem == 2:
    return (f(x - delta) - 2*f(x) + f(x + delta))/(delta**2)
  elif ordem == 3:
    return (f(x - 2*delta) - 2*f(x - delta) + 2*f(x + delta) - f(x + 2*delta))/(2*delta**3)
  elif ordem == 4:
    return (f(x - 2*delta) - 4*f(x - delta) + 6*f(x) - 4*f(x + delta) + f(x + 2*delta))/(delta**4)
  else:
    raise ValueError("Ordem não suportada")
  
if __name__ == "__main__":
  pi = math.pi

  x = 4
  f = lambda x: x**2
  # f = lambda x: 2 * x 
  # f = lambda x: math.sin(x)
  # f = lambda x: math.exp(x) # e^x

  ordem = 1
  delta = 0.001
  filosofia = "forward"
  
  if filosofia == "forward":
    result = derivada_filos_forward(f, x, ordem, delta)
    print("\nPela filosofia", filosofia, ", a derivada da função no ponto", x, "é:", result, "\n")

  elif filosofia == "backward":
    result = derivada_filos_backward(f, x, ordem, delta)
    print("\nPela filosofia", filosofia, ", a derivada da função no ponto", x, "é:", result, "\n")

  elif filosofia == "central":
    result = derivada_filos_central(f, x, ordem, delta)
    print("\nPela filosofia", filosofia, ", a derivada da função no ponto", x, "é:", result, "\n")
  
  else:
    print("Filosofia não suportada")

