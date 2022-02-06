import matplotlib.pyplot as plt
from numpy import random
import math

print("")
print("-----------------------------------")
print("")
n = input("Paths =  ")
print("")
N = input("Number of Points on Each Path =  ")
print("")
s = input("Spot ($) =  ")
print("")
r = input("Risk-Free Rate (%) =  ")
print("")
de = input("Dividend Yield (%) =  ")
print("")
sig = input("Volatility (%) =  ")
print("")
T = input("Time to Expiry (Years) =  ")
print("")

n=int(n)
N=int(N)
s=float(s)
r=float(r)/100
de=float(de)/100
sig=float(sig)/100
T=float(T)
h = float(T/N)

rands = []

for i in range(0,n): #New Path
    path = [s]
    for j in range(1,N): #Time Iteration
        z=random.standard_normal()
        if z>=8:
            print(str(i)+" "+str(j)+" "+"z = "+str(z))
        si = path[j-1] * math.exp((r-de-0.5*sig**2)*h + sig*(h**0.5)*z)
        path.append(si)
    rands.append(path)

x = [h*k for k in range(0,N)]

for path in rands:
    plt.plot(x,path)

plt.title("Monte Carlo Simulation")
plt.xlabel("Time (Years)")
plt.ylabel("Price ($)")

plt.show()
