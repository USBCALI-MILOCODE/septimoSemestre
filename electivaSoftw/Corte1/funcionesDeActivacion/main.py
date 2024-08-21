import math
import matplotlib.pyplot as plt
import numpy as np

def funcionEscalon(x):
    if x >= 0:
        return 1
    else:
        return 0

def funcionSigmoide(x):
    return 1 / (1 + math.exp(-x))

def funcionTangenteHiperbolica(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

def funcionReLU(x):
    if x >= 0:
        return x
    else:
        return 0

def graficarFuncion(funcion, rango):
    x = np.linspace(-rango, rango, 100)
    y = [funcion(i) for i in x]

    plt.plot(x, y)
    plt.title(f"{funcion.__name__}")
    plt.show()

def main():
    graficarFuncion(funcionEscalon, 5)
    graficarFuncion(funcionSigmoide, 5)
    graficarFuncion(funcionTangenteHiperbolica, 5)
    graficarFuncion(funcionReLU, 5)

if __name__ == "__main__":
    main()
