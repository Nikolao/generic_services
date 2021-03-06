import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generic_services",
    version="0.0.1",
    author="Nicolas Chauveau",
    description="Generic services for cloud apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nikolao",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
