from setuptools import setup, find_packages

setup(name='quicktest',
	version='0.4',
	description='A dependency for milkCan to enable it to run speed tests',
	url='https://github.com/v2thegreat/quicktest',
	author='v2thegreat',
	author_email='v2thegreat@gmail.com',
	license='MIT',
	packages=['quicktest', 'tests'],
	zip_safe=False,
	install_requires=['matplotlib', 'tqdm'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
	)
