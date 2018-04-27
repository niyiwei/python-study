import json
import pygal.maps.world
from country_codes import get_country_code

#将数据加载到一个列表中
filename = 'population_data.json'

with open(filename) as f:
	pop_data = json.load(f)

cc_populations = {}
#打印每个国家2010年的人口总数
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		# print(pop_dict)
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population

#根据人口数量将所有的国家分为三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
#查看每组分别包含多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))
wm = pygal.maps.world.World()
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_pops_1)

wm.add('2010', cc_populations)
wm.render_to_file("world_population.svg")