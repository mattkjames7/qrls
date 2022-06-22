import numpy as np
import matplotlib.pyplot as plt
from .Example import Example

def Test():
	'''
	Create some test plots
	
	
	'''

	beta = [0.1,1.8,4.0,-5.0]
	ax,out = Example(beta,ShowNumpy=False,ShowOriginal=False,ShowFit=False)
	xy = (out['x'],out['y'])
	
	plt.figure(figsize=(16,5))
	ax0,_ = Example(beta,deg=2,Label='(a)',fig=plt,maps=[3,1,0,0],ShowNumpy=False,ShowOriginal=False,xy=xy,loc='center')
	ax1,_ = Example(beta,deg=3,Label='(b)',fig=plt,maps=[3,1,1,0],ShowNumpy=False,ShowOriginal=False,xy=xy,loc='center')
	ax2,_ = Example(beta,deg=10,Label='(c)',fig=plt,maps=[3,1,2,0],ShowNumpy=False,ShowOriginal=False,xy=xy,loc='center')
	
	
	plt.figure(figsize=(16,5))
	ax0,_ = Example(beta,deg=2,Label='(a)',fig=plt,maps=[3,1,0,0],ShowNumpy=False,ShowOriginal=True,xy=xy,loc='center')
	ax1,_ = Example(beta,deg=3,Label='(b)',fig=plt,maps=[3,1,1,0],ShowNumpy=False,ShowOriginal=True,xy=xy,loc='center')
	ax2,_ = Example(beta,deg=10,Label='(c)',fig=plt,maps=[3,1,2,0],ShowNumpy=False,ShowOriginal=True,xy=xy,loc='center')


	ax0.set_facecolor([1.0,0.0,0.0,0.25])
	ax1.set_facecolor([0.0,1.0,0.0,0.25])
	ax2.set_facecolor([1.0,0.0,0.0,0.25])
	
