import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nlpt5",
    version="1.0.0",
    author="adamnpeace",
    author_email="test@email.com",
    description="Pipelines for T5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamnpeace/nlpt5",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)