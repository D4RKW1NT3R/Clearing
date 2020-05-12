from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
name='clearing',
version='0.0.2',
description='Cross-Platform Terminal Clearing Module.',
long_description=long_description,
long_description_content_type="text/markdown",
url='https://github.com/c00lhawk607/Clearing',
author='Jordan Dixon',
author_email='jordandixon2004@outlook.com',
license='GNU General Public License v3 (GPLv3)',
packages=['clearing'],
classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
zip_safe=True,
python_requires=">=3.0",
)