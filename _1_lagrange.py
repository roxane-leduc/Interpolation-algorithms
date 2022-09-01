import matplotlib.pyplot as plt, numpy as np

#~ ======================================================================
def lagrangePolynomial(Xk, i, x):
	num, den = 1, 1
	for j in range(len(Xk)):
		if (i != j):
			num *= (x - Xk[j])
			den *= (Xk[i] - Xk[j])
	return num / den

def lagrangeBasis(Xk, x):
	return [lagrangePolynomial(Xk, i, x) for i in range(len(Xk))]
	
def lagrangeInterpolation(Xk, Yk, x):
	L = lagrangeBasis(Xk, x)
	Px = np.dot(Yk, L)
	return Px

#~ ======================================================================
#~ MAIN
Xk = [-2, 3, 7, 9, 10]
Yk = [4, 8, 1, 19, 11]

x0, x1 = np.min(Xk), np.max(Xk)
X = np.linspace(x0, x1, 20) # MILLE POINTS

interp = lambda x: lagrangeInterpolation(Xk, Yk, x)

# Y = [lagrangeInterpolation(Xk, Yk, x) for x in X] # VERY SLOW 
Y = interp(X)

plt.plot(Xk, Yk, 'ko', X, Y, 'r-')
plt.grid()
plt.show()
