from setuptools import find_packages, setup

setup(
    name="espnapi",
    packages=find_packages(include=["espnapi"]),
    version="0.0.1",
    description="An ESPN API wrapper",
    author="Carter",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
