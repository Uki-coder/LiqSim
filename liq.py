import numpy as np
import sympy as sp
import scipy as sc

class liq:

    def __init__(self, ro, vel_y, vel_x, pres):
        if isinstance(ro, np.float64) and \
            isinstance(vel_y, sc.Expr) and \
            isinstance(vel_x, sc.Expr) and \
            isinstance(pres, sc.Expr):

            self.__ro = ro
            self.__vel_y = vel_y
            self.__vel_x = vel_x
            self.__pres = pres
            self.__symtime = sp.Symbol('t')
            self.__ntime = np.float64(0)

        else: raise TypeError('One or more of parameters ro vel_y, vel_x, pres has wrong type')

    @property
    def vel_x(self):
        return self.__vel_x
    @property
    def vel_y(self):
        return self.__vel_y
    @property
    def ro(self):
        return self.__ro
    @property
    def pres(self):
        return self.__pres

    @ntime.setter ##ask
    def time_set(self, t):
        if isinstance(t, np.float64):
            self.__ntime = t
        else: raise TypeError('Wrong type of ntime')


    @property
    def vel_y_value(self):
        return self.__vel_y.subs(self.__time)

    def __del__(self):
        print('Deleting liq')