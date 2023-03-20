from setuptools import find_packages, setup


setup(
    name = "obs-s3-client",
    version = "0.0.28",
    description = "Open-source S3 client library in python to support ObjectScales proprietary S3 extensions",
    author = "Drayer Sivertsen",
    classifiers = [ 'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3.10',
    'Topic :: Software Development :: Libraries' ],
    keywords = [ 'ObjectScale', 'S3', 'Dell', 'boto3', 'botocore' ],
    dependencies = [ 'boto3' ],
    packages = find_packages()
)