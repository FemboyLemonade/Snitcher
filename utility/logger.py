import time

from sty import fg

from utility.get_time import get_time

class Logger:

    def print_success(message: str):

        """
        Print a success message to the console.
        """

        print(fg(27) + f"[ {get_time()} ] " + fg(2) + f"[ + ] {message}")
        return
    
    def print_info(message: str):

        """
        Print an information message to the console.
        """

        print(fg(27) + f"[ {get_time()} ] " + fg(15) + f"[ / ] {message}")
        return
    
    def print_warning(message: str):

        """
        Print a warning message to the console.
        """

        print(fg(27) + f"[ {get_time()} ] " + fg(3) + f"[ ! ] {message}")
        return
    
    def print_error(message: str):

        """
        Print an error message to the console.
        """

        print(fg(27) + f"[ {get_time()} ] " + fg(1) + f"[ - ] {message}")
        return