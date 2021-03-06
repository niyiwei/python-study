import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moveing_right = True
	elif event.key == pygame.K_LEFT:
		ship.moveing_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moveing_right = False
	elif event.key == pygame.K_LEFT:
		ship.moveing_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
	#m每次循环都重绘屏幕， fill方法，用背景色填充屏幕，只接受一个实参：一种颜色
	screen.fill(ai_settings.bg_color)

	#在飞创和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	#对编组使用draw()方法是，pygame自动绘制编组的每个元素，绘制位置由元素的属性rect决定
	aliens.draw(screen)

	#让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings, screen, ship, bullets, aliens):
	"""更新子弹的位置，并删除已消失的子弹"""
	#更新子弹的位置
	bullets.update()

	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens)

def check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens):
	#检查是否有子弹击中了外星人
	#如果是这样，就删除相应的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) <= 0:
		#外星人被打完了,增加外星人移动速度
		bullets.empty()
		ai_settings.alien_speed_factor += 1
		# ai_settings.fleet_direction += 1
		create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
	"""开火"""
	#增加验证未消失的子弹数量
	if len(bullets) < ai_settings.bullets_allowed:
		#创建一颗子弹，并将其加入到编组bullets中
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
	"""计算每行可容纳多少外星人"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""创建一个外星人并将其放在当前行"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	"""创建外星人群"""
	#创建一个外星人，并计算一行可容纳多少个外星人
	#外星人间距为外星人宽度
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_numbet_rows(ai_settings, ship.rect.height, alien.rect.height)
	#创建第一行外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number, row_number)

def get_numbet_rows(ai_settings, ship_height, alien_height):
	"""计算屏幕可容纳多少行外星人"""
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def update_aliens(ai_settings, stats, screen,  ship, aliens, bullets):
	"""更新外星人群中所有外星人的位置"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	#检测外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		print("Ship hit!!!")
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
	"""有外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
def change_fleet_direction(ai_settings, aliens):
	"""将整群外星人下移，并改变它们的方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen,  ship, aliens, bullets):
	"""响应被外星人撞到的飞船"""
	# 将ships_left减1
	stats.ships_left -= 1

	# 清空外星人列表和子弹列表
	aliens.empty();
	bullets.empty();

	#创建一群新的外星人，并将飞船放到屏幕底部中央
	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()

	#暂停
	sleep(0.5)