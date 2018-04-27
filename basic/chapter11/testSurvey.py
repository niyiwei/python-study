import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnonymousSurvey类的测试类"""

	def setUp(self):
		""" 创建一个调查对象和一组答案，共使用的测试方法调用"""
		question = "What language did you first learn to speak?"
		self.mySurvey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']

	def testStoreSingleResponse(self):
		"""测试单个答案会被妥善地存储"""
		# question = "What language did you first learn to speak?"
		# mySurvey = AnonymousSurvey(question)
		self.mySurvey.storeResponse(self.responses[0])
		self.assertIn(self.responses[0], self.mySurvey.responses)

	def testStoreThreeResponse(self):
		"""测试三个答案会被妥善地存储"""
		for response in self.responses:
			self.mySurvey.storeResponse(response)
		for response in self.responses:
			self.assertIn(response, self.mySurvey.responses)

unittest.main()