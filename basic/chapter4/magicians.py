#遍历整个列表
magicians = ['alice', 'david', 'carolina']

#使用for循环来打印魔术师名单中的所有名字
for magician in magicians:
	print(magician)


#在循环中执行更多的操作
for magician in magicians:
	#在for循环里面缩进了的 都是循环里面要执行的代码
	print(magician.title() +", that was a great trick!")
	print("I can't wait to see your next trick, "+ magician.title() +".\n")

#不适用缩进代表不在循环里面执行
print("Thank you, everyone, That was a great magic show!")