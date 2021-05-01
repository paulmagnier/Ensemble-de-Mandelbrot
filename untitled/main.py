import numpy as np
import matplotlib.pyplot as plt
from cmath import *

N = 600# domaine spatial (600)
M = 100# arret termes suite (100)
P = 100# critere de convergence suite (1000)

## REGIONS f(z, c) = z**2 + c
#X = np.linspace(-1.7, 0.8, N)
#Y = np.linspace(-1.2, 1.2, N)

#X = np.linspace(-1.5, -1.3, N)
#Y = np.linspace(-0.1, 0.1, N)

## REGIONS f(z, c) = cos(z) + 1/c
#X = np.linspace(-1.7, 0.8, N)
#Y = np.linspace(-1.2, 1.2, N)

X = np.linspace(-0.09, -0.07, N)
Y = np.linspace(0.345, 0.36, N)

ensemble_mandelbrot = []
couleurs = []

def f(z, c):
    return cos(z) + 1/c

for i in range(N):
    for k in range(N):
        c = X[i] + Y[k]*1j# point de l'ensemble a tester
        z_n = 0# suite
        p = 0
        while abs(z_n) < P and p < M:
            z_n = f(z_n, c)
            p += 1
        if abs(z_n) < P:# critere de convergence
            ensemble_mandelbrot.append(c)
        else:
            couleurs.append((c, p))

#print("ensemble : ( longueur ", len(ensemble_mandelbrot), ") ", ensemble_mandelbrot)

Xq = [i.real for i in ensemble_mandelbrot]
Yq = [i.imag for i in ensemble_mandelbrot]

Xc = [i[0].real for i in couleurs]
Yc = [i[0].imag for i in couleurs]
Xcouleurs = [i[1] for i in couleurs]

plt.scatter(Xq, Yq, c='k', s=2)
plt.scatter(Xc, Yc, c=Xcouleurs, cmap='gnuplot2', s=1)

plt.show()


