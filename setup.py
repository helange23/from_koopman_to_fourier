import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fourier_koopman-pkg-helange23",
    version="0.0.0",
    author="Henning Lange, Steven L. Brunton, J. Nathan Kutz ",
    author_email="helange@uw.edu",
    description=" Spectral Methods for Long-term Time Series Prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/helange23/from_fourier_to_koopman",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
