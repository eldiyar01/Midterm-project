import pygame as pg
import random


class Settings():
	def __init__(self):
		self.g_pause = False

		self.screen_w = 1250
		self.screen_h = 650
		self.black = (0,0,0)
		self.white = (255,255,255)
		self.bg_img = pg.image.load('img/cosmos.bmp')
		self.anm_interval = 20
		self.font = pg.font.Font('freesansbold.ttf', 20)
		self.menu_font = pg.font.Font("Retro.ttf",55)  

		self.soundtrack = pg.mixer.music.load('music/Swarm-2fast.mp3')

		self.ship_speed = 4
		self.ship_health = 5
		self.ship_fs = pg.mixer.Sound('snd/laser.wav')
		self.ship_d = pg.mixer.Sound('snd/dammage.wav')

		self.bullet_speed = 4
		
		self.boss_health = 200
		self.boss_fs = pg.mixer.Sound('snd/laser_beam.wav')
		self.lf_interval = 1000
		self.laser_fire = False
		self.lr_timer = 6500
		self.laserdrop_speed = 1
		self.ld_interval =random.randint(1,100) 
		self.ld_sound = pg.mixer.Sound('snd/ld_electro.wav')
		self.ld_sound.set_volume(0.2)

		self.sm_position = random.randint(150,450)
		self.spacemin_speed = 3
		self.spacemin_health = 3
		self.sm_add_interval = 300
		self.sm_count = 10
		self.sm_lf = pg.mixer.Sound('snd/sm_laser.wav')

		self.smb_speed = 2
		self.smb_fire = False
		self.smbf_interval = random.randint(0,100)
		# self.sm_bullet = pg.image.load('img/sm_bullet.png')


		
