#外星人飞创
import pygame

class Ship():

	def __init__(self,  ai_settings, screen):
		"""初始化飞船并设置其初始化位置"""
		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞船图像并获取其外接矩形
		#加载图像，返回一个 surface对象
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#使用浮点类型记录移动位置
		self.center = float(self.rect.centerx);

		#移动标记
		self.moveing_right = False
		self.moveing_left = False

	def blitme(self):
		"""在指定位置绘制飞创"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""根据移动标志调整飞船的位置"""
		#限制移动位置，禁止飞船移动到屏幕外面去
		if self.moveing_right and self.rect.right < self.screen_rect.right:
			# print("右移前 当前位置:"+str(self.rect.center)+",移动速度:"+str(self.ai_settings.ship_speed_factor))
			self.center  += self.ai_settings.ship_speed_factor
			# print("右移后 当前位置:"+str(self.rect.center)+",移动速度:"+str(self.ai_settings.ship_speed_factor))
		if self.moveing_left and self.rect.left > 0:
			# print("左移前 当前位置:"+str(self.rect.center)+",移动速度:"+str(self.ai_settings.ship_speed_factor))
			self.center = self.rect.centerx-self.ai_settings.ship_speed_factor
			# print("左移后 当前位置:"+str(self.rect.center)+",移动速度:"+str(self.ai_settings.ship_speed_factor))
		#根据self.center更新rect对象
		self.rect.centerx = self.center