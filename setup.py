from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="estruturas",
    version="0.0.1",
    author="Pitossomo",
    author_email="pitossomo@gmail.com",
    description="A package to calculate continuous hyperstatic beams",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pitossomo/estruturas",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)