from setuptools import setup, find_packages

setup(
    name="plexcontentmanager",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "plexapi",
        "click",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "plexcontent=plexcontentmanager.cli:main",
        ],
    },
)
