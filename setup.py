from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
#function to trigger requirements
def get_requirements(file_path:str)->List[str]:
    '''
    this is a function to trigger requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.strip() for req in requirements if req.strip()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

        


#setting up basics 
setup(
    name='mlproject',
    version='0.0.0.1',
    author='Karthik',
    author_email='Karthikramesh1813@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)