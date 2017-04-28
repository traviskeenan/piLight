import types
import json
import re

class slackBambooMsgParser(object):

	def __init__(self, message):
		if ( type(message) is types.DictType ):
			self.message = str(message)
		else: 
			self.message = message

		self.jsonMsg = json.loads(self.message.replace("u\'","\'").replace("\'","\""))

	def getUser(self):
		return self.jsonMsg["username"]

	def getMsg(self):
		return self.message

	def isJobPassed(self):
		successRegex = re.compile(".*passed.*")
		if successRegex.match( self.jsonMsg["attachments"][0]["fallback"] ):
			return True

		return False

	def isValid(self):
		vaild = False
		if ( 'username' in self.jsonMsg ) and ( 'attachments' in self.jsonMsg ):
			vaild = True
		else:
			vaild = False

		return vaild

	def getBambooProjectName(self):
		return self.jsonMsg["attachments"][0]["fallback"].split(u' \u203a ')[0]

	def getBambooPlanName(self):
		return self.jsonMsg["attachments"][0]["fallback"].split(u' \u203a ')[1]

	def isFeatureBranch(self):
		buildNumberRegex = re.compile("^#.*")
		if not buildNumberRegex.match(self.jsonMsg["attachments"][0]["fallback"].split(u' \u203a ')[2]):
			return True

		return False
