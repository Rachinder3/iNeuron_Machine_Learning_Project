import os
import sys

## Creating our custom exception

class Housing_Exception(Exception):

    def __init__(self, error_message : Exception, error_deatils : sys):
        ## error_message : Exception, tells that datatype of error_message datatype is Exception
        ## whenever we run our code, sys module keeps track of any error and all the information related to it
        super().__init__(error_message) # passing the error_message to exception class

        self.error_message = Housing_Exception.get_detailed_error_message(error_message=error_message, error_detail=error_deatils)
        

    @staticmethod
    def get_detailed_error_message(error_message : Exception, error_detail:sys)->str:
        """
            error_messgae : Exception object
            error_detail : object of sys module
        """
        _,_,exec_tb = error_detail.exc_info() # returns type, value, traceback. This fn call returns info about most recent exception
        
        line_number = exec_tb.tb_frame.f_lineno  # line no which is causing the error
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script L [{file_name}] at line number: [{line_number}] error message : [{error_message}]" 


        return error_message ## returning Exception as message_type is Exception

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return Housing_Exception.__name__.str()

