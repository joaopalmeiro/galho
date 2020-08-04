import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text().split()


def get_version(root, rel_path):
    for line in (root / rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="galho",
    version=get_version(HERE, "galho/__version__.py"),
    description="A minimal Python implementation of the `tree` command to list the contents of folders.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/joaopalmeiro/galho",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Terminals",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Typing :: Typed",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    entry_points={"console_scripts": ["galho=galho.__main__:main"]},
    project_urls={
        "Bug Reports": "https://github.com/joaopalmeiro/galho/issues",
        "Source": "https://github.com/joaopalmeiro/galho",
    },
    keywords="cli, tree",
)
