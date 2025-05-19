from setuptools import setup, find_packages

setup(
    name="thewatcher",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
        "rich>=10.0.0",
        "google-generativeai>=0.3.0",
        "groq>=0.4.0"
    ],
    entry_points={
        'console_scripts': [
            'thewatcher=terminal_monitor:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-Powered Terminal Error Monitor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/thewatcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 