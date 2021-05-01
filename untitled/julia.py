import numpy as np
import matplotlib.pyplot as plt
from cmath import *

N = 700# domaine spatial (600)
M = 100# arret termes suite (100)
P = 100# critere de convergence suite (1000)
C = -0.7#0.285 + 0.01j

X = np.linspace(-1.5, -1.3, N)
Y = np.linspace(-1.5, -1.3, N)

ensemble_julia = []
couleurs = []

def f(z):
    return cos(z) + 1/C

for i in range(N):
    for k in range(N):
        z_0 = X[i] + Y[k]*1j# point de l'ensemble a tester
        z_n = z_0
        p = 0
        while abs(z_n) < P and p < M:
            z_n = f(z_n)
            p += 1
        if abs(z_n) < P:# critere de convergence
            ensemble_julia.append(z_0)
        else:
            couleurs.append((z_0, p))

Xq = [i.real for i in ensemble_julia]
Yq = [i.imag for i in ensemble_julia]

Xc = [i[0].real for i in couleurs]
Yc = [i[0].imag for i in couleurs]
Xcouleurs = [i[1] for i in couleurs]

plt.scatter(Xq, Yq, c='k', s=2)
plt.scatter(Xc, Yc, c=Xcouleurs, cmap='gnuplot2', s=1)
plt.axis('equal')

plt.show()


