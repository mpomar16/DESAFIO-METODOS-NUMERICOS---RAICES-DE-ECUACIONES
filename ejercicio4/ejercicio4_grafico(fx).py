import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.cos(x)**2 - 0.5 * x * math.exp(0.3 * x) + 5.0
    
def main():

    xs_fun = np.linspace(0.0, 8.0, 400)
    ys_fun = [f(x) for x in xs_fun]

    plt.figure()
    plt.plot(xs_fun, ys_fun, label="Curva de la funcion f(x)")
    plt.plot(xs_fun, [0.0] * len(xs_fun), label="Eje x (f(x)=0)")
    plt.xlabel("Variable independiente x")
    plt.ylabel("Valor de la funcion f(x)")
    plt.title("Funcion f(x) = cos^2(x) - 0.5 x e^{0.3 x} + 5")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
