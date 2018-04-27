alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0,alien_1,alien_2]

# for alien in aliens:
# 	print(alien)


aliens = []

#创建30个绿色的外形人
for alienNumber in range(30):
	aliens.append({'color':'green', 'points':5, 'speed': 'slow'})

#显示前面五个外星人
for alien in aliens[0:5]:
	print(alien)
print("...")

#显示创建了多少外星人
print("Total number of aliens: "+str(len(aliens)))


#修改前面三个外星人颜色改为黄色，速度改为中等，且值10个点
print("\nUpdate alien color,spend and point")
for alien in aliens[:3]:
	alien['color'] = 'yellow'
	alien['speed'] = 'medium'
	alien['points'] = 10

for alien in aliens[0:5]:
	print(alien)
print("...")


print("\nUpdate yellow alien to red alien")
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'red'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15