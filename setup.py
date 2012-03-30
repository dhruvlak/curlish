import os
from setuptools import setup

readme = open(os.path.join(os.path.dirname(__file__), 'README'), 'r').read()

setup(
    name='curlish',
    author='Fireteam Ltd.',
    author_email='support@fireteam.net',
    version='1.0',
    url='http://github.com/fireteam/curlish',
    py_modules=['curlish'],
    description='A wrapper for curl that adds OAuth support',
    long_description=readme,
    entry_points={
        'console_scripts': [
            'curlish = curlish:main'
        ]
    },
    install_requires=['Pygments'],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)