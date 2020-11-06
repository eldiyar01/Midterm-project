import pygame as pg 
from pygame.sprite import Sprite


class SmBullet(Sprite):
	def __init__(self, ai_settings, screen, spacemin):
		super(SmBullet, self).__init__()


		self.screen = screen
		self.sm_bullet = pg.image.load('img/sm_bullet.png')
		self.rect = self.sm_bullet.get_rect()
		self.rect.centerx = spacemin.rect.centerx
		self.rect.top = spacemin.rect.top
		self.y = float(self.rect.y)
		self.speed = ai_settings.smb_speed
		self.interval = 150
	def update(self):
		self.y = self.rect.y
		self.rect.y += self.speed

	def draw_smb(self):
		self.screen.blit(self.sm_bullet, self.rect)
