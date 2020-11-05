import pygame as pg
from pygame.sprite import Sprite


class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.ship_img_url = ['img/spaceship_1.png', 'img/spaceship_2.png', 'img/spaceship_3.png', 'img/spaceship_4.png']
		self.ship_images = []

		for self.img in self.ship_img_url:
			self.ship_images.append(pg.image.load(self.img))

		self.rect = self.ship_images[0].get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		self.moving_r = False
		self.moving_l = False

		self.ship_interval = ai_settings.anm_interval
		self.index = 0
		self.ship_img = self.ship_images[self.index]
		

	def update(self):
		if self.moving_r and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed
		if self.moving_l and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed
		self.rect.centerx = self.center

	def blitme(self):
		if self.ship_interval == 0:
			self.index += 1
			self.ship_interval = 20
		self.ship_interval -= 1

		if self.index >= len(self.ship_images):
			self.index = 0

		self.screen.blit(self.ship_images[self.index], self.rect)

	def blit_health(self):
		sh_txt = self.ai_settings.font.render('Health: '+str(self.ai_settings.ship_health), True, (255,255,255))
		self.screen.blit(sh_txt,(0,0))