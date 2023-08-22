from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).resolve().parent
exec((BASE_DIR / "tmplot/_version.py").read_text())

setup(
    name="tmplot",
    version=__version__,  # type: ignore[name-defined]  # NOQA: F821
    packages=find_packages(),
    description=(
        "tmplot: One liner Plotter that supports file and pipe input for quick description"
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="th2ch-g",
    url="https://github.com/th2ch-g/tmplot.py",
    license="MIT License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python",
    ],
    install_requires=[
        "matplotlib",
        "seaborn",
    ],
    extras_require={},
    package_data={},
    entry_points={"console_scripts": ["tmplot=tmplot.__main__:main"]},
)
