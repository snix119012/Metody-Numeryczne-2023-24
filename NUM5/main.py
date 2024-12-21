import numpy as np
import matplotlib.pyplot as plt
import copy
import random

def wykres1():
    plt.grid(True)
    plt.xlabel('n')
    plt.ylabel("$log|x(n) - x(ostatni)|$")
    plt.yscale('log')
    plt.plot([i for i in range(1, len(w1) + 1)], w1)
    plt.plot([i for i in range(1, len(w2) + 1)], w2)
    plt.legend(['Jacobi','Gauss'])
    plt.title('Porównanie metod w losowym wektorze x')
    plt.show()
def wykres2():
    plt.grid(True)
    plt.xlabel('n')
    plt.ylabel("$log|x(n) - x(ostatni)|$")
    plt.yscale('log')
    plt.plot([i for i in range(1, len(w1) + 1)], w1)
    plt.plot([i for i in range(1, len(w2) + 1)], w2)
    plt.legend(['Jacobi','Gauss'])
    plt.title('Porównanie metod w stałym wektorze x=[10,10,10..]')
    plt.show()
def wykres3():
    plt.grid(True)
    plt.xlabel('n')
    plt.ylabel("$log|x(n) - x(ostatni)|$")
    plt.yscale('log')
    plt.plot([i for i in range(1, len(w1) + 1)], w1)
    plt.plot([i for i in range(1, len(w2) + 1)], w2)
    plt.legend(['Jacobi','Gauss'])
    plt.title('Porównanie metod w stałym wektorze x=[1,1,1..]')
    plt.show()
def gauss(x, n,rozw):
    his_iteracji = []
    norma1 = 0
    licznik = 500
    while licznik:
        y = x.copy()
        for i in range(n):
            if i == 0:
                x[i] = (b[i] - x[i + 1] - 0.15 * x[i + 2]) / 3
            elif i == 1:
                x[i] = (b[i] - x[i - 1] - x[i + 1] - 0.15 * x[i + 2]) / 3
            elif i == n - 2:
                x[i] = (b[i] - x[i - 1] - 0.15 * x[i - 2] - x[i + 1]) / 3
            elif i == n - 1:
                x[i] = (b[i] - x[i - 1] - 0.15 * x[i - 2]) / 3
            else:
                x[i] = (b[i] - x[i - 1] - 0.15 * x[i - 2] - x[i + 1] - 0.15 * x[i + 2]) / 3

        norma2 = np.sqrt(sum(map(lambda a, b: (a - b) ** 2, x, y)))
        his_iteracji.append(copy.deepcopy(x))
        if abs(norma1 - norma2) < 10 ** (-12):
            break
        norma1 = norma2
        licznik = licznik - 1
    if rozw==1:
     print(x)


    return his_iteracji

def jacobi(x, n,rozw):
    his_iteracji = []
    norma1 = 0
    licznik = 500
    while licznik:
        y = x.copy()
        for i in range(n):
            if i == 0:
                x[i] = (b[i] - x[i + 1] - 0.15 * x[i + 2]) / 3
            elif i == 1:
                x[i] = (b[i] - y[i - 1] - x[i + 1] - 0.15 * x[i + 2]) / 3
            elif i == n - 2:
                x[i] = (b[i] - y[i - 1] - 0.15 * y[i - 2] - x[i + 1]) / 3
            elif i == n - 1:
                x[i] = (b[i] - y[i - 1] - 0.15 * y[i - 2]) / 3
            else:
                x[i] = (b[i] - y[i - 1] - 0.15 * y[i - 2] - x[i + 1] - 0.15 * x[i + 2]) / 3
        norma2 = np.sqrt(sum(map(lambda a, b: (a - b) ** 2, x, y)))
        his_iteracji.append(copy.deepcopy(x))
        if abs(norma1 - norma2) < 10 ** (-12):
            break
        norma1 = norma2
        licznik = licznik - 1

    if rozw == 1:
        print(x)
    return his_iteracji


licznik = 500
x = random.sample(range(500), 124)
b = list(range(1, 125))

print("Wynik otrzymany metodą Jacobiego:")
his_iteracji_Jacobi = jacobi(x.copy(), 124,1)
print("\nWynik otrzymany metodą Gaussa:")
his_iteracji_Gauss = gauss(x.copy(), 124,1)
w1 = []
last1 = his_iteracji_Jacobi[-1]
for i in range(len(his_iteracji_Jacobi) - 1):
    w1.append(np.sqrt(sum(map(lambda a, b: (a - b) ** 2, his_iteracji_Jacobi[i], last1))))

w2 = []
last2 = his_iteracji_Gauss[-1]
for i in range(len(his_iteracji_Gauss) - 1):
    w2.append(np.sqrt(sum(map(lambda a, b: (a - b) ** 2, his_iteracji_Gauss[i], last2))))

wykres1()
n = 124
x2 = [10] * n
his_iteracji_Jacobi = jacobi(x2.copy(), 124,0)
his_iteracji_Gauss = gauss(x2.copy(), 124,0)
w1 = []
last1 = his_iteracji_Jacobi[-1]
for i in range(len(his_iteracji_Jacobi) - 1):
    w1.append(np.sqrt(sum(map(lambda a, b: (a - b) ** 2, his_iteracji_Jacobi[i], last1))))

w2 = []
last2 = his_iteracji_Gauss[-1]
for i in range(len(his_iteracji_Gauss) - 1):
    w2.append(np.sqrt(sum(map(lambda a, b: (a - b) ** 2, his_iteracji_Gauss[i], last2))))

wykres2()
n = 124
x3 = [1] * n
his_iteracji_Jacobi = jacobi(x3.copy(), 124,0)
his_iteracji_Gauss = gauss(x3.copy(), 124,0)
w1 = []
last1 = his_iteracji_Jacobi[-1]
for i in range(len(his_iteracji_Jacobi) - 1):
    w1.append(np.sqrt(sum(map(lambda a, b: (a - b) ** 2, his_iteracji_Jacobi[i], last1))))

w2 = []
last2 = his_iteracji_Gauss[-1]
for i in range(len(his_iteracji_Gauss) - 1):
    w2.append(np.sqrt(sum(map(lambda a, b: (a - b) ** 2, his_iteracji_Gauss[i], last2))))

wykres3()