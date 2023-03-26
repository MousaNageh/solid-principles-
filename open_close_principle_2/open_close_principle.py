"""
software entities (classes, modules, functions, and so on) should be open for extension, but closed for modification.
example :
need to write error into error file.
we will use inhertance 
"""
import sys
sys.path.append('/media/mousa/code5/study/solid-principles-/')

from single_responsability_1.single_responsability import Logger


class ErrorLogger(Logger):

    def write_error_to_file(self,merrage):
        with open("error.txt",'a') as writer:
            writer.write(merrage+"\n")
            writer.flush()

from datetime import datetime 

try:
    a = int(input("enter numer 1 : "))
    b = int(input("enter numer 2 : "))
    res = a / b 
    print(res) 
except Exception as e :
    message = f"{str(e)} --- at time -- {datetime.now()}"
    e = ErrorLogger()
    e.write_error_to_file(merrage=message)
    e.write_log_to_system(messsage=message)
    print(message)