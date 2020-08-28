import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="galbwe_pycsv",
    version="0.0.1",
    author="Wes Galbraith",
    author_email="galbwe92@gmail.com",
    description="Package for parsing csv files to various data formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/galbwe/csv_parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)