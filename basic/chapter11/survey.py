#一个要测试的类
class AnonymousSurvey():
	"""收集匿名调查问卷的答案"""

	def __init__(self, question):
		"""存储一个问题，并未存储答案做准备"""
		self.question = question
		self.responses = []

	def showQuestion(self):
		"""显示调查问卷"""
		print(self.question)

	def storeResponse(self, newResponse):
		"""存储单份调查问卷"""
		self.responses.append(newResponse)

	def showResults(self):
		"""显示收集到的所有答卷"""
		print("Survey results:")
		for response in self.responses:
			print(response)
