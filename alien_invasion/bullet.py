import pygame as pg
from pygame.sprite import Sprite 

class Bullet(Sprite):
	
	def __init__(self, ai_settings, screen, ship):
		super(Bullet, self).__init__()

		self.screen = screen

		self.rect = ai_settings.bullet.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)

		self.bullet = ai_settings.bullet
		self.speed = ai_settings.bullet_speed

		self.fire_b = False

	def update(self):
		self.y -= self.speed
		self.rect.y = self.y


	def draw_bullet(self):	
		self.screen.blit(self.bullet, self.rect)
		