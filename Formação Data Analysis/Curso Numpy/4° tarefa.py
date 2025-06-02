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

x = datas

y = 2*x+80

#plt.plot(x,Moscow)
#plt.plot(x,y)

np.sqrt(np.sum(np.power(Moscow-y,2)))
        
np.linalg.norm(Moscow-y)

Y = Moscow
X= datas
n = np.size(Moscow)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2) - np.sum(X)**2)



b = np.mean(Y) - a*np.mean(X)

y= a*X+b

np.linalg.norm(Moscow-y)

#plt.plot(x,Moscow)
#plt.plot(x,y)

#plt.plot(41.5,41.5*a+b, '*r')
#plt.plot(100,100*a+b, '*r')

print(np.random.randint(low=40,high=100, size=100))

np.random.seed(84)

coef_angulares = np.random.uniform(low=0.10, high=0.90, size=100)

norma = np.array([])

for i in range(100):
    norma = np.append(norma,np.linalg.norm(Moscow-(coef_angulares[i]*X+b)))
dados = np.column_stack([norma,coef_angulares])
print(dados.shape)

np.savetxt('dados.csv', dados, delimiter=',')