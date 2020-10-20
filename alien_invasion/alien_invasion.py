import pygame as pg
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from boss import Boss
from laser import Laser

def run_game():
	pg.init()
	ai_settings = Settings()
	screen = pg.display.set_mode((ai_settings.screen_w, ai_settings.screen_h))
	lr_timer = 2100
	g_icon = pg.image.load('img/icon.png')
	pg.display.set_icon(g_icon)
	pg.display.set_caption("Alien Invasion")

	gf.play_snd(ai_settings)
	ship = Ship(ai_settings, screen)
	bullets = Group()
	boss = Boss(ai_settings, screen) 
	spacemins = Group()
	laser = Laser(ai_settings, screen, boss)
	laserdrops = Group() 

	while True:
		# print(len(laserdrops))
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.boss_dammage(ai_settings, boss, bullets)
		gf.boss_fire(ai_settings, screen, boss)
		if lr_timer <= 2000:
			gf.laser_rain(ai_settings, screen, laserdrops)
			if lr_timer == 0:
				lr_timer = 2600
		lr_timer -= 1
		gf.lr_update(laserdrops)
		gf.add_spacemin(ai_settings, screen, spacemins)
		gf.update_spacemins(ai_settings, spacemins)
		gf.spacemin_dammage(ai_settings, spacemins, bullets)
		gf.ship_dammage(ai_settings, ship, laserdrops, laser)
		# gf.update_boss(ai_settings, boss)
		gf.update_screen(ai_settings, screen, ship, boss, spacemins, bullets, laserdrops, laser)
run_game()
