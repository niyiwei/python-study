class Settings():
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		self.title = "外星人入侵"

		#飞船的设置
		self.ship_speed_factor = 1.5
		#飞船的生命
		self.ship_limit = 3


		#子弹设置
		#子弹速度
		self.bullet_speed_factor = 3
		#子弹矩形宽度
		self.bullet_width = 3
		#子弹高度
		self.bullet_height = 15
		#子弹颜色
		self.bullet_color = 60, 60, 60
		#子弹数量
		self.bullets_allowed = 30

		#外星人设置
		#移动速度
		self.alien_speed_factor = 1
		#降落高度
		self.fleet_drop_speed = 50
		#往右为(1)往左为(-1)
		self.fleet_direction = 1
