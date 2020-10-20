import pygame as pg 
from pygame.sprite import Sprite


class Boss(Sprite):

	def __init__(self, ai_settings, screen):
		super(Boss, self).__init__()

		self.screen = screen
		self.ai_settings = ai_settings

		self.boss_img_url = ['img/boss-1.bmp', 'img/boss-2.bmp','img/boss-3.bmp','img/boss-4.bmp',]
		self.boss_images = []

		for self.img in self.boss_img_url:
			self.boss_images.append(pg.image.load(self.img)) 

		self.index = 0
		self.boss_interval = ai_settings.anm_interval

		self.screen_rect = screen.get_rect()
		self.rect = self.boss_images[0].get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.top = self.screen_rect.top

		self.center = float(self.rect.centerx)


	def update(self):
		pass


	def blitme(self):
		
		if self.boss_interval == 0:
			self.index += 1
			self.boss_interval = 20
		self.boss_interval  -= 1

		if self.index >= len(self.boss_images):
			self.index = 0
		
		if self.ai_settings.boss_health>0:
			self.screen.blit(self.boss_images[self.index], self.rect)	
	