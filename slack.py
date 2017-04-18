#!/usr/bin/python
from slackclient import SlackClient
import json
import re
import leds
import sys

RED = "d00000"
GREEN = "36a64f"
GREY = "707070"

slack_token = ''
sc = SlackClient(slack_token)

response = sc.api_call(
  "channels.history",
  channel="C3K3PGK8B"
  #,oldest="1482945405.000000"
  #,latest="1482956093.000006"
)

failedjobs = set([])

for msg in reversed(response["messages"]):
    # print "MSG:"
    # print msg
    # print ""
    if "username" not in msg:
        continue
    if "attachments" not in msg:
        continue
    # Only look for the projects that we are interested in
    if "ClearCare" not in msg:
        continue

    if ( msg["username"] == "Bamboo" ) or ( msg["username"] == "incoming-webhook" ):
        messageText = msg["attachments"][0]["fallback"]
        parts = messageText.split(u' \u203a ')
        plan = parts[1]
        # See if parts[2] has a build number, which indicates it's the dev branch.  Otherwise parts[2] is the branch name, and parts[3] has the build number.
        buildNumberRegex = re.compile("^#.*")
        if not buildNumberRegex.match(parts[2]):
            continue
        
        successRegex = re.compile(".*passed.*")
        if successRegex.match(messageText):
            failedjobs.discard(plan)
        else:
            if msg["attachments"][0]["color"] == RED:
                failedjobs.add(plan)
    else:
        continue

if len(failedjobs) == 0:
    leds.setColorByRGB(0,255,0)
else:
    leds.setColorByRGB(255,0,0)

# print '--------- failures -----------'
#for plan in failedjobs:
#    print plan
#
#print len(failedjobs)
