import pygame as pg
import random

class Settings():
	def __init__(self):

		self.screen_w = 1250
		self.screen_h = 650
		self.bg_color = (0,0,0)
		self.bg_img = pg.image.load('img/cosmos.bmp')
		self.anm_interval = 20

		self.soundtrack = pg.mixer.music.load('music/vulta-cyborgist.mp3')

		self.ship_speed = 4
		self.ship_health = 10

		self.bullet_speed = 4
		self.bullet = pg.image.load('img/laser.png')
		self.bullet_fs = pg.mixer.Sound('snd/laser.wav')

		self.boss_health = 10
		self.lf_interval = random.randint(300,1000)
		self.laser_fire = False
		self.laserdrop_speed = 1
		self.ld_interval =random.randint(1,100) 

		self.sm_position = random.randint(150,450)
		self.spacemin_speed = 3
		self.spacemin_health = 3
		self.sm_add_interval = 0

		# self.sm_bullet = pg.image.load('img/sm_bullet.png')


		
