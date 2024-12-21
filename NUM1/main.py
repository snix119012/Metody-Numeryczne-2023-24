import numpy as np
import matplotlib.pyplot as plt
import sys

def f_Float(x):
    return np.float32(np.sin(np.float32(x)**np.float32(2)))

def pochodna_Prawdziwa_Float(x):
    return np.float32(2) * np.float32(x) * np.float32(np.cos(np.float32(x)**np.float32(2)))

def f_Double(x):
    return np.float64(np.sin(np.float64(x)**np.float64(2)))

def pochodna_Prawdziwa_Double(x):
    return np.float64(2) * np.float64(x) * np.float64(np.cos(np.float64(x)**np.float64(2)))

def g_Float(x):
    return np.float32(2)*np.float32(np.cos(np.float32(x)**np.float32(2)))

def g_pochodna_Prawdziwa_Float(x):
    return np.float32(-4) * np.float32(x) * np.float32(np.sin(np.float32(x)**np.float32(2)))

def g_Double(x):
    return np.float64(2) * np.float64(np.cos(np.float64(x) ** np.float64(2)))

def g_pochodna_Prawdziwa_Double(x):
    return np.float64(-4) * np.float64(x) * np.float64(np.sin(np.float64(x) ** np.float64(2)))


def pochodna_Centralna(x, h, f):
    return (f(x + h) - f(x - h)) / (2 * h)

def pochodna_Przod(x, h, f):
    return (f(x + h) - f(x)) / h

def obliczanie_bledu(prawdziwa_Wartosc, przyblizona_Wartosc):
    return np.abs(prawdziwa_Wartosc - przyblizona_Wartosc)


def main():
    x_Wartosc = 0.2
    h_WartoscF = np.logspace(-7, 0, 250)
    h_WartoscD = np.logspace(-16, 0, 250)

    # f(x)
    float_BledyC = [
        obliczanie_bledu(pochodna_Prawdziwa_Float(x_Wartosc), pochodna_Centralna(x_Wartosc, np.float32(h), f_Float))
        for h in h_WartoscF
    ]
    float_BledyP = [
        obliczanie_bledu(pochodna_Prawdziwa_Float(x_Wartosc), pochodna_Przod(x_Wartosc, np.float32(h), f_Float))
        for h in h_WartoscF
    ]

    double_BledyP = [
        obliczanie_bledu(pochodna_Prawdziwa_Double(x_Wartosc), pochodna_Przod(x_Wartosc, np.float64(h),f_Double))
        for h in h_WartoscD
    ]
    double_BledyC = [
        obliczanie_bledu(pochodna_Prawdziwa_Double(x_Wartosc), pochodna_Centralna(x_Wartosc, np.float64(h), f_Double))
        for h in h_WartoscD
    ]

    #g(x)
    g_float_BledyC = [
        obliczanie_bledu(g_pochodna_Prawdziwa_Float(x_Wartosc), pochodna_Centralna(x_Wartosc, np.float32(h), g_Float))
        for h in h_WartoscF
    ]
    g_float_BledyP = [
        obliczanie_bledu(g_pochodna_Prawdziwa_Float(x_Wartosc), pochodna_Przod(x_Wartosc, np.float32(h), g_Float))
        for h in h_WartoscF
    ]

    g_double_BledyP = [
        obliczanie_bledu(g_pochodna_Prawdziwa_Double(x_Wartosc), pochodna_Przod(x_Wartosc, np.float64(h), g_Double))
        for h in h_WartoscD
    ]
    g_double_BledyC = [
        obliczanie_bledu(g_pochodna_Prawdziwa_Double(x_Wartosc), pochodna_Centralna(x_Wartosc, np.float64(h), g_Double))
        for h in h_WartoscD
    ]
    if len(sys.argv)>1:
        arg = sys.argv[1]
        if arg == '1':
            print("Wykres dla funkcji sinus(x^2) i zmiennej float")
            plt.figure(figsize=(10, 6))
            plt.title('sin(x^2)')
            plt.loglog(h_WartoscF, float_BledyC, label='Float-Centralna')
            plt.loglog(h_WartoscF, float_BledyP, label='Float-Przednia')
            plt.xlabel('h')
            plt.ylabel('|Dhf(x) - f\'(x)|')
            plt.legend()
            plt.show()
        elif arg == '2':
            print("Wykres dla funkcji sinus(x^2) i zmiennej double")
            plt.figure(figsize=(10, 6))
            plt.title('sin(x^2)')
            plt.loglog(h_WartoscD, double_BledyC, label='Double-Centralna')
            plt.loglog(h_WartoscD, double_BledyP, label='Double-Przednia')
            plt.xlabel('h')
            plt.ylabel('|Dhf(x) - f\'(x)|')
            plt.legend()
            plt.show()
        elif arg == '3':
            print("Wykres dla funkcji 2cosinus(x^2) zmiennej float")
            plt.figure(figsize=(10, 6))
            plt.title('2*cos(x^2)')
            plt.loglog(h_WartoscF, g_float_BledyC, label='Float-Centralna')
            plt.loglog(h_WartoscF, g_float_BledyP, label='Float-Przednia')
            plt.xlabel('h')
            plt.ylabel('|Dhf(x) - g\'(x)|')
            plt.legend()
            plt.show()
        elif arg == '4':
            print("Wykres dla funkcji 2cosinus(x^2) zmiennej double")
            plt.figure(figsize=(10, 6))
            plt.title('2*cos(x^2)')
            plt.loglog(h_WartoscD, g_double_BledyC, label='Double-Centralna')
            plt.loglog(h_WartoscD, g_double_BledyP, label='Double-Przednia')
            plt.xlabel('h')
            plt.ylabel('|Dhf(x) - g\'(x)|')
            plt.legend()
            plt.show()
        else:
            print("Podana zle zmienna")

if __name__ == "__main__":
    main()
