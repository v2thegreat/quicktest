
## Usage:

Features simple tests that can be executed from the command line to check and compare execution speeds for different functions on the current hardware

### Understand Usage with Command line

```
>>> from quicktests import quickTests
>>> def isPrimeWithPython(n):
	for x in range(2, int(n**(0.5))):
		if n%x == 0:
			return False
	return True

>>> def isPrimeWithNumpyAndPython(n):
	return all(n % np.arange(2, int(n**(0.5))))

>>> test = quickTest(range(1000), isPrimeWithPython, isPrimeWithNumpyAndPython)

>>> test.run()
>>> print(test.getMeanDifference())
>>> print(test.getFaster())
>>> print(test.showPlot())

Output:

	4.8408712118543915e-06
	isPrimeWithPython
	<Plot showing the difference>
```

The quicktests class is for writting speed tests quickly to see which two functions are faster and visualizing the results with an increase in number of outputs of changes in outputs


## Does the creator know that this is a pretty bad way to check if a function is actually faster than another?

Yes, he does. Does the reader realize that this is just a project and that all life is meaningless and we are in one way or another just waiting for the heat death of the universe to kill us all?

Further, this is simply a means of checking if a particular algorithm function faster than another without having to dig through and finding the complexity of the algorithm in-depth via the documentation or source code.

As an example:

Let's say I have 2 algorithms, which have the same job; finding out if a number is a prime or not:


### Generic Python program to check if a number is prime:

#### A traditional Python Prime Number Checking Function

```
def isPrimeWithPython(n):
	for x in range(2, int(n**(0.5))):
		if n%x == 0:
			return False
	return True
```

As the name suggests, it's a simple python loop that checks if any numbers between 2 to the square root of the given number is divisible by the number itself, and if not calls it a prime number

#### Running a Python Prime Number Checking Function with Numpy

```
def isPrimeWithNumpyAndPython(n):
	return all(n % np.arange(2, int(n**(0.5))))
```

In this one however, we're doing something different, and possibly, *really complicated*

Let me explain this in detail:

	np.arange(2, int(n**0.5))

This is pretty fun right? it's just creating a Numpy array with a range starting from 2 to square root of the given number

	n % np.arange(2, int(n**0.5))

Hmm, this seems a little more difficult, but it's simply returning an array which has the remainders between the number `n` and each element in the array. Not too hard right? here's an example:

Let `n = 101` and keep simplifying it:

	101 % np.arange(2, int(101**0.5))

which is the same as:

	101 % np.arange(2, int(10.04987562112089)) #According to the Python 3.5 interpreter

and again, this can be simplified down to:
	
	101 % np.arange(2, 10)

and again, this is the same as:
	
	101 % array([2, 3, 4, 5, 6, 7, 8, 9])

now, numpy arrays have an interesting property where they can run any binary operation (like `%` in this case) to an entire array in one go, without needed a for loop. Breaking this down again, we get the result of this operation as:

	array([1, 2, 1, 1, 5, 3, 5, 2])


Hmm! It seems like each of these is a number that's not 0. If my math is right (and by some miracle it is in this case), this means that there's no number from 2-101^(1/2) that gives us a remainder of 0, and hence, we can beleive that this number is prime. Simple right?

But, how do we cross check this? with the `all` function! which return's true if `all` the elements in an array/list/any container can be considered to be a boolean `yes` (i.e. True)

so, in this case, this is what our all function looks like:

	all(array([1, 2, 1, 1, 5, 3, 5, 2]))

In this, is there any number that might indicate that this number is false, or, in programmers terms, do any of these considered a boolean false? Nope! So naturally, it returns True, telling us that this thing is a prime number! 

Phew, that wasn't so hard was it? Yes, it was a case where we threw in too many things in one line causing it to seem like a cluster show, but that's not what we're looking for right now, is it?

Now, let's have another look at the two functions:


**A python for loop that only uses a function:**

```
def isPrimeWithPython(n):
	for x in range(2, int(n**(0.5))):
		if n%x == 0:
			return False
	return True
```

**A Python function that uses the C-compiled Numpy library that's extrememly fast, esp. in comparison to Python:**

```
def isPrimeWithNumpyAndPython(n):
	return all(n % np.arange(2, int(n**(0.5))))
```


So, let's write some simple test to see which one will be faster. The following speedtests seem to do the job well enough

```
from time import clock


def test1(n):
	t = clock()
	isPrimeWithPython(n)
	return clock()-t


def test2(n):
	t = clock()
	isPrimeWithNumpyAndPython(n)
	return clock()-t
```

Pretty simple right? just taking a note of the clock when the function starts and returning the time difference between that and when the function ends. Nothing much to it

Let's run it over a list of values to make sure that it's easy to test accross a lot of values by doing this:

```
l1 = [test1(x) for x in range(1000)]
l2 = [test2(x) for x in range(1000)]
```

and to help us visualize it, let's use matplotlib to plot it:

```
import matplotlib.pyplot as plt


plt.plot(l1, "r.", label = "isPrimeWithPython")
plt.plot(l2, "b.", label = "isPrimeWithNumpyAndPython")
plt.legend()
plt.show()
```

This is what we see:

![Graph showing the variation in the two functions runtime](https://github.com/v2thegreat/quicktest/blob/master/Images/Readme%20Comparison%20Test.png)


WHAT? Why is the numpy setup slower? That's not what we were expecting, was it?

Well, that could be for a number of reasons, but it goes to show my point; **your computer right now runs Numpy code slower than python code**

Ok, that's not true. It runs *this* Numpy code slower than *this* Python code. Guess Occam was right in this case, the simpler solution was the better one. But what if it wasn't? What if you were writing a time depenant program in python and you needed to check which of the two algoritms was faster quicly without having to look into the documentaion (which may not even exist)? 


Of course, there are going to be situations where this is just going to be a bad idea, but isn't that true for pretty much everything?

However, if you still decide to mention the thing about it being a bad way to check if functions are faster than another, then I'd like to thank you for your time and effort, and that it's been noted and will be taken care of during the apocalypse, or when hell freezes over!

**HAIL LORD CHUTULU** :)
