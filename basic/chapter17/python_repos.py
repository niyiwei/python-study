import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

#将API响应存储在一个变量中
response_dict = r.json();
print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names, stars = [], []
plot_dicts = []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	# stars.append(repo_dict['stargazers_count'])
	label = repo_dict['description']
	if label == None:
		print("此项目没有描述", repo_dict['name'])
		label = 'name'
		
	plot_dict = {
		'value': repo_dict['stargazers_count']
		,'label': label
		,'xlink': repo_dict['html_url']
	}
	plot_dicts.append(plot_dict)
	# plot_dict = {'value': repo_dict['stargazers_count'], 'label': repo_dict['description']}
	# plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366', base_style = LCS)
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.label_font_size = 14
# my_config.major_label_font_size = 18
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000

# chart = pygal.Bar(my_config, style = my_style)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_label = names

# print(plot_dicts)
# plot_dicts = [
# 	{'value': 16101, 'label': 'Description of httple.'}
# 	,{'value':15028, 'label': 'Description of django.'}
# 	,{'value':14798, 'label': 'Description of flask.'}
# ]
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
