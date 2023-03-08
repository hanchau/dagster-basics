from setuptools import find_packages, setup

setup(
    name="dagster_basics",
    packages=find_packages(exclude=["dagster_basics_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas",
        "requests"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
