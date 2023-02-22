#!/bin/sh

cp service-2.sdk-extras.json ~/.aws/models/s3/2006-03-01/service-2.sdk-extras.json
python3 query.py
