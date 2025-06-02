import numpy as np
import matplotlib.pyplot as plt

np.arange(1, 88, 1)

dado = np.loadtxt('apples_ts.csv',delimiter=',', usecols=np.arange(1, 88, 1))

dado.ndim
dado.size
dado.shape

dado_transposto = dado.T

datas = dado_transposto[:,0]

precos = dado_transposto[:,1:6]

datas = np.arange(1,88,1)

#plt.plot(datas,precos[:,0])

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

Moscow_ano1 = Moscow[0:12] 
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

#plt.plot(np.arange(1,13,1),Moscow_ano1)
#plt.plot(np.arange(1,13,1),Moscow_ano2)
#plt.plot(np.arange(1,13,1),Moscow_ano3)
#plt.plot(np.arange(1,13,1),Moscow_ano4)

np.array_equal(Moscow_ano3,Moscow_ano4)

#plt.plot(datas, Kaliningrad)

np.isnan(Kaliningrad)

sum(np.isnan(Kaliningrad))

(Kaliningrad[3]+Kaliningrad[5])/2

Kaliningrad[4] = np.mean((Kaliningrad[3],Kaliningrad[5]))

np.mean(Moscow)

np.mean(Kaliningrad)

plt.plot(datas, Kaliningrad)
plt.plot(datas, Moscow)

plt.show()