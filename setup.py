
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='Ospin-promotion',
    version='1.0',
    description='A useful module',
    author='Abhilasha Revur',
    author_email='abhilasha.m.revur@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pandas', 'numpy', 'datatest', 'attrs', 'pytest', 'python-dateutil'],
    package_data={
        '': [
            'input/orders_a.csv',
            'output/output.csv',
            'config/args.cfg',
            'tests/output/test_output.csv'
        ]
    }
)