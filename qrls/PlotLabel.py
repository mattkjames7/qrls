import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

def PlotLabel(ax,label,color=[0.0,0.0,0.0],fontsize=None,x=0.05,y=0.95,
				ha='center',va='center',bgcolor=None,**kwargs):
	
	txt = ax.text(x,y,label,color=color,ha=ha,va=va,
				transform=ax.transAxes,fontsize=fontsize,**kwargs)
	
	if not bgcolor is None:
		txt.set_path_effects([path_effects.Stroke(linewidth=2,foreground=bgcolor),
								path_effects.Normal()])

	return txt
