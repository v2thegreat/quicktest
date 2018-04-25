from typing import Callable, List, Collection
from cpython cimport bool, list
from time import clock
import warnings

cdef bool __MATPLOTLIB_INSTALLED__

try:
    import matplotlib.pyplot as plt
    __MATPLOTLIB_INSTALLED__ = True

except ImportError:
    warnings.warn("Matplotlib not Found", ImportWarning)
    __MATPLOTLIB_INSTALLED__ = False


cdef class quicktest:
    def __init__(self, iterable: Collection, *functions):
        """

        :type iterable: Collection
        """
        cdef int x
        self.iterable = iterable
        self.functions = []
        self.__meanLst = []
        self.__speedTestRunTimes = []
        self.__function_names = []

        self._setFunctions(functions)
        self._setFunctionNames()

    def run(self):

        for func in self.functions:
            temp = [self.__get_time(func, iterVal) for iterVal in self.iterable]
            self.__speedTestRunTimes.append(temp)

    def fastest(self):
        cdef float min_time
        cdef short unsigned int min_pos

        self.__meanLst = self._get_all_mean_time

        try:
            min_time = min(self.__meanLst)

        except ValueError:
            raise RuntimeError("Please call run function before calling fastest proper")

        min_pos = self.__meanLst.index(min_time)
        return self.functions[min_pos]

    def getPlot(self):
        cdef int pos

        self._checkMatplotlib()

        for pos, runTimes in enumerate(self.__speedTestRunTimes):
            plt.plot(runTimes, label = self.__function_names[pos])

        return plt

    cdef void _setFunctionNames(self):
        for x in self.functions:
            self.__function_names.append(str(x).split()[1])

    cdef void _setFunctions(self, functions):
        for x in functions:
            if not callable(x):
                raise ValueError("{} is not a callable function".format(x))

            self.functions.append(x)

    cpdef list _get_all_mean_time(self):
        return [self._mean(times) for times in self.__speedTestRunTimes]

    def _checkMatplotlib(self):
        if not __MATPLOTLIB_INSTALLED__:
            raise ImportError("Matplotlib not Installed")

    cpdef float _mean(self, times):
        return sum(times)/len(times)

    cpdef float __get_time(self, func: Callable, iter_val: object):
        """

        :type iter_val: object
        """
        t = clock()
        func(iter_val)
        return clock() - t
