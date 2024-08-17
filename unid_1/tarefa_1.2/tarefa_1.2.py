 # 1) Suavize a imagem, aplicando um filtro Gaussiano
 # 2) Na imagem do passo 1, aplique o filtro convolucional de Gradiente 
 # 2.1) um filtro de Sobel para a derivada na direção x, gerando uma imagem/matriz, A, com os valores da derivada em cada pixel/elemento da matriz;
 # 2.2) um filtro de Sobel para a derivada na direção y, gerando uma imagens/matriz, B, com os valores da derivada em cada pixel/elemento da matriz;
 # 2.3) em cada uma das matrizes, A e B, eleve ao quadrado os valores dos elementos;
 # 2.4) some as duas matrizes A e B modificadas no passo 2.3 e tire a raiz quadrada  de cada elemento dessa matriz, C
 # 3) Escolha um valor (float)  para threshold e 
 # 4) gere uma matriz Final, D, com 
 # >>>>> pixel 0 caso o pixel correspondente da matriz C seja menor do que o threshold
 # >>>>> pixel 1. caso o pixel correspondente da matriz C seja maior do que o threshold.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(img, kernel_size, sigma):
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = kernel * kernel.T
    img = cv2.filter2D(img, -1, kernel)
    return img

def sobel_filter(img):
    # Aplicar Sobel em x
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    # Aplicar Sobel em y
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    return sobel_x, sobel_y

def threshold_image(img, threshold):
    _, thresholded_img = cv2.threshold(img, threshold, 1, cv2.THRESH_BINARY)
    return thresholded_img

def gradient_magnitude(sobel_x, sobel_y):
    return np.sqrt(sobel_x + sobel_y)

def apply_threshold(gradient, threshold):
    return np.where(gradient < threshold, 0, 1)


# Exemplo de como usar as funções definidas
if __name__ == "__main__":
    # Correção: Definir img_path como uma string contendo o caminho do arquivo
    img_path = 'D:\\ESTUDO\\MET_NUM_2\\mn2_implementations\\mn2_implementations\\tarefa_1.2\\gato.jpg'
    # Carrega a imagem em escala de cinza diretamente
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)    
    img_suavizada = gaussian_filter(img, 5, 1)
    sobel_x, sobel_y = sobel_filter(img_suavizada)  # Assumindo que sobel_filter retorna uma tupla (sobel_x, sobel_y)
    gradiente = gradient_magnitude(sobel_x, sobel_y)
    resultado_final = apply_threshold(gradiente, 500)  # Exemplo de threshold

    plt.imshow(resultado_final, cmap='gray')
    plt.show()