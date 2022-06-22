import numpy as np


def FakeData(beta=[0.1,0.2,2.0,-10.0],noise=5.0,xrange=[-5.0,5.0],n=100):
	'''
	Generate some fake "data" by defining a polynomial with some 
	additional noise.
	
	Inputs
	======
	beta : list
		List of polynomial betaicients, the length of which is equal to
		the degree of the polynomial minus one. The betaicients are in
		the order from highest degree to lowest.
		e.g. 
		beta = [1,2,3,4,5] would give the following polynomial:
		x**4 + 2x**3 + 3x**2 + 4x + 5
	noise : float
		Level of Gaussian noise to apply to the "data" - this value 
		would effectively be the standard deviation of the noise.
	range : list
		2-element array-like defining the range of x values.
	n : int
		The number of elements in the output arrays
		
	Returns
	=======
	x :  float
		Array of randomly selected x values within xrange.
	t : float
		The polynomial at each x coordinate + noise.
		
	
	'''


	#create random x array
	x = np.random.random(n)*(xrange[1] - xrange[0]) + xrange[0]
	x.sort()
	
	#polynomial object
	beta = np.array(beta)
	p1d =  np.poly1d(beta)
	deg = beta.size - 1
	
	#get y
	y = p1d(x) + noise*(np.random.randn(x.size))	

	return x,y
