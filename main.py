from plot_makers.quiver_maker import quiver_maker
from plot_makers.surf_maker import surf_maker
import numpy as np

fun = lambda x, y, t: 25*np.sin(0.11*t*np.sqrt(x*x + y*y)) - np.cos(x*y)
vfun = lambda x, y, t: 25*np.sin(0.11*t*np.sqrt(x*x + y*y)) - np.cos(x*y)
ufun = lambda x, y, t: 25*np.sin(0.11*t*np.sqrt(x*x + y*y)) - np.cos(x*y)

xlim = np.array([-50,50])
ylim = np.array([-50,50])
tlim = np.array([0,5])
fps = 120
N = 100
zlim = np.array([-50, 50])

quiv= quiver_maker(N,fps,xlim,ylim,tlim,fun, vfun,ufun)
quiv.save_animated_plot()