import matplotlib.pyplot as plt, numpy as np
from timeit import default_timer as timer
#~ ======================================================================
def finiteDifference(Xk, Yk):
	Fcurr, F = Yk, [ Yk[0] ]
	k = 0
	while (1 < len(Fcurr)):
		Fsucc = []
		for i in range(len(Fcurr) - 1):
			_tmp = (Fcurr[i+1] - Fcurr[i]) / (Xk[i+k+1] - Xk[i])
			Fsucc.append(_tmp)
		F.append(Fsucc[0])
		Fcurr = Fsucc
		k += 1
	return F

def newtownBasis(Xk, x):
	N = [ 1 ]
	for i in range(1, len(Xk)):
		Ni = np.prod( x - Xk[0:i] )
		N.append(Ni)
	return N

def horner(Xk, Yk, F, x):
	N = newtownBasis(Xk, x)
	return np.dot(F, N)

#~ ======================================================================
#~ MAIN
Xk = [-2, 3, 7, 9, 10]
Yk = [4, 8, 1, 19, 11]

x0, x1 = np.min(Xk), np.max(Xk)
#~ x0, x1 = x0 - (x1 - x0) / 10, x1 + (x1 - x0) / 10, 
X = np.linspace(x0, x1, 10000) # 10 MILLE POINTS

start = timer()
F = finiteDifference(Xk, Yk)
Y = [horner(Xk, Yk, F, x) for x in X] # VERY SLOW 
stop = timer()
delta = stop - start
print(f'Elapsed time: {delta}')

plt.plot(Xk, Yk, 'ko', X, Y, 'r-')
plt.grid()
plt.show()
