import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x**2 * math.exp(-0.5 * x) - 3.0 * x + 1.0
    
def main():

    xs_fun = np.linspace(-3.0, 3.0, 400)
    ys_fun = [f(x) for x in xs_fun]

    plt.figure()
    plt.plot(xs_fun, ys_fun, label="Curva de la funcion f(x) en [-3,3]")
    plt.plot(xs_fun, [0.0] * len(xs_fun), label="Eje x (f(x)=0)")
    plt.xlabel("Variable independiente x")
    plt.ylabel("Valor de la funcion f(x)")
    plt.title("Funcion f(x) = x^3 - x^2 e^{-0.5 x} - 3 x + 1")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
