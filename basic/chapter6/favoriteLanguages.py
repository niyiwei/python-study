favoriteLanguages = {
	'jen':'python'
	,'sarah':'c'
	,'edward':'ruby'
	,'phil':'python'
}

for name, language in favoriteLanguages.items():
	print(name.title() + "'s favorite language is "+ language.title()+".")


#遍历字典中的所有键  keys()方法
for name in favoriteLanguages.keys():
	print(name.title())

#除去重复set()方法
print("\nThe following languages have been mentioned:")
for language in set(favoriteLanguages.values()):
	print(language.title())