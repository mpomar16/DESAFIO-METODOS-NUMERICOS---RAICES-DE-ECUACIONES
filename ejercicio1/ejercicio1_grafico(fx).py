import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - math.exp(0.8 * x) - 20.0
    
def main():
    xs_fun = np.linspace(0.0, 8.0, 400)
    ys_fun = [f(x) for x in xs_fun]
    plt.figure()
    line_fun, = plt.plot(xs_fun, ys_fun, label="Curva de la funcion f(x) en [0,8]")
    line_x, = plt.plot(xs_fun, [0.0] * len(xs_fun))
    plt.xlabel("Variable independiente x")
    plt.ylabel("Valor de la funcion f(x)")
    plt.title("Grafico de la funcion f(x) = x^3 - e^{0.8 x} - 20")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
