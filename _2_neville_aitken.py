import matplotlib.pyplot as plt, numpy as np
from timeit import default_timer as timer
#~ ======================================================================
def schemaNevilleAitken(Xk, Yk, x):
	Tcurr = Yk
	k = 0
	while (1 < len(Tcurr)):
		Tsucc = []
		for i in range(len(Tcurr) - 1):
			_tmp = (Tcurr[i] * (Xk[i+k+1] - x) - Tcurr[i+1] * (Xk[i] - x)) / (Xk[i+k+1] - Xk[i])
			Tsucc.append(_tmp)
		Tcurr = Tsucc
		k += 1
	return Tcurr[0]

#~ ======================================================================
#~ MAIN
Xk = [-2, 3, 7, 9, 10]
Yk = [4, 8, 1, 19, 11]

x0, x1 = np.min(Xk), np.max(Xk)
x0, x1 = x0 - (x1 - x0) / 10, x1 + (x1 - x0) / 10, 
X = np.linspace(x0, x1, 10000) # 10 MILLE POINTS

start = timer()
Y = [schemaNevilleAitken(Xk, Yk, x) for x in X] # VERY SLOW 
stop = timer()
delta = stop - start
print(f'Elapsed time: {delta}')

plt.plot(Xk, Yk, 'ko', X, Y, 'r-')
plt.grid()
plt.show()
