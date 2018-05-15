from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(name='quicktest',
    version='0.8',
    ext_modules = cythonize([r"quicktest/primetest.pyx", r"quicktest/test_quicktest.pyx"]),
    description='A dependency for milkCan to enable it to run speed tests',
    url='https://github.com/v2thegreat/quicktest',
    author='v2thegreat',
    author_email='v2thegreat@gmail.com',
    license='MIT',
    packages=['quicktest'],
    zip_safe=False,
    install_requires=['matplotlib', 'tqdm', 'Cython'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
    )
