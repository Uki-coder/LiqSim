import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
from .plot_maker import plt_maker

class quiver_maker(plt_maker):

    def __init__(self, mesh_grids_num, fps, xlim, ylim, tlim, fun, ufun, vfun):

        mpl.use('TkAgg')

        super().__init__(mesh_grids_num, fps, xlim, ylim, tlim, fun)

        self._x, self._y= np.meshgrid(self._x, self._y)


        self.__v = np.zeros((self._mesh_grids_num + 1, self._mesh_grids_num + 1, self._frn))
        self.__u = np.zeros((self._mesh_grids_num + 1, self._mesh_grids_num + 1, self._frn))

        for i in range(self._frn):
            self.__v[:, :, i] = vfun(self._x, self._y, self._t[i])
        for i in range(self._frn):
            self.__u[:, :,i] = ufun(self._x, self._y,  self._t[i])

        self.__fig, self.__ax = plt.subplots(1,1)
        self.__plot = [self.__ax.quiver(self._x, self._y, self.__v[:, :, 0], self.__u[:, :, 0], color='0.75')]

    def _change_plot(self, frame):
        self.__plot[0].remove()
        self.__plot[0] = self.__ax.quiver(self._x, self._y, self.__v[:, :, frame], self.__u[:, :, frame], cmap="afmhot_r")

    def save_animated_plot(self):
        ani = animation.FuncAnimation(self.__fig, self._change_plot, self._frn, interval=1000 / self._fps)
        plt.show()
    def __del__(self): pass