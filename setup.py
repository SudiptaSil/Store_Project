import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Store-ssil",
    version="0.0.1",
    author="Sudipta Sil",
    author_email="sudipta.sil14@gmail.com",
    description="Virtual cash register",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SudiptaSil/Store_Project",
    project_urls={
        "Bug Tracker": "https://github.com/SudiptaSil/Store_Project/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)