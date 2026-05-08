from setuptools import setup, find_packages

setup(
    name="task-turbo-agile-20260507_194929",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'task=task:main',
        ],
    },
)
