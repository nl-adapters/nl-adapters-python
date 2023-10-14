from projen.python import PythonProject, VenvOptions, PoetryPyprojectOptionsWithoutDeps 


AUTHORS = [
    "Jacob Petterle",
]
project = PythonProject(
    author_email="jacobpetterle@tai-tutor.team",
    author_name=AUTHORS[0],
    module_name="nl_adapters",
    name="nl-adapters",
    version="0.1.0",
    poetry=True,
    description="A library that provides natural language interfaces for any python code.",
)

project.synth()
