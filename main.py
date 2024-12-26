from plot_makers.surf_maker import surf_maker
import numpy as np

fun = lambda x, y, t: 10*np.sin(-0.25*t*np.sqrt(x*x + y*y))

xlim = np.array([-25,25])
ylim = np.array([-25,25])
tlim = np.array([0,5])
fps = 120
N = 150
zlim = np.array([-50, 50])

mkr = surf_maker(N,fps,xlim,ylim,tlim,fun,zlim)
mkr.save_animated_plot()
mkr.save_static_plot(3)
