#!/usr/bin/python
from slackclient import SlackClient
import json
import re
import leds
import sys
from slackBambooMsgParser import slackBambooMsgParser
import json

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
    msgParser = slackBambooMsgParser(msg)
    #print curMsg.getMsg()
    if not msgParser.isValid():
	continue
    if msgParser.getBambooProjectName() != "ClearCare":
	continue

    if ( msgParser.getUser() == "Bamboo" ) or ( msgParser.getUser() == "incoming-webhook" ):
        if msgParser.isFeatureBranch():
            continue

        if msgParser.isJobPassed():
            failedjobs.discard(msgParser.getBambooPlanName())
        else:
            failedjobs.add(msgParser.getBambooPlanName())
            #NOTE: May need to add logic for so that grey messages don't get used
            #        msg["attachments"][0]["color"] == RED:
    else:
        continue

if len(failedjobs) == 0:
    leds.setColorByRGB(0,255,0)
else:
    leds.setColorByRGB(255,0,0)

#print '--------- failures -----------'
#for plan in failedjobs:
#    print plan

#print len(failedjobs)
