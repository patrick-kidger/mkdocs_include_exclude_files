import pathlib
import re

import setuptools


_here = pathlib.Path(__file__).resolve().parent

name = "mkdocs_include_exclude_files"

# for simplicity we actually store the version in the __version__ attribute in the
# source
with open(_here / name / "__init__.py") as f:
    meta_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if meta_match:
        version = meta_match.group(1)
    else:
        raise RuntimeError("Unable to find __version__ string.")

author = "Patrick Kidger"

author_email = "contact@kidger.site"

description = "Modify which files MkDocs includes or excludes."

with open(_here / "README.md", "r") as f:
    readme = f.read()

url = "https://github.com/patrick-kidger/" + name

license = "Apache-2.0"

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
]

python_requires = "~=3.8"

install_requires = ["mkdocs>=1.2.3"]

entry_points = {
    "mkdocs.plugins": [
        "include_exclude_files = mkdocs_include_exclude_files:IncludeExcludePlugin"
    ]
}

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    url=url,
    license=license,
    classifiers=classifiers,
    zip_safe=False,
    python_requires=python_requires,
    install_requires=install_requires,
    packages=[name],
    entry_points=entry_points,
)
