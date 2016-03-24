from setuptools import setup, find_packages

NAME = 'graph-extract'

CLASSIFIERS = [
"Development Status :: 3 - Alpha",
"Intended Audience :: Science/Research",
"License :: OSI Approved :: MIT License"
]

VERSION = '0.0.1'

DESCRIPTION = 'Library for extracting values from graphs'

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

AUTHOR = 'Rich Lewis'
AUTHOR_EMAIL = 'rl403@cam.ac.uk'
URL = 'https://github.com/richlewis42/graph-extract'
LICENSE = 'MIT License'
INSTALL_REQUIRES = ['numpy', 'pillow']

if __name__ == '__main__':
    setup(
          name=NAME,
          classifiers=CLASSIFIERS,
          version=VERSION,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          url=URL,
          license=LICENSE,
          install_requires=INSTALL_REQUIRES,
          packages=find_packages()
    )
