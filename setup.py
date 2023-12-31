## setup.py is a package of our project


from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = list(filter(lambda x: x.strip() != '-e .', requirements))
    return requirements


setup(
    name="mlproject",
    version='0.0.1',
    author="Vaibhav",
    author_email="vaibhavreddyv02@gmail.com",
    packages=find_packages(include=['mlproject', 'mlproject.*']),
    install_requires=get_requirements("requirements.txt"),
    # Add a long description if needed
    long_description="Your long description here.",
    long_description_content_type="text/markdown",  # Change accordingly
)
