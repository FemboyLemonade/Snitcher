import argparse
import os
import sys

from reporter import ReportMessages
from utility.logger import Logger

from sty import fg, bg, ef, rs

class InitialiseProgram:

    def print_banner():

        """
        Print the banner to the console (CLI only).
        """

        with open("config/banner.txt", "r", encoding = "utf-8") as banner_file:
            banner = banner_file.read()

        print(fg(171) + f"{banner}")
        return

    def parser_error(error_message: str):

        """
        Call when a parser error is encountered.
        """

        InitialiseProgram.print_banner()
        Logger.print_error(f"There was an error: {error_message}")
        sys.exit()

    def parse_arguments():

        """
        Parse the command line arguments.
        """

        parser = argparse.ArgumentParser(epilog = "python snitcher.py -t token -g guild_id -u user_id")
        parser.error = InitialiseProgram.parser_error

        input_options_group = parser._optionals.title = "[ OPTIONS ]"
        parser.add_argument("-v", "--verbose", help = "Verbose output to the console", action = "store_true")
        parser.add_argument("-t", "--token", help = "The user token to report messages from", required = True)
        parser.add_argument("-g", "--guild", help = "The guild ID to report messages from", required = True)
        parser.add_argument("-u", "--user", help = "The user ID to report messages from", required = True)

        return parser.parse_args()
    
    def __init__(self, verbose: bool, token: str, guild_id: str, user_id: str):
        
        """
        The entry point for Snitcher.
        """

        InitialiseProgram.print_banner()
        print(fg(27) + f">> Verbose    : {verbose}")
        print(fg(27) + f">> Guild ID   : {guild_id}")
        print(fg(27) + f">> User ID    : {user_id}")
        print(fg(27) + f">> OS         : {"Windows" if os.name == "nt" else "Unix"}")
        print(fg(171) + "--------- Reporting Messages ---------")

        reporter = ReportMessages()
        reporter.fetch_messages(verbose, token, user_id, guild_id)

if __name__ == "__main__":

    os.system("cls" if os.name == "nt" else "clear")
    os.system("title Snitcher" if os.name == "nt" else "echo '\033]0;Snitcher\007'")

    arguments = InitialiseProgram.parse_arguments()

    verbose = arguments.verbose
    token = arguments.token
    guild_id = arguments.guild
    user_id = arguments.user

    InitialiseProgram(verbose, token, guild_id, user_id)