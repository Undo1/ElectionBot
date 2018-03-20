import getpass
import logging
import os
import time
import urllib
import sys
from subprocess import call

import ChatExchange.chatexchange
from ChatExchange.chatexchange.events import MessageEdited

logging.captureWarnings(True)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

logging.basicConfig(level=logging.CRITICAL)

if 'ChatExchangeU' in os.environ:
    email = os.environ['ChatExchangeU']
else:
    email = input("Email: ")
if 'ChatExchangeP' in os.environ:
    password = os.environ['ChatExchangeP']
else:
    password = getpass.getpass("Password: ")
client = ChatExchange.chatexchange.Client('stackexchange.com', email, password)

input(bcolors.BOLD + bcolors.OKGREEN + "Connection good." + bcolors.ENDC + bcolors.BOLD + " [Enter] to proceed getting results for " + sys.argv[1] + " election #" + sys.argv[2] + "..." + bcolors.ENDC)

urllib.request.urlretrieve("https://" + sys.argv[1] + "/election/download-result/" + sys.argv[2], "votes.blt")

result = os.popen("python openstv/openstv/runElection.py MeekSTV votes.blt").read()

os.remove("votes.blt")

result_indented = ""

for string in result.splitlines():
    result_indented = result_indented + "    " + string + "\n"

print(result_indented)

winners_line = "**Unofficial results**: " + result_indented.splitlines()[-1]

okay_to_post = input("Okay to post? ")
if okay_to_post.lower() == "" or okay_to_post.lower == "y":
    for room in sys.argv[3].split(","):
      sandbox = client.get_room(room)
      sandbox.send_message(winners_line)
      sandbox.send_message(result_indented, False)

    time.sleep(10)
