from setuptools import setup, find_packages

setup(
    name="convo-cli",
    version="0.1.0",
    description="Terminal conversation logger and analyzer",
    author="Heemansh Bhawsar",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'convo=convo:main',
        ],
    },
    include_package_data=True,
)

