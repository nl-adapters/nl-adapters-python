from projen import ProjectType
from projen.python import (
    PythonProject,
    PoetryPyprojectOptionsWithoutDeps,
)


project = PythonProject(
    author_email="jacobpetterle@tai-tutor.team",
    author_name="Jacob Petterle",
    module_name="nl_adapters",
    name="nl-adapters",
    version="0.1.0",
    project_type=ProjectType.LIB,
    poetry=True,
    description="A library that provides a natural language interface for python code.",
    deps=[
        "python@>=3.8.1,<4",
        "langchain@>=0.0.314",
    ],
    dev_deps=[
        "projen@>=0.74.17",
    ]
)


project.synth()
