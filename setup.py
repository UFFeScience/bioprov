import setuptools

setuptools.setup(
    name="bioprov",
    version="0.1.0",
    author="Vini Salazar",
    author_email="viniws@gmail.com",
    description="BioProv - Provenance capture for bioinformatics workflows",
    long_description="BioProv is a toolkit for capturing and extracting provenance data from bioinformatics workflows.",
    url="https://github.com/vinisalazar/BioProv",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    packages=setuptools.find_packages(),
    scripts=[],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["pytest", "biopython"],
)
