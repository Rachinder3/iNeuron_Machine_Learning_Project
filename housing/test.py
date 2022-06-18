REQUIREMENT_FILE_NAME = "requirements.txt"
from typing import List

def get_requirements_list() -> List[str]:# -> List[str] means we will return a list of strings.  It is a good practice to do this
    """
    Description: This function is going to return list of requirement
    
    returns: This function is going to return a list which contains name of libraries
    mentionaed in requirements.txt
    """
    
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        test = requirement_file.readlines()
        test.pop()
        test1 = [x.replace("\n","") for x in test]
        return test1
        
    
if __name__=='__main__':
    print(get_requirements_list())
