#单词首字母大写方法
name = "ada lovelace"
print(name.title())


name = "Ada Lovelace"
#全部转成大写
print(name.upper())
#全部转成小写

print(name.lower());

#合并（拼接）字符串

firstName = "ada"
lastName = "lovelace"
fullName = firstName +" "+ lastName
print(fullName)
print(fullName.title())
print("Hello word, "+ fullName.title());

#使用制表符或换行符来添加空白
print("Python")
print("\tPython")

print("\n\n")
print("Languages:\n\tPython\n\tJava\n\tJavaScript")

#删除空白
favoriteLanguage = "pytho ";
#rstrip()函数删除句尾空格
print(favoriteLanguage.rstrip()+"n");
#lstrip()函数删除开头空白
favoriteLanguage = " ytho ";
print("p"+favoriteLanguage+"n");
print("p"+favoriteLanguage.lstrip().strip()+"n")