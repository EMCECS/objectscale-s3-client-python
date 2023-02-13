'''
Copyright 2022 Dell Technologies. All Rights Reserved.

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
#import boto3
import botocore
import os
#from boto3.session import Session
from botocore.session import Session
from botocore.loaders import Loader

#boto3.DEFAULT_SESSION = None
SEARCH_PATH = os.path.join(os.path.dirname(__file__), 'data')

def obs_setup_default_session(**kwargs):
    print("DEFAULT SESSION FUNCTION OVERWRITTEN")
    boto3.DEFAULT_SESSION = Session(**kwargs)
    boto3.DEFAULT_SESSION._loader.search_paths.append(SEARCH_PATH)
    paths = boto3.DEFAULT_SESSION._loader.search_paths
    paths = "path"

def obs_create_loader(search_path_string=SEARCH_PATH):
    if search_path_string is None:
        return Loader()
    paths = []
    extra_paths = search_path_string.split(os.pathsep)
    for path in extra_paths:
        path = os.path.expanduser(os.path.expandvars(path))
        paths.append(path)
    return Loader(extra_search_paths=paths)

def obs_register_data_loader(self):
        self._components.lazy_register_component(
            'data_loader',
            lambda: botocore.loaders.create_loader(SEARCH_PATH),
        )

def obs_load_service_model(self, service_name, type_name, api_version=None):
    # Wrapper around the load_data.  This will calculate the path
    # to call load_data with.
    known_services = self.list_available_services(type_name)
    if service_name not in known_services:
        raise UnknownServiceError(
            service_name=service_name,
            known_service_names=', '.join(sorted(known_services)),
        )
    if api_version is None:
        api_version = self.determine_latest_version(
            service_name, type_name
        )
    full_path = os.path.join(service_name, api_version, type_name)
    model = self.load_data(full_path)

    # Load in all the extras
    extras_data = self._find_extras(service_name, type_name, api_version)
    self._extras_processor.process(model, extras_data)

    if service_name == "s3":
        api_version = "2023-2-11"
        #full_path = os.path.join(service_name, api_version, type_name)
        #model = self.load_data(full_path)
        extras_data = self._find_extras(service_name, type_name, api_version)
        self._extras_processor.process(model, extras_data)

    return model

def obs_client(
        self,
        service_name="obs",
        region_name=None,
        api_version=None,
        use_ssl=True,
        verify=None,
        endpoint_url=None,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        aws_session_token=None,
        config=None,
    ):
        return self._session.create_client(
            service_name,
            region_name=region_name,
            api_version=api_version,
            use_ssl=use_ssl,
            verify=verify,
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            config=config,
        )

Session._register_data_loader = obs_register_data_loader
Loader.load_service_model = obs_load_service_model
#botocore.loaders.create_loader = obs_create_loader
#boto3.setup_default_session = obs_setup_default_session
#boto3.Session.client = obs_client