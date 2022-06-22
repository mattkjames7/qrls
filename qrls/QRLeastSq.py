import numpy as np
from .GramSchmidt import GramSchmidt


def QRLeastSq(x,y,deg):
	'''
	Use QR decomposition to perform least squares regression.
	
	Inputs
	======
	x : float
		x-coordinates
	y : float
		y-coordinates
	deg : int
		Degree of polynomial to fit
		
	Returns
	=======
	beta : float
		Array of polynomial coefficients in order from highest degree
		to the lowest (this is for compatibility with numpy.poly1d)
	'''

	#get the X matrix, with one column for each degree (deg)
	X = np.zeros((x.size,deg+1),dtype='float64')
	X[:,0] = 1.0
	for i in range(1,deg+1):
		X[:,i] = X[:,i-1]*x
		
	#turn y into a matrix
	Y = np.array([y]).T
	
	#Get Q and R using the Gram-Schmidt process
	Q,R = GramSchmidt(X)

	#time to solve Rβ = Q^T Y
	#where β contains the polynomial coefficients
	qty = np.dot(Q.T,Y)
	
	#solve set of equations for β
	beta = np.linalg.solve(R,qty)
	
	#return in reverse order like numpy.polyfit does
	return beta.flatten()[::-1]
	
