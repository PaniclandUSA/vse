"""
VSE Setup
Vector-Space Esperanto v1.4
"""

from setuptools import setup, find_packages
import pathlib

# Read README
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="vse",
    version="1.4.0",
    description="Vector-Space Esperanto: Universal semantic control protocol for AI systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stonespell72/vse",
    author="John J. Weber II",
    author_email="john@example.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="ai, semantic-control, nlp, vector-space, prompt-engineering",
    packages=find_packages(exclude=["tests", "examples", "docs", "notebooks"]),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
        "viz": [
            "matplotlib>=3.5",
            "plotly>=5.0",
            "networkx>=2.8",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/stonespell72/vse/issues",
        "Source": "https://github.com/stonespell72/vse",
    },
)
