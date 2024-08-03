import math

def Normalizar(vOld):
  total = 0.0
  x1 = vOld.copy()
  for l in range(len(vOld)):
    total = total + vOld[l]**2.0
  denominador = math.sqrt(total)

  for m in range(len(vOld)):
    x1[m] = vOld[m] / denominador

  return x1

if __name__ == "__main__":
  mat = [1, 2, 3]
  print(Normalizar(mat))