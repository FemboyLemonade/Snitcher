# Snitcher - Mass Discord Reporter

## What is Snitcher?

Snitcher is a tool used to mass report a Discord account via bannable words sent in messages. The tool automatically scrapes every single message sent by the targetted user and combs through them to see if any of the words match a blacklisted word in the bad word dump.

## How to use Snitcher?
```
 _____       _ _       _               
/  ___|     (_) |     | |              
\ `--. _ __  _| |_ ___| |__   ___ _ __ 
 `--. \ '_ \| | __/ __| '_ \ / _ \ '__|
/\__/ / | | | | || (__| | | |  __/ |   
\____/|_| |_|_|\__\___|_| |_|\___|_|

usage: snitcher.py [-h] [-v] -t TOKEN -g GUILD -u USER

[ OPTIONS ]:
  -h, --help         show this help message and exit
  -v, --verbose      Verbose output to the console
  -t, --token TOKEN  The user token to report messages from
  -g, --guild GUILD  The guild ID to report messages from
  -u, --user USER    The user ID to report messages from

python snitcher.py -t token -g guild_id -u user_id
```

