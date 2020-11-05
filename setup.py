import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dayuri-pending", # Replace with your own username
    version="0.0.0",
    author="Luis Alberto Díaz Díaz",
    author_email="Dummy@Anon.forNow",
    description="Functional Language Compiler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Luis-omega/Dayuri",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
