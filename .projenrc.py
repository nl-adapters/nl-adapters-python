from projen.python import PythonProject

project = PythonProject(
    author_email="jacobpetterle@gmail.com",
    author_name="Jacob Petterle",
    module_name="nl_adapters_python",
    name="nl-adapters-python",
    version="0.1.0",
)

project.synth()