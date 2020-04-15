from codecs import open as codecs_open
import os
from setuptools import setup, find_packages

with codecs_open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("__init__.py") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Prime Now Notifier",
    version=version,
    description=u"Texts you when there's an available delivery slot for Prime Now in your area.",
    long_description=long_description,
    python_requires=">=3",
    classifiers=[],
    keywords="utilities, covid-19, shopping",
    author=u"Bhavika Tekwani",
    author_email="bhavicka@protonmail.com",
    url="https://github.com/bhavika/Prime-Now-Notifier",
    license="MIT",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=read("requirements.txt").splitlines(),
    entry_points="""
      [console_scripts]
      """,
)