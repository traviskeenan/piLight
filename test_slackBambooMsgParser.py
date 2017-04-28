import unittest
from slackBambooMsgParser import slackBambooMsgParser

class TestSlackBambooMsgParser(unittest.TestCase):

	# def successMsg = {u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/browse/CLEAR-CAR-47|ClearCare \u203a CareGap \u203a #47> passed (rerun once). Rebuilt by <https://build.devtools.lumeris.com/browse/user/anewton|Allen Newton>', u'fallback': u'ClearCare \u203a CareGap \u203a #47 passed (rerun once). Rebuilt by Allen Newton', u'id': 1}], u'text': u'', u'ts': u'1493329694.658318', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'}

	def test_getUser(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/browse/CLEAR-CAR-47|ClearCare \u203a CareGap \u203a #47> passed (rerun once). Rebuilt by <https://build.devtools.lumeris.com/browse/user/anewton|Allen Newton>', u'fallback': u'ClearCare \u203a CareGap \u203a #47 passed (rerun once). Rebuilt by Allen Newton', u'id': 1}], u'text': u'', u'ts': u'1493329694.658318', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})

		self.assertEquals(parser.getUser(), "incoming-webhook")

	def test_isNotValid_noUserName(self):
		parser =  slackBambooMsgParser({u'text': u'message', u'type': u'message', u'user': u'U38TSJNUD', u'ts': u'1493406467.291965'})
		self.assertFalse(parser.isValid())

	def test_isNotValid_noAttachments(self):
		parser =  slackBambooMsgParser({u'username': u'message', u'type': u'message', u'user': u'U38TSJNUD', u'ts': u'1493406467.291965'})
		self.assertFalse(parser.isValid())

	def test_getBambooPlan(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/browse/CLEAR-CAR-47|ClearCare \u203a CareGap \u203a #47> passed (rerun once). Rebuilt by <https://build.devtools.lumeris.com/browse/user/anewton|Allen Newton>', u'fallback': u'ClearCare \u203a CareGap \u203a #47 passed (rerun once). Rebuilt by Allen Newton', u'id': 1}], u'text': u'', u'ts': u'1493329694.658318', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})

		self.assertEquals(parser.getBambooPlanName(), "CareGap")

	def test_getBambooProject(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/browse/CLEAR-CAR-47|ClearCare \u203a CareGap \u203a #47> passed (rerun once). Rebuilt by <https://build.devtools.lumeris.com/browse/user/anewton|Allen Newton>', u'fallback': u'ClearCare \u203a CareGap \u203a #47 passed (rerun once). Rebuilt by Allen Newton', u'id': 1}], u'text': u'', u'ts': u'1493329694.658318', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})

		self.assertEquals(parser.getBambooProjectName(), "ClearCare")

	def test_isFeatureBranch(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/browse/CLEAR-CAR-47|ClearCare \u203a CareGap \u203a #47> passed (rerun once). Rebuilt by <https://build.devtools.lumeris.com/browse/user/anewton|Allen Newton>', u'fallback': u'ClearCare \u203a CareGap \u203a #47 passed (rerun once). Rebuilt by Allen Newton', u'id': 1}], u'text': u'', u'ts': u'1493329694.658318', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		
		self.assertFalse(parser.isFeatureBranch())
		
	def test_isJobPassedTrue(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/browse/CLEAR-CAR-47|ClearCare \u203a CareGap \u203a #47> passed (rerun once). Rebuilt by <https://build.devtools.lumeris.com/browse/user/anewton|Allen Newton>', u'fallback': u'ClearCare \u203a CareGap \u203a #47 passed (rerun once). Rebuilt by Allen Newton', u'id': 1}], u'text': u'', u'ts': u'1493329694.658318', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		
		self.assertTrue(parser.isJobPassed())

	def test_isJobPassedFalse(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/browse/CLEAR-CAR-47|ClearCare \u203a CareGap \u203a #47> passed (rerun once). Rebuilt by <https://build.devtools.lumeris.com/browse/user/anewton|Allen Newton>', u'fallback': u'ClearCare \u203a CareGap \u203a #47 failed (rerun once). Rebuilt by Allen Newton', u'id': 1}], u'text': u'', u'ts': u'1493329694.658318', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		
		self.assertFalse(parser.isJobPassed())

if __name__ == '__main__':
	unittest.main()
