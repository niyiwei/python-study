import json
from pygal_maps_world.i18n import COUNTRIES

# for country_code in sorted(COUNTRIES.keys()):
	# print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code

	#没有找到就返回None
	return None

#将数据加载到一个列表中
filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)

#打印每个国家2010年的人口数量
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			print(code +": " + str(population))
		else:
			print('Error - '+ country_name)