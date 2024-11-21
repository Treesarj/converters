# setup.py
from setuptools import setup, find_packages

setup(
    name="mypackage",  # Name of your package
    version="0.1.0",  # Initial version
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[  # Dependencies of your package
        'numpy',
        # Example: 'requests',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/mypackage",  # URL to the package's source code
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
