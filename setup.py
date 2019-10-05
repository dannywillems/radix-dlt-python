from setuptools import setup, find_packages

excluded_packages = ['tests']

setup(
    name='radixdlt',

    version='0.0.1',

    description='Library for Radix DLT',
    long_description="Library for Radix DLT",

    url='https://github.com/dannywillems/radix-dlt-python',

    author='Danny Willems',
    author_email='contact@danny-willems.be',

    packages=find_packages(exclude=excluded_packages),

    setup_requires=['pytest-runner'],
    tests_require=["pytest", "pytest-cov", "flexmock", "factory-boy", "pytest-lazy-fixture"],
    install_requires=[
        "base58==1.0.3",
        'enum34==1.1.6;python_version<"3.4"',
        "pathlib2==2.3.3",
        "requests",
        "secp256k1==0.13.2",
        'six==1.11.0',
        "websocket-client==0.56.0",
    ],
)
