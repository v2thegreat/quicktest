from typing import Callable, List, Collection
from time import clock
import warnings

__MATPLOTLIB_INSTALLED__ = None
__TQDM_INSTALLED__ = None

#Setting import flags
def import_matplotlib():
    """
    Creating a seperate function to import matplotlib and reduce import time
    """
    global __MATPLOTLIB_INSTALLED__
    try:
        import matplotlib.pyplot as plt
        __MATPLOTLIB_INSTALLED__ = True
        global plt
    except ImportError:
        warnings.warn("Matplotlib not Found", ImportWarning)
        __MATPLOTLIB_INSTALLED__ = False

def import_tqdm():
    """
    Creating a seperate function to import tqdm and reduce import time
    """
    global __TQDM_INSTALLED__
    try:
        from tqdm import tqdm
        __TQDM_INSTALLED__ = True
        global tqdm
    except ImportError:
        warnings.warn("tqdm not Found", ImportWarning)
        __TQDM_INSTALLED__ = False


class quicktest:
    def __init__(self, iterable: Collection, *functions):
        """
        A simple python library which compares runtimes for different functions

        Args:
            iterable    (:Collection: of objects): A collection of parameters that functions are meant to take as input
            functions   (:obj: Callable): A collection of callable functions that take values of iterable as parameters
        """

        self.iterable = iterable
        self.functions = []
        self.__meanLst = []
        self.__speedTestRunTimes = []
        self.__function_names = []
        self._fastest = None
        self.__testran = False

        self._setFunctions(functions)
        self._setFunctionNames()

    def _setFunctions(self, functions):
        """
        Checks if functions are callable and addsm to a list for funcitons. If not, raises ValueError
        
        Args:
            functions   (:obj: Callable): A collection of callable functions that take values of iterable as parameters
        """
        for x in functions:
            if not callable(x):
                raise ValueError("{} is not a callable function".format(x))

            self.functions.append(x)

    def _setFunctionNames(self):
        """
        Extracts names of functions and savesm for later
        """
        for func in self.functions:
            self.__function_names.append(func.__name__)

    def run(self, progressbar = False):
        """Runs functions with given parameters to get average runtime

        Args:
            progressbar (bool, optional): Optional parameter for displaying progressbar, default False
        """
        if progressbar:
            self.__check_tqdm_installed()
            self.__run_with_progressbar()

        else:
            self.__run_without_progressbar()

        self.__testran = True

    def __run_with_progressbar(self):
        """
        running tests with progressbar
        """
        for func in tqdm(self.functions):
                temp = [self.__get_time(func, iterVal) for iterVal in self.iterable]
                self.__speedTestRunTimes.append(temp)

    def __run_without_progressbar(self):
        """
        running tests without progressbar
        """
        for func in self.functions:
                temp = [self.__get_time(func, iterVal) for iterVal in self.iterable]
                self.__speedTestRunTimes.append(temp)

    @property
    def fastest(self) -> Callable:
        """
        gets the fastest function
        """
        self.__runtests()

        min_time = min(self.__meanLst)
        min_pos = self.__meanLst.index(min_time)
        self._fastest = self.functions[min_pos]

        return self._fastest

    @property
    def fastest_time(self) -> float:
        """
        gets runtime for fastest function
        """
        try:
            return min(self.__meanLst)

        except ValueError:
            self.__runtests()
            return self.fastest_time

    @property
    def fastestby(self) -> float:
        """
        returns how much faster the fastest function is compared to the second fastest 
        """
        self.__runtests()                                           #Running this in case tests have not been run before
        smallestpos = self.__meanLst.index(self.fastest_time)       #Getting position of fastest one so that it can be skipped later

        secondfastest = min(self.__meanLst[:smallestpos] + self.__meanLst[smallestpos+1:])  #getting second smallest one by skipping fastest
        self._fastestby =  (secondfastest - self.fastest_time)/secondfastest    #calculate how much faster it is
        return self._fastestby*100

    @property
    def plot(self) -> object:
        """
        returns a plot object which has all function runtimes plotted
        sets the plot's legend to True
        """
        self.__runtests()
        self.__checkMatplotlib()

        for pos, runTimes in enumerate(self.__speedTestRunTimes):
            plt.plot(runTimes, label = self.__function_names[pos])
        plt.legend()

        return plt

    @property
    def get_all_runtimes(self) -> dict:
        """
        returns all the runtimes for all the functions as a dictionary
        """
        self.__runtests()
        self._all_runtimes = {}
        for x in range(len(self.__speedTestRunTimes)):
            self._all_runtimes[self.functions[x]] = self.__speedTestRunTimes[x]
        return self._all_runtimes

    def __runtests(self):
        """
        function to run the tests if they haven't been run before
        """
        if not self.__testran:
            self.run()
            self.__testran = True
        self.__meanLst = self._get_all_mean_time

    @property
    def _get_all_mean_time(self) -> List:
        """
        return a list of a mean for all the runtimes
        """
        return [self._mean(times) for times in self.__speedTestRunTimes]

    @staticmethod
    def __checkMatplotlib():
        """
        function to check if Matplotlib is installed
        """
        import_matplotlib()
        try:
            if not __MATPLOTLIB_INSTALLED__:
                raise ImportError("Matplotlib not Installed")
        except ValueError:
            self.__checkMatplotlib()

    @staticmethod
    def __check_tqdm_installed():
        """
        function to check if tqdm is installed
        """
        import_tqdm()
        try:
            if not __TQDM_INSTALLED__:
                raise ImportError("tqdm is not Installed")
        except ValueError:
            self.__check_tqdm_installed()

    @staticmethod
    def _mean(times):
        """
        Calculates mean time
        """
        return sum(times)/len(times)

    @staticmethod
    def __get_time(func: Callable, iter_val: object) -> float:
        """
        :Callable     func:        Function that needs to be run to calculate its run time
        :object     iter_val:     Iterator vales object that is passed as parameter for function
        """
        t = clock()
        func(iter_val)
        return clock() - t


if __name__ == '__main__':
    t = quicktest(range(100000), dir, float)
    help(t)
    # print(t.fastestby)