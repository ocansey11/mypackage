from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packaes= find_packages(exclude=['tests']),
    license="MIT",
    description="EDSA example pyython package",
    long_description=open('readME.md').read(),
    install_requires=["numpy"],
    url="https://github.com/ocansey11/mypackage",
    author="Ocansey Kevin",
    author_email="kevinocansey11@gmail.com"
)