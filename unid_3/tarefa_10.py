#aula_18
# POTENCIA REGULAR

from numpy import double
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *


def potenciaRegular(matA, vOld, E):
  lambdaNew = 0
  vNew = []
  vNew = vOld.copy()

  while True:
    lambdaOld = lambdaNew
    vOld = vNew.copy()
    x1Old = Normalizar(vOld)
    vNew = multVetorMatriz(x1Old, matA)
    lambdaNew = multVetorVetor(x1Old, vNew)
    if convergencia(lambdaOld, lambdaNew) < E:
      break
  return (lambdaNew, x1Old)

if __name__ == '__main__':
  matA = [[5.0, 2.0, 1.0], [2.0, 3.0, 1.0], [1.0, 1.0, 2.0]]
  vOld = [1.0, 1.0, 1.0]
  E = 0.000006
  (lambdaNew, x1Old) = potenciaRegular(matA, vOld, E)
  print(lambdaNew)
  print(x1Old)