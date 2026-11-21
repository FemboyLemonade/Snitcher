# Snitcher

Snitcher is a mass Discord message reporting tool. Give it an account token, a guild ID and a target user ID, and it will scrape **every message** that user has sent in the guild, comb through them against a blacklist of bannable words (`config/report_words.txt`), and automatically report every message that matches.

## Features

- Scrapes all messages from a target user in a guild using Discord's search API
- Matches messages against a fully customizable blacklist of words (case-insensitive, whole-word matching)
- Reports every matching message straight to Discord's reporting endpoint
- Configurable delay between requests to stay under rate limits
- Colorful console output with timestamps, plus everything logged to a file in `logs/`
- Cross-platform (Windows / Unix) — uses `curl_cffi` with browser impersonation to look like a real Firefox client

## Requirements

- [Python](https://www.python.org/downloads/) 3.x
- A Discord user token
- The ID of the guild the target user has been active in
- The ID of the target user

## Getting Your Token

Snitcher authenticates with a Discord **user token**. Here's how to grab your own:

1. Log in to Discord — either in the browser at [discord.com](https://discord.com) or in the desktop app.
2. Open Developer Tools with `Ctrl + Shift + I` (`Cmd + Option + I` on macOS).
3. Switch to the **Network** tab.
4. Trigger some traffic — switch channels or send any message.
5. Click any request sent to `discord.com/api/...`.
6. Under **Request Headers**, copy the value of `Authorization`. That long string is your token.

> - The token is case-sensitive — copy it exactly as-is, without quotes.
> - Your token is effectively your account password: anyone who has it has full access to your account. Never share it or commit it to version control.
> - Automating a user account ("self-botting") violates [Discord's Terms of Service](https://discord.com/terms) and can get the account banned.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tomas/Snitcher.git
cd Snitcher
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```
usage: snitcher.py [-h] [-v] -t TOKEN -g GUILD -u USER [-s SLEEP]
```

| Option | Description | Default |
| --- | --- | --- |
| `-h`, `--help` | Show the help message and exit | — |
| `-v`, `--verbose` | Verbose output to the console | off |
| `-t`, `--token TOKEN` | The user token to fetch and report messages with (**required**) | — |
| `-g`, `--guild GUILD` | The guild ID to search messages in (**required**) | — |
| `-u`, `--user USER` | The user ID whose messages will be scanned (**required**) | — |
| `-s`, `--sleep SLEEP` | Delay (in seconds) between requests | `5` |

Example:

```bash
python snitcher.py -t <token> -g <guild_id> -u <user_id>
```

With custom settings:

```bash
python snitcher.py -t <token> -g <guild_id> -u <user_id> -v -s 10
```

## Configuration

Everything lives in the [`config/`](config/) directory:

- **`report_words.txt`** — the blacklist used when scanning messages, one word per line. Any message from the target containing one of these words (case-insensitive, as a whole word) gets reported. Add or remove words freely.
- **`banner.txt`** — the ASCII banner printed on startup. Change it if you want a different look.

## How It Works

1. Snitcher loads the word blacklist from `config/report_words.txt`.
2. It pages through Discord's guild message search API (`author_id=<user>`), 25 results at a time, until there are no messages left.
3. Every fetched message is checked against the blacklist with case-insensitive whole-word regex matching.
4. Each match is reported to Discord's `/reporting/message` endpoint, then the script moves on after the configured sleep delay.
5. When everything has been processed, you get a summary of how many messages were reported.

If the provided token does not have access to the guild (e.g. the account isn't in it), Snitcher exits with a clear error instead of hammering the API.

## Disclaimer

This tool is intended for **educational purposes only**. Mass-reporting accounts violates [Discord's Terms of Service](https://discord.com/terms), and misusing this tool can get your own account suspended or banned. You are solely responsible for whatever you do with it.
