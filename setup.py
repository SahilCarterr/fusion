from setuptools import setup
from setuptools import find_packages
extras = {}
extras["quality"] = ["black ~= 22.0", "isort >= 5.5.4", "flake8 >= 3.8.3"]
extras["docs"] = []
extras["test"] = [
    "pytest",
    "pytest-xdist",
    "pytest-subtests",
    "datasets",
    "transformers",
]
extras["dev"] = extras["quality"] + extras["test"]

extras["sagemaker"] = [
    "sagemaker",  # boto3 is a required package in sagemaker
]

setup(
    name="fusion",
    version="0.0.1",
    description="Diffusers",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="deep learning",
    license="MIL",
    author="SahilCarterr",
    author_email="patrick@huggingface.co",
    url="https://github.com/SahilCarterr/fusion",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.6.0",
    install_requires=["numpy>=1.17", "packaging>=20.0", "pyyaml", "torch>=1.4.0"],
    extras_require=extras,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
