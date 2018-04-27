from nameFunction import getFormattedName

print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q' or first == 'Q':
		break

	last = input("\nPlease give me a last me: ")
	if last == "q" or first == 'Q':
		break

	formattedName = getFormattedName(first, last)
	print("\tNeatly formatted name: " + formattedName + ".")