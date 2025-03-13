import numpy as np

np.arange(1, 88, 1)

dado = np.loadtxt('apples_ts.csv',delimiter=',', usecols=np.arange(1, 88, 1))

dado.ndim
dado.size
dado.shape

dado_transposto = dado.T

print(dado_transposto)
