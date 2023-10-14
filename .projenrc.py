from projen.python import PythonProject, VenvOptions

project = PythonProject(
    author_email="jacobpetterle@tai-tutor.team",
    author_name="Jacob Petterle",
    module_name="nl_adapters",
    name="nl-adapters",
    version="0.1.0",
)

project.synth()
