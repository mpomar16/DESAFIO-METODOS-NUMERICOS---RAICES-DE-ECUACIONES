import math

def f(x):
    return x**3 - math.exp(0.8 * x) - 20.0

def df(x):
    return 3.0 * x**2 - 0.8 * math.exp(0.8 * x)

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
    x1_exacto = 3.208219802
    x2_exacto = 7.48983873

    bis_x1 = biseccion(f, 3.0, 4.0, tol)
    bis_x2 = biseccion(f, 7.0, 8.0, tol)
    new_x1 = newton(f, df, 3.5, tol)
    new_x2 = newton(f, df, 7.5, tol)
    sec_x1 = secante(f, 3.0, 4.0, tol)
    sec_x2 = secante(f, 7.0, 8.0, tol)

    biseccion_tabla("raiz x1", bis_x1)
    biseccion_tabla("raiz x2", bis_x2)

    newton_tabla("raiz x1", new_x1)
    newton_tabla("raiz x2", new_x2)

    secante_tabla("raiz x1", sec_x1)
    secante_tabla("raiz x2", sec_x2)

    raiz_bis_x1 = bis_x1[-1][3]
    raiz_bis_x2 = bis_x2[-1][3]
    raiz_new_x1 = new_x1[-1][1]
    raiz_new_x2 = new_x2[-1][1]
    raiz_sec_x1 = sec_x1[-1][1]
    raiz_sec_x2 = sec_x2[-1][1]

    print("Approximate roots for each method:")
    print(f"Bisection: x1 = {raiz_bis_x1:.10f}, x2 = {raiz_bis_x2:.10f}")
    print(f"Newton   : x1 = {raiz_new_x1:.10f}, x2 = {raiz_new_x2:.10f}")
    print(f"Secant   : x1 = {raiz_sec_x1:.10f}, x2 = {raiz_sec_x2:.10f}")
    print()

    print("Relative error percent with respect to exact roots:")
    print(f"Bisection: x1 = {error_rel_porcentual(raiz_bis_x1, x1_exacto):.10e} %, x2 = {error_rel_porcentual(raiz_bis_x2, x2_exacto):.10e} %")
    print(f"Newton   : x1 = {error_rel_porcentual(raiz_new_x1, x1_exacto):.10e} %, x2 = {error_rel_porcentual(raiz_new_x2, x2_exacto):.10e} %")
    print(f"Secant   : x1 = {error_rel_porcentual(raiz_sec_x1, x1_exacto):.10e} %, x2 = {error_rel_porcentual(raiz_sec_x2, x2_exacto):.10e} %")

if __name__ == "__main__":
    main()