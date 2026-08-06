import time

from sty import fg
from pathlib import Path

from utility.get_time import get_time

Path("logs").mkdir(parents = True, exist_ok = True)
output_file_name = f"logs/{time.time()}" + "-snitcher-logs.txt"
output_logs = open(output_file_name, "w", encoding = "utf-8")

class FileManager:

    def write_to_file(message: str):

        """
        Write console logs to a logs file.
        """

        logging_message = f"[ {get_time()} ] " + message
        output_logs.write(logging_message)
        return
    
    def close_logs_file():

        """
        Close the logs file stream when killing the program.
        """

        output_logs.close()
        return

class Logger:

    def print_success(message: str):

        """
        Print a success message to the console.
        """

        print(fg(27) + f"[ {get_time()} ] " + fg(2) + f"[ + ] {message}")
        FileManager.write_to_file(message)
        return
    
    def print_info(message: str):

        """
        Print an information message to the console.
        """

        print(fg(27) + f"[ {get_time()} ] " + fg(15) + f"[ / ] {message}")
        FileManager.write_to_file(message)
        return
    
    def print_warning(message: str):

        """
        Print a warning message to the console.
        """

        print(fg(27) + f"[ {get_time()} ] " + fg(3) + f"[ ! ] {message}")
        FileManager.write_to_file(message)
        return
    
    def print_error(message: str):

        """
        Print an error message to the console.
        """

        print(fg(27) + f"[ {get_time()} ] " + fg(1) + f"[ - ] {message}")
        FileManager.write_to_file(message)
        return