from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def getrequirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPHEN_E_DOT]
    return requirements

setup( 

    name='mlproject',
    version='0.0.1',
    author='Biswadip Banerjee',
    author_email='biswadip5143@gmail.com',
    packages=find_packages(),
    install_requires=getrequirements('requirements.txt')
    
)