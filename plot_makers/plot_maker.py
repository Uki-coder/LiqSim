import abc
from types import FunctionType
import numpy as np

class plt_maker(abc.ABC):

    def __init__(self, mesh_grids_num, fps, xlim, ylim, tlim, fun):
        self._check_type(mesh_grids_num, int, 'mesh_grids_num')
        self._check_type(fps, int, 'fps')
        self._check_type(fun, FunctionType, 'fun')

        self._check_shape(xlim, 'xlim')
        self._check_shape(ylim, 'ylim')
        self._check_shape(tlim, 'tlim')

        self._mesh_grids_num = mesh_grids_num
        self._tlim = tlim
        self._fps = fps
        self._fun = fun
        self._frn = int(self._fps * (self._tlim[1] - self._tlim[0]))
        self._xlim = xlim
        self._ylim = ylim

        self._x = np.linspace(xlim[0], xlim[1], self._mesh_grids_num)
        self._y = np.linspace(ylim[0], ylim[1], self._mesh_grids_num)
        self._t = np.linspace(self._tlim[0], self._tlim[1], self._frn)


    def _check_shape(self, obj, name):
        if (isinstance(obj, np.ndarray)):
            arr_check = np.array(obj)
            if arr_check.shape != (2,):
                raise ValueError('shape of ' + name + ' must be (1,2)')
        else:
            raise TypeError('Wrong type for ' + name + '. Must be a np.array')

    def _check_type(self, obj, type, name):
        if (isinstance(obj, type) != True):
            raise TypeError(name + ' is wong type. Must be '\
                            + str(type))

    def _check_tlim(self, obj):
        self._check_shape(obj, 'tlim')
        if (obj[1] < obj[0]):
            raise ValueError('tlim has wrong values')

    @abc.abstractmethod
    def _change_plot(self, frame): pass

    @abc.abstractmethod
    def save_animated_plot(self): pass

    @abc.abstractmethod
    def save_static_plot(self, time_moment): pass

    def __del__(self): pass