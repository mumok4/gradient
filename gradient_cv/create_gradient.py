import numpy as np
import matplotlib.pyplot as plt

def generate_gradient(shape=(100, 100)):
    """
    Генерирует градиентный массив.
    
    :param shape: Размерность массива (по умолчанию (100, 100)).
    :return: Градиентный массив.
    """
    gradient = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            gradient[i, j] = i + j
    return gradient

def show_gradient(gradient):
    """
    Отображает градиентный массив с помощью matplotlib.
    
    :param gradient: Градиентный массив.
    """
    plt.imshow(gradient)
    plt.show()