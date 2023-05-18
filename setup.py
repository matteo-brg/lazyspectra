import os
from setuptools import setup, find_packages


PACKAGE = " "

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup( # Finally, pass this all along to distutils to do the heavy lifting.
    name             = PACKAGE,
    version          = '0.0.1',
    description      = 'Tools for ',
    long_description = read('README.md'),
    author           = ' ',
    author_email     = ' ',
    url              = '',
#    license          = read('LICENSE'),
    install_requires = read('requirements.txt').splitlines(),
    package_dir      = {'': 'src'},
#   packages         = find_packages(where='src', exclude=('tests', 'notebooks', 'scripts', 'data')),
    packages         = find_packages(where='src'),
    python_requires  = '>=3.8', 
    zip_safe         = False,
)
