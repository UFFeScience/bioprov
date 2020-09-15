__author__ = "Vini Salazar"
__license__ = "MIT"
__maintainer__ = "Vini Salazar"
__url__ = "https://github.com/vinisalazar/bioprov"
__version__ = "0.1.1"


import setuptools

setuptools.setup(
    name="bioprov",
    version="0.1.1",
    author="Vini Salazar",
    author_email="viniws@gmail.com",
    description="BioProv - Provenance capture for bioinformatics workflows",
    long_description=(
        "BioProv is a toolkit for capturing and extracting provenance data from"
        " bioinformatics workflows."
        "\n"
        "To know more about BioProv, please visit the Homepage."
    ),
    url="https://github.com/vinisalazar/BioProv",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    scripts=["bioprov/bioprov"],
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "biopython",
        "coolname",
        "coveralls",
        "pandas",
        "prov",
        "pydot",
        "pytest",
        "pytest-cov",
        "tqdm",
    ],
)
