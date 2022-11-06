# Contributing to our Project
We appreciate contributions to the objectscale-s3-client-python library and its documentation.

## Introduction

A Dell project maintainer will be responsible for accepting contributions but only if they adhere to the Developer's Certificate of Origin 1.1 which can be found at https://developercertificate.org. 

## Getting Started
---
### Issues
#### Create a new issue
If you locate a bug in the code or a problem with the docs, search if the issue already exists. If a related issue does not exist, you can open a new issue. Please describe the issue in detail and mark the issue with relevant tags.

#### Solve an issue
If you identify a issue that you would like to fix comment on the issue to show others that you are assigning the issue to yourself.

Fork the main branch so you have a repository on your Github called username/objectscale-s3-client-python.

After finishing all your commits compress them into a single commit and make a new pull request comparing your repo username/objectscale-s3-client-python to the main repo. 

If a Dell project maintainer reviews your pull request solving the issue and adheres to the Developer's Certificate of Origin 1.1, the request will be accepted!

### Developer Certificate of of Origin
Contributions can agree to the DCO by using a signed-off-by line at the end of each commit message. An example of this message is as follows:

```
Signed-off-by: Drayer Sivertsen <drayer.sivertsen@email.com>
```

This message can be added to your commit message. However, Git supports a much easier way to add this to your commit messages. 

If you set up "user.name" and "user.email" as part of your git configuration, you can sign each commit by just using: 
```
git commit -s
```

Configuring git can be done using the commands:
```
//add username
git config --global user.name "your_username"

//add email
git config --global user.email "your_email_address@example.com"
```

The below text of the DCO is from https://developercertificate.org:
```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```


## Copyright
---
All source files need to include a Copyright header in the top of the file. The header will consist of the following:
```
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
```
(Python Comment Block)