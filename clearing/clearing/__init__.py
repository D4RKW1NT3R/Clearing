import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="clearing-c00lhawk607",
  version="0.0.1",
  author="Jordan Dixon",
  author_email="jordandixon2004@outlook.com",
  description="Clears Terminal: Cross-Platform.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/c00lhawk607/Clearing",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU :: 3 :: License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.0",
)