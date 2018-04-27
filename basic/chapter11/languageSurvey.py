from survey import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象

question = "What language did you first learn to speak?"
mySurvey = AnonymousSurvey(question)

#显示问题并存储答案
mySurvey.showQuestion();
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	mySurvey.storeResponse(response)

#显示调查结果

print("\nThank you to everyone who participated in the survey!")
mySurvey.showResults()