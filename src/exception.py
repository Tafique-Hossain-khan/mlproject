import sys

def custom_exception_handeling(error,error_detail:sys):

    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error accure in pyhton script name [{0}] line numbrer[{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) 
        self.error_message = custom_exception_handeling(error_message,error_detail)

    def __str__(self) -> str:
        return self.error_message
        


if __name__ == '__main__':

    try:
        a =1/0
    except Exception as e:
       raise CustomException(e,sys)
        



