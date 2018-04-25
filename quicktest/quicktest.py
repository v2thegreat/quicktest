from typing import Callable, List, Collection
from time import clock
import warnings


try:
    import matplotlib.pyplot as plt
    __MATPLOTLIB_INSTALLED__ = True
except ImportError:
    warnings.warn("Matplotlib not Found", ImportWarning)
    __MATPLOTLIB_INSTALLED__ = False

try:
    from tqdm import tqdm
    __TQDM_INSTALLED__ = True
except ImportError:
    warnings.warn("tqdm not Found", ImportWarning)
    __TQDM_INSTALLED__ = False

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

    def run(self, progressbar = True):
        if progressbar:
            self._checktqdm()
            self.__run_with_progressbar()

        else:
            self.__run_without_progressbar()

        self.__setproperties()

    def __run_with_progressbar(self):
        for func in tqdm(self.functions):
                temp = [self.__get_time(func, iterVal) for iterVal in self.iterable]
                self.__speedTestRunTimes.append(temp)     

    def __run_without_progressbar(self):
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

    @property
    def plot(self):
        self._checkMatplotlib()

        for pos, runTimes in enumerate(self.__speedTestRunTimes):
            plt.plot(runTimes, label = self.__function_names[pos])

        plt.legend()
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
    def fastestby(self) -> float:
        mintime = min(self.__meanLst)
        smallestpos = self.__meanLst.index(mintime)
        temp = self.__meanLst.pop(smallestpos)

        self._fastestby = min(self.__meanLst) - mintime

        self.__meanLst.insert(smallestpos, temp)
        return self._fastestby

    def __setproperties(self):
        self.fastest
        self.plot

    @property
    def _get_all_mean_time(self) -> List:
        return [self._mean(times) for times in self.__speedTestRunTimes]

    @staticmethod
    def _checkMatplotlib():
        if not __MATPLOTLIB_INSTALLED__:
            raise ImportError("Matplotlib not Installed")

    @staticmethod
    def _checktqdm():
        if not __TQDM_INSTALLED__:
            raise ImportError("tqdm is not Installed")

    @staticmethod
    def _mean(times):
        return sum(times)/len(times)

    @staticmethod
    def __get_time(func: Callable, iter_val: object) -> float:
        """
        :Callable     func:        Function that needs to be run to calculate its run time
        :object     iter_val:     Iterator vales object that is passed as the parameter for the function
        """
        t = clock()
        func(iter_val)
        return clock() - t

if __name__ == '__main__':
    t = quicktest(range(100000), dir, float)
    t.run(False)