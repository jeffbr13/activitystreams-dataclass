import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="activitystreams-dataclass",
    version="0.0.2",
    author="Ben Jeffrey",
    author_email="mail@benjeffrey.net",
    description="Dataclasses for ActivityStreams objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeffbr13/activitystreams-dataclass",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ),
)
