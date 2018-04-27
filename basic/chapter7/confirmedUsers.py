#7.3 使用while循环来处理列表和字典

#首先，创建一个待验证用户的列表和一个用于存储已验证用户的空列表
unconfirmedUsers = ['alice', 'brian', 'candace']
confirmedUsers = []

#验证每个用户，知道没有未验证用户为止
#将每个经过验证的列表都转移到已验证用户列表中
while unconfirmedUsers:
	currentUser = unconfirmedUsers.pop()

	print("Verifying user: "+currentUser.title())
	confirmedUsers.append(currentUser)

#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed in confirmedUsers:
	print(confirmed.title())
