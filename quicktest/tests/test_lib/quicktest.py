from typing import Callable, List, Collection
from time import clock
import warnings


try:
    import matplotlib.pyplot as plt
    __MATPLOTLIB_INSTALLED__ = True
except ImportError:
    warnings.warn("Matplotlib not Found", ImportWarning)
    __MATPLOTLIB_INSTALLED__ = False


class quicktest:
    def __init__(self, iterable: Collection, *functions):
        """

        :type iterable: Collection
        """
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

    @property
    def fastest(self) -> Callable:
        self.__meanLst = self._get_all_mean_time

        try:
            min_time = min(self.__meanLst)

        except ValueError:
            raise RuntimeError("Please call run function before calling fastest proper")

        min_pos = self.__meanLst.index(min_time)
        return self.functions[min_pos]

    def getPlot(self):
        self._checkMatplotlib()

        for pos, runTimes in enumerate(self.__speedTestRunTimes):
            plt.plot(runTimes, label = self.__function_names[pos])

        return plt


    def _setFunctionNames(self):
        for x in self.functions:
            self.__function_names.append(str(x).split()[1])

    def _setFunctions(self, functions):
        for x in functions:
            if not callable(x):
                raise ValueError("{} is not a callable function".format(x))

            self.functions.append(x)

    @property
    def _get_all_mean_time(self) -> List:
        return [self._mean(times) for times in self.__speedTestRunTimes]

    @staticmethod
    def _checkMatplotlib():
        if not __MATPLOTLIB_INSTALLED__:
            raise ImportError("Matplotlib not Installed")

    @staticmethod
    def _mean(times):
        return sum(times)/len(times)

    @staticmethod
    def __get_time(func: Callable, iter_val: object) -> float:
        """

        :type iter_val: object
        """
        t = clock()
        func(iter_val)
        return clock() - t
