from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file

long_description = ''

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='qface',
    version='1.0.0a3',
    description='QFace - A Generator Framework',
    long_description=long_description,
    url='https://github.com/Pelagicore/qface',
    author='JRyannel',
    license='GPLV3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='qt code generator framework',
    packages=['qface'],
    install_requires=[
        'jinja2',
        'path.py',
        'pyyaml',
    ],
    extras_require={
        'dev': [
            'antlr4-python3-runtime',
            'click',
            'watchdog',
            'pypandoc',
        ],
        'test': [
            'pytest',
            'click',
            'watchdog',
            'ipdb',
        ],
    },
    entry_points='''
        [console_scripts]
        qface=cli:cli
    '''
)
