import numpy as np
import matplotlib.pyplot as plt

Vrest = -70e-3 #70 mV
R = 100e6 #100 Mohms
C = 100e-12 #100pf
I = .1e-9 #namp

#for any negative time, V = trest

startTime = -100e-3
endTime = 200e-3
increments = 300
t = np.linspace(startTime,endTime,increments)
v = np.zeros(increments,dtype=float)

#for restarting the time for each equation
endEachTime = (endTime-startTime)/3
print(int(increments/3))

tnew = np.linspace(0,endEachTime,int(increments/3))


for i in range(0,100):
  v[i] = Vrest

for i in range(100,200):
  v[i] = (R*I)*(1-np.exp(-tnew[i-100]/(R*C)))+Vrest

for i in range(200,300):
  v[i] = (R*I)*(np.exp(-tnew[i-200]/(R*C)))+Vrest


plt.plot(t,v)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.show()
