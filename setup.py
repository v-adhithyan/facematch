from setuptools import setup

def readme():
    with open("README.rst") as f:
        return f.read()

setup(
    name="facematch",
    version="0.1",
    description="Find similarity between two faces.",
    long_description=readme(),
    keywords="faces similarity",
    author="Adhithyan V",
    author_email="v.adhithyan@gmail.com",
    license='MIT',
    packages=['facematch'],
    entry_points={
        "console_scripts":['facematch=facematch:main'],
    }
)
