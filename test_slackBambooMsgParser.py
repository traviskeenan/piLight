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

        # Deploy Jobs
	def test_isDeployJobValid(self):
		parser =  slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/deploy/viewDeploymentProjectEnvironments.action?id=25559054|CFN-CareGapDeploy> <https://build.devtools.lumeris.com/deploy/viewDeploymentVersion.action?versionId=25755701|1.0.5-17> was successfully deployed to <https://build.devtools.lumeris.com/deploy/viewEnvironment.action?id=25624619|DEV>. <https://build.devtools.lumeris.com/deploy/viewDeploymentResult.action?deploymentResultId=25886830|See details>.', u'fallback': u'CFN-CareGapDeploy 1.0.5-17 was successfully deployed to DEV. See details.', u'id': 1}], u'text': u'', u'ts': u'1497025597.594905', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		self.assertTrue(parser.isValid())

	def test_isDeployJobValidStartingDeploy(self):
		parser =  slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'daa038', u'text': u'<https://build.devtools.lumeris.com/deploy/viewDeploymentProjectEnvironments.action?id=27525128|CaregapDevDeploy> <https://build.devtools.lumeris.com/deploy/viewDeploymentVersion.action?versionId=27754537|release-1> has started deploying to <https://build.devtools.lumeris.com/deploy/viewEnvironment.action?id=27623437|DEV>. <https://build.devtools.lumeris.com/deploy/viewDeploymentResult.action?deploymentResultId=27951179|See details>.', u'fallback': u'CaregapDevDeploy release-1 has started deploying to DEV. See details.', u'id': 1}], u'text': u'', u'ts': u'1499262127.096838', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		self.assertFalse(parser.isValid())

	def test_isDeployJobPassedTrue(self):
		parser =  slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/deploy/viewDeploymentProjectEnvironments.action?id=25559054|CFN-CareGapDeploy> <https://build.devtools.lumeris.com/deploy/viewDeploymentVersion.action?versionId=25755701|1.0.5-17> was successfully deployed to <https://build.devtools.lumeris.com/deploy/viewEnvironment.action?id=25624619|DEV>. <https://build.devtools.lumeris.com/deploy/viewDeploymentResult.action?deploymentResultId=25886830|See details>.', u'fallback': u'CFN-CareGapDeploy 1.0.5-17 was successfully deployed to DEV. See details.', u'id': 1}], u'text': u'', u'ts': u'1497025597.594905', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		self.assertTrue(parser.isJobPassed())

	def test_isDeployJobPassedFalse(self):
		parser =  slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'd00000', u'text': u'<https://build.devtools.lumeris.com/deploy/viewDeploymentProjectEnvironments.action?id=25559054|CFN-CareGapDeploy> <https://build.devtools.lumeris.com/deploy/viewDeploymentVersion.action?versionId=25755697|1.0.0-12> failed deploying to <https://build.devtools.lumeris.com/deploy/viewEnvironment.action?id=25624619|DEV>. <https://build.devtools.lumeris.com/deploy/viewDeploymentResult.action?deploymentResultId=25886824|See details>.', u'fallback': u'CFN-CareGapDeploy 1.0.0-12 failed deploying to DEV. See details.', u'id': 1}], u'text': u'', u'ts': u'1496427761.547608', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		self.assertFalse(parser.isJobPassed())

	def test_getBambooDeployJobPlanName(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'd00000', u'text': u'<https://build.devtools.lumeris.com/deploy/viewDeploymentProjectEnvironments.action?id=25559054|CFN-CareGapDeploy> <https://build.devtools.lumeris.com/deploy/viewDeploymentVersion.action?versionId=25755697|1.0.0-12> failed deploying to <https://build.devtools.lumeris.com/deploy/viewEnvironment.action?id=25624619|DEV>. <https://build.devtools.lumeris.com/deploy/viewDeploymentResult.action?deploymentResultId=25886824|See details>.', u'fallback': u'CFN-CareGapDeploy 1.0.0-12 failed deploying to DEV. See details.', u'id': 1}], u'text': u'', u'ts': u'1496427761.547608', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		self.assertEquals(parser.getBambooPlanName(), "CFN-CareGapDeploy-DEV.")

	def test_getBambooDeployJobProjectName(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'd00000', u'text': u'<https://build.devtools.lumeris.com/deploy/viewDeploymentProjectEnvironments.action?id=25559054|CFN-CareGapDeploy> <https://build.devtools.lumeris.com/deploy/viewDeploymentVersion.action?versionId=25755697|1.0.0-12> failed deploying to <https://build.devtools.lumeris.com/deploy/viewEnvironment.action?id=25624619|DEV>. <https://build.devtools.lumeris.com/deploy/viewDeploymentResult.action?deploymentResultId=25886824|See details>.', u'fallback': u'CFN-CareGapDeploy 1.0.0-12 failed deploying to DEV. See details.', u'id': 1}], u'text': u'', u'ts': u'1496427761.547608', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		self.assertEquals(parser.getBambooProjectName(), "CFN-CareGapDeploy")

	def test_getBambooDeployJobPlanNameFailedJob(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'd00000', u'text': u'<https://build.devtools.lumeris.com/deploy/viewDeploymentProjectEnvironments.action?id=25559054|CFN-CareGapDeploy> <https://build.devtools.lumeris.com/deploy/viewDeploymentVersion.action?versionId=25755697|1.0.0-12> failed deploying to <https://build.devtools.lumeris.com/deploy/viewEnvironment.action?id=25624619|DEV>. <https://build.devtools.lumeris.com/deploy/viewDeploymentResult.action?deploymentResultId=25886824|See details>.', u'fallback': u'CFN-CareGapDeploy 1.0.0-12 failed deploying to DEV. See details.', u'id': 1}], u'text': u'', u'ts': u'1496427761.547608', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		self.assertEquals(parser.getBambooPlanName(), "CFN-CareGapDeploy-DEV.")

	def test_getBambooDeployJobPlanNameSuccessJob(self):
		parser = slackBambooMsgParser({u'username': u'incoming-webhook', u'attachments': [{u'color': u'36a64f', u'text': u'<https://build.devtools.lumeris.com/deploy/viewDeploymentProjectEnvironments.action?id=25559054|CFN-CareGapDeploy> <https://build.devtools.lumeris.com/deploy/viewDeploymentVersion.action?versionId=25755698|1.0.2-14> was successfully deployed to <https://build.devtools.lumeris.com/deploy/viewEnvironment.action?id=25624619|DEV>. <https://build.devtools.lumeris.com/deploy/viewDeploymentResult.action?deploymentResultId=25886826|See details>.', u'fallback': u'CFN-CareGapDeploy 1.0.2-14 was successfully deployed to DEV. See details.', u'id': 1}], u'text': u'', u'ts': u'1496847656.773149', u'subtype': u'bot_message', u'type': u'message', u'bot_id': u'B3JF4Q0SD'})
		self.assertEquals(parser.getBambooPlanName(), "CFN-CareGapDeploy-DEV.")


if __name__ == '__main__':
	unittest.main()
