# setup.py
from setuptools import setup, find_packages

setup(
    name="daily-productivity-assistant",
    version="1.0.0",
    author="Edwin Kestler",
    description="A personal productivity tool with Pomodoro tracking, planning prompts, and weekly reporting.",
    packages=find_packages(),
    install_requires=[
        "contourpy==1.3.1",
        "cycler==0.12.1",
        "fonttools==4.56.0",
        "kiwisolver==1.4.8",
        "matplotlib==3.10.1",
        "numpy==2.2.4",
        "packaging==24.2",
        "pillow==11.1.0",
        "plyer==2.1.0",
        "pyparsing==3.2.3",
        "python-dateutil==2.9.0.post0",
        "schedule==1.2.2",
        "six==1.17.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11.9',
    entry_points={
        'console_scripts': [
            'productivity-assistant=main:run'
        ]
    },
    include_package_data=True,
)
