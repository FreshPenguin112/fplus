from setuptools import setup, find_packages
setup(
    name="fplus",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fplus = fplus.__main__:main'
        ]
    }
)