from setuptools import setup

setup(name='quicktest',
	version='0.1',
	description='A dependency for milkCan to enable it to run speed tests',
	url='https://github.com/v2thegreat/quicktest',
	author='v2thegreat',
	author_email='v2thegreat@gmail.com',
	license='MIT',
	packages=['quicktest'],
	zip_safe=False,
	install_requires=['matplotlib']
	)
