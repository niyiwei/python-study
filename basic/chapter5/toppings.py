requestedToppings = ['mushrooms', 'green peppers', 'extra cheese']

for requestedTopping in requestedToppings:
	if requestedTopping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding "+requestedTopping+".")
	# print(requestedTopping)

print("\nFinished making your pizza!")


print("\nCheck list is empty")
# 检查列表不是空的
requestedToppings = []

if requestedToppings:
	for requestedTopping in requestedToppings:
		print("Adding "+ requestedTopping +".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")


#使用多个列表
print("\n")
availableToppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requestedToppings = ['mushrooms', 'french fries', 'extra cheese']

for requestedTopping in requestedToppings:
	if requestedTopping in availableToppings:
		print("Adding "+ requestedTopping+".")
	else:
		print("Sorry, we don't have "+requestedTopping+".")

print("\nFinished making your pizza!")