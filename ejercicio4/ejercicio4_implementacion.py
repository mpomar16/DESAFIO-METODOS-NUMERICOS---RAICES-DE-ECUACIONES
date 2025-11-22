import math

def f(x):
    return math.cos(x)**2 - 0.5 * x * math.exp(0.3 * x) + 5.0

def df(x):
    return -2.0 * math.cos(x) * math.sin(x) - 0.5 * math.exp(0.3 * x) * (1.0 + 0.3 * x)

def biseccion(f, a, b, tol=0.0001, max_iter=100):
    table = []
    for n in range(max_iter + 1):
        fa = f(a)
        fb = f(b)
        m = (a + b) / 2.0
        fm = f(m)
        table.append((n, a, b, m, fa, fb, fm))
        if abs(fm) <= tol:
            break
        if fa * fm < 0.0:
            b = m
        else:
            a = m
    return table

def newton(f, df, x0, tol=0.0001, max_iter=100):
    table = []
    x = x0
    for n in range(max_iter + 1):
        fx = f(x)
        dfx = df(x)
        table.append((n, x, fx, dfx))
        if abs(fx) <= tol:
            break
        x = x - fx / dfx
    return table

def secante(f, x0, x1, tol=0.0001, max_iter=100):
    table = []
    x_previo = x0
    x_actual = x1
    table.append((0, x_previo, f(x_previo)))
    table.append((1, x_actual, f(x_actual)))
    for n in range(2, max_iter + 1):
        f_previo = f(x_previo)
        f_actual = f(x_actual)
        if f_actual - f_previo == 0.0:
            break
        x_sig = x_actual - f_actual * (x_actual - x_previo) / (f_actual - f_previo)
        fx_sig = f(x_sig)
        table.append((n, x_sig, fx_sig))
        if abs(fx_sig) <= tol:
            break
        x_previo, x_actual = x_actual, x_sig
    return table

def biseccion_tabla(label, table):
    print("------------------------------------------------------------")
    print("Biseccion - " + label)
    print("n        a           b           m           f(a)           f(b)           f(m)")
    for n, a, b, m, fa, fb, fm in table:
        print(f"{n:2d} {a:12.9f} {b:12.9f} {m:12.9f} {fa:14.9f} {fb:14.9f} {fm:14.9f}")
    print()

def newton_tabla(label, table):
    print("------------------------------------------------------------")
    print("Newton - " + label)
    print("n        x           f(x)        f'_(x)")
    for n, x, fx, dfx in table:
        print(f"{n:2d} {x:12.9f} {fx:12.9f} {dfx:12.9f}")
    print()

def secante_tabla(label, table):
    print("------------------------------------------------------------")
    print("Secante - " + label)
    print("n        x           f(x)")
    for n, x, fx in table:
        print(f"{n:2d} {x:12.9f} {fx:14.9f}")
    print()

def error_rel_porcentual(approx, exacto):
    return abs(approx - exacto) / abs(exacto) * 100.0

def main():
    tol = 0.0001
    x_exacto = 3.7256021765

    bis_x = biseccion(f, 3.0, 4.0, tol)
    new_x = newton(f, df, 3.5, tol)
    sec_x = secante(f, 3.0, 4.0, tol)

    biseccion_tabla("raiz x", bis_x)
    newton_tabla("raiz x", new_x)
    secante_tabla("raiz x", sec_x)

    raiz_bis_x = bis_x[-1][3]
    raiz_new_x = new_x[-1][1]
    raiz_sec_x = sec_x[-1][1]

    print("Raiz exacta:")
    print(f" x = {x_exacto:.10f}")
    print()
    print("Raiz aproximada por metodo:")
    print(f"Biseccion: x = {raiz_bis_x:.10f}")
    print(f"Newton   : x = {raiz_new_x:.10f}")
    print(f"Secante  : x = {raiz_sec_x:.10f}")
    print()
    print("Error relativo porcentual por metodo:")
    print(f"Biseccion: x = {error_rel_porcentual(raiz_bis_x, x_exacto):.10e} %")
    print(f"Newton   : x = {error_rel_porcentual(raiz_new_x, x_exacto):.10e} %")
    print(f"Secante  : x = {error_rel_porcentual(raiz_sec_x, x_exacto):.10e} %")

if __name__ == "__main__":
    main()