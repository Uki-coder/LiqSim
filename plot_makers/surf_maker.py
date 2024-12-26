import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
from .plot_maker import plt_maker

class surf_maker(plt_maker):

    def __init__(self, mesh_grids_num, fps, xlim, ylim, tlim, fun, zlim):

        mpl.use('TkAgg')

        super().__init__(mesh_grids_num, fps, xlim, ylim, tlim, fun)
        super()._check_shape(zlim, 'zlim')

        self._x, self._y = np.meshgrid(self._x, self._y)
        self.__zvalues = np.zeros((self._mesh_grids_num + 1, self._mesh_grids_num + 1, self._frn))

        for i in range(self._frn):
            self.__zvalues[:, :, i] = fun(self._x, self._y, self._t[i])

        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(111, projection='3d')
        self.__plot = [self.__ax.plot_surface(self._x, self._y, self.__zvalues[:, :, 0], color='0.75', rstride=1, cstride=1)]
        self.__ax.set_zlim(zlim)

    def _change_plot(self, frame):
        self.__plot[0].remove()
        self.__plot[0] = self.__ax.plot_surface(self._x, self._y, self.__zvalues[:, :, frame], cmap="ocean")

    def save_animated_plot(self):
        ani = animation.FuncAnimation(self.__fig, self._change_plot, self._frn, interval=1 / self._fps)
        writer = animation.PillowWriter(fps=self._fps,
                                        metadata=dict(artist='Me'),
                                        bitrate=1800)
        ani.save('surface.gif', writer=writer)

    def save_static_plot(self, time_moment):
        self.__fig, self.__ax = plt.subplots()
        self.__ax.contourf(self._x, self._y, self.__zvalues[:, :, int(time_moment * self._frn / (self._tlim[1] - self._tlim[0]))], cmap="ocean")
        plt.savefig('surface.png', dpi=600)

    def __del__(self): pass