import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# This call to setup() does all the work
setup(
    name="{{cookiecutter.library_name}}",
    version="1.0.0",
    description="{{cookiecutter.description}}",
    long_description_content_type="text/markdown",
    url="{{cookiecutter.github_url}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["{{cookiecutter.library_name}}"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)