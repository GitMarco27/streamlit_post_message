import os

from setuptools import find_packages, setup


# Function to read the README file.
def read(fname):
    """
    Reading fname
    """
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()


# Package setup
setup(
    name="streamlit_post_message",
    version="0.1.0",
    author="Your Name",
    author_email="marco.sanguineti.info@gmail.com",
    description="A Streamlit component for postMessaging between a parent and child window",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/GitMarco27/streamlit_post_message",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "streamlit_post_message": ["*.js"],
    },
    install_requires=[
        line.strip() for line in open("requirements.txt", encoding="utf-8")
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
