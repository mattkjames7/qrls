import numpy as np

def GramSchmidt(A):
	'''
	Gram-Schmidt method of QR decomposition A=QR
	
	Inputs
	======
	A : float	
		(m,n) matrix
	
	Returns
	=======
	Q : float
		Orthogonal matrix.
	R : float
		Upper triangular matrix.
	
	'''
	
	#get the dimensions of A
	m,n = A.shape
	
    #U and E have the same shape
	U = np.zeros(A.shape,dtype='float64')
	E = np.zeros(A.shape,dtype='float64')
	
    #calculate the orthogonal vectors (and unit vectors) 
	for i in range(0,n):
		U[:,i] = A[:,i]
		for j in range(0,i):
			U[:,i] -=  np.sum(A[:,i]*E[:,j])*E[:,j]
		E[:,i] = U[:,i]/np.linalg.norm(U[:,i])
		
	#E is actually Q!!
	Q = E

	#calculate R
	R = np.dot(Q.T,A)

	#make sure it's upper-triangular!
	R = np.triu(R)

	
	return Q,R
