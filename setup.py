from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(name='myapp',
    version='0.0.1',
    packages=find_packages(),
    nane='ml-project',
    author='Sharad',
    author_email='sharadgarg2000gupta@gmail.com',
    install_requires=get_requirements('requirements.txt')
)