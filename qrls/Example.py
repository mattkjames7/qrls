import numpy as np
import matplotlib.pyplot as plt
from .FakeData import FakeData 
from .QRLeastSq import QRLeastSq
from .PlotLabel import PlotLabel


def _eqlabel(C):
	
	deg = len(C) - 1
	s = '$y='
	for i in range(0,deg):
		s += '{:3.1f}x'.format(C[i])
		if i < deg-1:
			s+='^{'+'{:d}'.format(deg-i)+'}'
		if C[i+1] >= 0:
			s += '+'
	s += '{:3.1f}$'.format(C[-1])
	return s
		

def Example(beta=[0.1,0.2,2.0,-10.0],deg=None,noise=5.0,
			xrange=[-10.0,10.0],n=100,fig=None,maps=[1,1,0,0],
			ShowNumpy=True,ShowLegend=True,ShowOriginal=True,Label=None):
	'''
	Generate some fake "data" by defining a polynomial with some 
	additional noise.
	
	Inputs
	======
	beta : list
		List of polynomial coefficients, the length of which is equal to
		the degree of the polynomial minus one. The coefficients are in
		the order from highest degree to lowest.
		e.g. 
		beta = [1,2,3,4,5] would give the following polynomial:
		x**4 + 2x**3 + 3x**2 + 4x + 5
	deg : int
		Degree of polynomial to fit	(if None then it will be len(beta)-1)
	noise : float
		Level of Gaussian noise to apply to the "data" - this value 
		would effectively be the standard deviation of the noise.
	range : list
		2-element array-like defining the range of x values.
	n : int
		The number of elements in the output arrays
	fig : None|object
		If None - a new figure is created; if supp[lied with an instance
		of matplotlib.pyplot then a new subplot is created on an 
		existing figure; and if an Axes instance is provided then the
		existing Axes will be used.
	maps : list
		4-element array-like defining the position of the subplot.
		maps=[xmaps,ymaps,xmap,ymap]
		xmaps : number of horizontal subplots
		ymaps : number of vertical subplots
		xmap : horizontal position from the left
		ymap : vertical postition from the top
	ShowNumpy : bool
		If True then the numpy.polyfit solution using SVD will be shown.
	ShowLegend : bool
		If True then the plot will have a legend.
	ShowOriginal : bool
		If True then the original equation will also be plotted.
	Label : str
		plot label

	Returns
	=======
	ax : object
		matplotlib.pyplot.Axes instance

	'''
	
	#get the fake data
	x,y = FakeData(beta=beta,noise=noise,xrange=xrange,n=n)
	
	#get the polynomial degree to fit if not supplied
	if deg is None:
		deg = len(beta) - 1
	
	#QR fit
	betaqr = QRLeastSq(x,y,deg)
	p1dqr = np.poly1d(betaqr)
	
	#numpy fit
	betanp = np.polyfit(x,y,deg)
	p1dnp = np.poly1d(betanp)
	
	#original
	p1d0 = np.poly1d(beta)
	
	#get some lines to plot
	xp = np.linspace(xrange[0],xrange[1],n)
	yp0 = p1d0(xp)
	ypqr = p1dqr(xp)
	ypnp = p1dnp(xp)
	
	#get the labels
	y0l = _eqlabel(beta)
	yql = _eqlabel(betaqr)
	ynl = _eqlabel(betanp)
	
		
	if fig is None:
		fig = plt
		fig.figure()
	if hasattr(fig,'Axes'):	
		ax = fig.subplot2grid((maps[1],maps[0]),(maps[3],maps[2]))
	else:
		ax = fig

	#plot data
	if noise > 0:
		ax.scatter(x,y,color='grey',label='Noisy Data')
	else:
		ax.scatter(x,y,color='grey',label='Data')
	
	#plot original equation without noise
	if ShowOriginal:
		ax.plot(xp,yp0,color='black',label=y0l+' (original)')
		
	#plot QR fit
	ax.plot(xp,ypqr,color='red',label=yql+' (QR)',linestyle='--',lw=2.0)
	
	#plot numpy fit
	if ShowNumpy:
		ax.plot(xp,ypnp,color='lime',label=ynl+' (numpy)',linestyle=':',lw=3.0)
	
	#subplot label
	if not Label is None:
		PlotLabel(ax,Label)
	
	#show the legend
	if ShowLegend:
		ax.legend()
	
	return ax
