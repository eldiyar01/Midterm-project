import pygame as pg 
from pygame.sprite import Sprite 


class LaserDrop(Sprite):

	def __init__(self, ai_settings, screen, ld_position):
		super(LaserDrop, self).__init__()
		self.ld_load_int = ai_settings.anm_interval
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.speed = ai_settings.laserdrop_speed
		ld_img_url = ['img/ld1.png','img/ld2.png', 'img/ld3.png', 'img/ld4.png', 'img/ld5.png', 'img/ld4.png', 
		'img/ld3.png', 'img/ld2.png', 'img/ld1.png']
		self.ld_images = []
		for img in ld_img_url:
			self.ld_images.append(pg.image.load(img))

		self.index=0
		self.rect = self.ld_images[0].get_rect()
		self.rect.top = self.screen_rect.top
		self.rect.x = float(ld_position)
		self.y = float(self.rect.y)
		
	def update(self):
		self.y += self.speed
		self.rect.y = self.y

	def draw_laserdrop(self):

		if self.ld_load_int == 0:
			self.index += 1
			self.ld_load_int = 20
		self.ld_load_int  -= 1

		if self.index >= len(self.ld_images):
			self.index = 0
		self.screen.blit(self.ld_images[self.index], self.rect)	