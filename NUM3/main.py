import time
import matplotlib.pyplot as plt
import sys
def obliczenia_dla_N(n):
            arr1 = [0 if i == 0 else 0.2 for i in range(n)]
            arr2 = [1.2] * n
            arr3 = [0.1 / (i + 1) if i > 0 and i < n - 1 else 0 for i in range(n)]
            arr4 = [0.15 / ((i + 1) ** 2) if i > 0 and i < n - 1 else 0 for i in range(n)]
            arr3[0]=0.1
            arr4[0]=0.15
            arr4[n-2]=0
            arr_2D = [arr1, arr2, arr3, arr4]
            global x
            x = list(range(1, n + 1))
            #rozbicie na LU
            for i in range(1, n - 2):
                if arr_2D[1][i-1]==0:
                    print("/0 ERROR")
                    break
                arr_2D[0][i] = arr_2D[0][i] / arr_2D[1][i - 1]
                arr_2D[1][i] = arr_2D[1][i] - arr_2D[0][i] * arr_2D[2][i - 1]
                arr_2D[2][i] = arr_2D[2][i] - arr_2D[0][i] * arr_2D[3][i - 1]

            arr_2D[0][n - 2] = arr_2D[0][n - 2] / arr_2D[1][n - 3]
            arr_2D[1][n - 2] = arr_2D[1][n - 2] - arr_2D[0][n - 2] * arr_2D[2][n - 3]
            arr_2D[2][n - 2] = arr_2D[2][n - 2] - arr_2D[0][n - 2] * arr_2D[3][n - 3]

            arr_2D[0][n - 1] = arr_2D[0][n - 1] / arr_2D[1][n - 2]
            arr_2D[1][n - 1] = arr_2D[1][n - 1] - arr_2D[0][n - 1] * arr_2D[2][n - 2]
            #obliczanie wyznacznika macierzy
            global w
            w=1
            for i in range(n):
                w = arr_2D[1][i] * w
            i=1
            #wyliczanie naszego rozwiazania
            for i in range(1,n):
                x[i] = (x[i] - arr_2D[0][i] * x[i-1])
            for i in range(n-3, -1, -1):
                x[i] = (x[i]-(arr_2D[2][i]*x[i+1])-(arr_2D[3][i]*x[i+2]))/ arr_2D[1][i]
            x[n-1]=x[n-1]/arr_2D[1][n-1]
            x[n-2]=(x[n-2]-(arr_2D[2][n-2]*x[n-1])) / arr_2D[1][n-1]
def wykres(proby):
    w_czasu = [0] * len(N_wartosci)
    for i in range(len(N_wartosci)):
        for j in range(proby):
            start = time.time()
            obliczenia_dla_N(N_wartosci[i])
            koniec = time.time()-start
            w_czasu[i] += koniec
        w_czasu[i] /=proby
    plt.plot(N_wartosci, w_czasu)
    plt.xlabel('N')
    plt.ylabel('Czas wykonania (s)')
    plt.title('Zależność czasu od N')
    plt.show()
n=124
if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == '1':
        obliczenia_dla_N(n)
        print("Wyznacznik macierzy wynosi: ", w)
        print(" ")
        print("Wynik to ")
        for i in range(n):
            print(x[i])
    elif arg == '2':
         N_wartosci = list(range(124, 1500))
         wykres(30)
    else:
        print("Podana zle zmienna")

