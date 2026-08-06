import json
import re
import time

from curl_cffi import requests

from utility.logger import Logger

class ReportMessages:

    def __init__(self):

        with open("config/report_words.txt", "r", encoding = "utf-8") as bad_word_file:
            lines = bad_word_file.readlines()

        self.bad_words = lines

    def fetch_messages(self, verbose: bool, token: str, user_id: str, guild_id: str):

        """
        Fetch all messages from a user in a guild provided its ID.
        """

        offset = 0

        headers = {

            "Authorization": token,
            "Content-Type": "application/json"

        }

        while True:

            time.sleep(5)

            URL = f"https://discord.com/api/v9/guilds/{guild_id}/messages/search?author_id={user_id}&sort_by=timestamp&sort_order=desc&offset={offset}"

            response = requests.get(URL, headers = headers, impersonate = "firefox")

            response_json = response.json()

            if "message" in response_json:
                if response_json["message"] == "Missing Access":
                    Logger.print_error(f"The account with the provided token does not exist in the guild with ID {guild_id}")
                    return

            total_messages = response_json["total_results"]

            messages = response_json["messages"]

            if not messages:
                if verbose:
                    Logger.print_error(f"No messages were fetched from offset = {offset}")
                break

            for message_group in messages:
                for message in message_group:
                    for word in self.bad_words:
                        word = word.strip()
                        if re.search(rf"\b{re.escape(word)}\b", message["content"], re.IGNORECASE):
                            Logger.print_info(f"Found {word} in message: \"{message["content"]}\"")
                            channel_id = message["channel_id"]
                            message_id = message["id"]
                            self.report_message(token, channel_id, message_id, message["content"])
                            time.sleep(0.5)

            offset += 25

    def report_message(self, token: str, channel_id: str, message_id: str, message_content: str):

        """
        Report a message.
        """

        URL = "https://discord.com/api/v9/reporting/message"
        
        headers = {

            "Authorization": token,
            "Content-Type": "application/json"

        }

        payload = {

            "version": "1.0",
            "variant": "8",
            "language": "en",
            "breadcrumbs": [7, 98],
            "elements": {},
            "channel_id": channel_id,
            "message_id": message_id,
            "name": "message"

        }

        response = requests.post(URL, headers = headers, json = payload, impersonate = "firefox")

        if response.status_code != 200:
            Logger.print_error(f"Failed to report the message \"{message_content}\": HTTP code {response.status_code}")
            return

        Logger.print_success(f"Successfully reported the message \"{message_content}\"")