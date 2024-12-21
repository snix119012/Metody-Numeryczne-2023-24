import numpy as np
import matplotlib.pyplot as plt
import time
import sys
n=80
def check(n):
    A = np.ones((n, n))
    A += np.diag([11]*n)
    A += np.diag([7]*(n - 1), 1)
    b = np.ones(n) * 5
    start = time.time()
    np.linalg.solve(A, b)
    return time.time()-start

def sherman(n,test):
    arr1 = [11]*n
    arr2 = [7]*(n-1) + [0]
    arr_ = [arr1,arr2]
    b = [5] * n
    start = time.time()
    z = [0] * n
    x = [0] * n
    z[n - 1] = b[n - 1] / arr_[0][n - 1]
    x[n - 1] = 1 / arr_[0][n - 1]

    for i in range(n - 2, -1, -1):
        z[i] = (b[n - 2] - arr_[1][i] * z[i + 1]) / arr_[0][i]
        x[i] = (1 - arr_[1][i] * x[i + 1]) / arr_[0][i]

    delta = sum(z) / (1 + sum(x))

    # Wyliczenie wyniku
    y = []
    for i in range(len(z)):
        y.append(z[i] - x[i] * delta)
    koniec = time.time()
    czas = koniec - start
    if(test==1):
        return czas
    if(test==0):
         return y


n_w = list(range(2, 81))
proby = 50
w_czasu = [0] * len(n_w)
total_time=0
w_czasu2 = [0] * len(n_w)
total_time2=0
for i in range(len(n_w)):
    for _ in range(proby):
        total_time += sherman(n,1)
    avg_time = total_time / proby
    w_czasu[i] = avg_time

for i in range(len(n_w)):
    for _ in range(proby):
        total_time2 += check(n)
    avg_time2 = total_time2 / proby
    w_czasu2[i] = avg_time2
def wykres1():
 plt.plot(n_w, w_czasu)
 plt.plot(n_w, w_czasu2)
 plt.xlabel('N')
 plt.ylabel('Czas wykoania (s)')
 plt.title('Zależność czasu dla algorytmów własnego oraz wyliczanego przez numpy ')
 plt.legend(['Zależność czasu dla zaimplementowanego algorytmu','Zależność czasu dla biblioteki Numpy' ])
 plt.show()
def wykres2():
 plt.plot(n_w, w_czasu)
 plt.xlabel('N')
 plt.ylabel('Czas wykoania (s)')
 plt.title('Zależność czasu dla własnego algorytmu')
 plt.show()

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == '1':
        print("Wynik to ", sherman(80,0))
    elif arg == '2':
         wykres2()
    elif arg == '3':
         wykres1()
    else:
        print("zły numer")

