import sys              #to access exception information
import logging



def error_message_details(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"error occurred in python script name: {file_name}, line number: {exc_tb.tb_lineno}, error message: {str(error)}"

    return error_message



class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message


# test
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info('divide by zero test error')
#         raise CustomException(e, sys)