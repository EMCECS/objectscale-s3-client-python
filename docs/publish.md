# Publishing Python S3 Library

Detailed here is the method by which this library extension will be published. The publishing repository that we will be using is PyPI, the open source Python packaging index. Publishing the library here will allow for availability amoung Dell's clients. This library will be called PyscaleS3. We will keep the package name and the name in PyPI the same for the sake of consistency. 

### Configuration

The build system and the package itself must be configured before the library is published. This is done through the use of a pyproject.toml file. The build system that will be used is setuptools, and in the file, this build configuration can be specified in the build-system section. It is best practice to place the build directory into a file called /src. This section specifies what dependencies will be necessary for building the package.

To configure the package, the project section must assign values to various fields. Most of these fields are optional (all but name and version), but the rest are necessary to fill in for the purposes of the project. The library is more attractive and findable on PyPI with these fields filled in, and this in turn ensures maximal convienience for the clients.

The remaining sections are also optional but necessary for the reasons listed above. The optional dependencies section includes notable dependencies that are supported in the library but not required. This can also inlude any dependancies used during development, like testing frameworks. The urls section includes any important urls that the user might need. Since this project will eventually transition to open source it is important that the link to the Github repository of the library is included so users can have easy and convienient access. The scripts section includes any command line arguments that can be invoked using the library as well as the functions that they call in the package. The entry-points and gui-scripts sections can also be included, though they may not be necessary depending on the inclusion of plugins and GUI.

Virtual environment and pip tools can be used to manage dependencies effectively

```
[build-system]
requires      = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "PyscaleS3"
version = "1.0.0"
description = "Description of library"
readme = "README.md"
authors = [ **List of authors** ]
license = { **License file** }
classifiers = [ *List of classifiers** ]
keywords = [ **List of keywords** ]
requires-python = ">=3.9"
dependencies = [ **List of necessary dependencies** ]
# ">= version" specifies the lowest version needed for the package
# "; python_version < version" specifies the dependency is only needed under a specified python version


[project.optional-dependencies]
dev = [ **List of optional dependencies** ]

[project.urls]
Homepage = "https://github.com/EMCECS/objectscale-s3-client-python"

[project.scripts]
<command_line_function> = <script call>
...
```

### Testing and Documentation

The main functionality will be published as implemented here. But more items outside of the main functionality need to be included. Documentation with installation instructions, tutorials, and API references must be included in the publication. These must be detailed descriptions that help the user understand how to effectively use the product. The documentation can either be included in the publication on PyPI or hosted on a separate site. 

Unit testing is necessary for the development of this library, but it should not be included in the publication. Testing is needed for the developers to confirm the quality of the code before it is shipped, but not needed for the functionality of the library itself, and should not be used by the clients.

### Versioning

Versioning is needed for our work on the project. It helps users and developers keep track of updates to the software, and can allow for easy knowledge of what is in development and what is in production. PyPI doesn't allow multiple publishings of a package with the same version. If any updates are to be made to the package while it is published, a versioning scheme must be implemented. For now, semantic versioning will suffice. This is composed of three components, being the Major, Minor, and Patch components. Major must be incremented when non-backwards-compatible functionality is implemented. Minor must be incremented when backwards-compatible functionality is implemented. Patch must be incremented when backwards-compatible bug fixes are implemented. 

Bumpver can be used to track versions of the project. The bumpver init command will configure this tool to the project, and produce more configuration specifications in the .toml file. This tool keeps version numbering consistent throughout the project and integrates with git, automatically commiting, flagging, and pushing on version updates.

```
[tool.bumpver]
current_version = "1.0.0"
version_pattern = "MAJOR.MINOR.PATCH"
commit_message  = "Bump version {old_version} -> {new_version}"
commit          = true
tag             = true
push            = false

[tool.bumpver.file_patterns]
"pyproject.toml" = ['current_version = "{version}"', 'version = "{version}"']
"src/reader/__init__.py" = ["{version}"]
```

Incrementing version can be done through a simple command line argument. Flags --minor, --major, and --patch can be used to update their respective version components. The --dry flag can be used to view changes of an action and not actually preform the changes.

`bumpver update --minor`

### Resource Files and Licensing

Many files that are not source code files are not included in the project build by default. To include these files, a maifest file is necessary, detailing which files to include and exclude in the build. This file needs to be titled MANIFEST.in and it must be included in the base directory of the project. The files to be put in the manifest file must at least include the configuration pyproject.toml file. Depending on weather or not documentation is to be hosted with the repository or in a separate place, documentation files also must be included in the manifest file. This is done through a series of include statements.

`include src/PyscaleS3/*.toml`

For others to use the libraries, a license must also be included. This details how others are legally allowed to use and modify the product. This is a legal document that should not be written by the team. This license may be found online or provided by the client. The project is intended to be open-source, so a license appropriate for this framework must be acquired. This is to be included in a file titled LICENSE and included in the configuration file under the license field for visibility in PyPI.

### Publishing

Finally, the package must be built and uploaded to PyPI. To do this, an account on PyPI must be created. Also, two tools must be installed, those being Build and Twine. These can simply be installed through pip. Now, the project must be wrapped into a Python wheel and a zip archive containing the code. The wheel is a more user-convienient and flexible method for accessing the code, and the archive is used for backup. Using the following command, the output should show both the wheel and the archive being created:

`python -m build`
```
PyscaleS3/
|
|__ dist/
    |__ PyscaleS3-1.0.0-py3-none-any.whl
    |__ PyscaleS3-1.0.0.tar.gz
```

It can be verified that the packages have the correct files by inspecting them. The wheel can be given a .zip extension and simply depackaged to view the files. If the files in the package look correct, the package is in a state where it can be uploaded to PyPI. Here, TestPyPI is a good tool for testing the upload. By registering a TestPyPI account and using the command below, the library can be check to see if everything renders properly and nothing is excluded without consequence:

`twine upload -r testpypi dist/*`

Once the library has been prepared for publication, the following command will upload packages to PyPI for anyone to use:

`twine upload dist/*`