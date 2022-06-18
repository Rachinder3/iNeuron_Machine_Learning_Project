from setuptools import setup, find_packages
from typing import List



#### Declaring variables for setup functions
PROJECT_NAME = "housing predictor"
VERSION = "0.0.9"
AUTHOR = "Rachinder Singh" 
DESCRIPTION = "This is the first  FSDS November Batch Project"
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:# -> List[str] means we will return a list of strings.  It is a good practice to do this
    """
    Description: This function is going to return list of requirement
    
    returns: This function is going to return a list which contains name of libraries
    mentionaed in requirements.txt
    """
    
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        
        return requirement_file.readlines()
        


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), ## looks for all the packages and returns as a list
    install_requires = get_requirements_list()
)


## check if get_requirements_list fun is working or not
## write command: python setup.py install. Now we don't need to 
## write pip install -r requirements.txt
