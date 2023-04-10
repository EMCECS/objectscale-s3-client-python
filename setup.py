'''
Copyright (c) 2021 Dell Inc., or its subsidiaries. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file execpt in compliance with License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and
limitations under the License.
'''

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