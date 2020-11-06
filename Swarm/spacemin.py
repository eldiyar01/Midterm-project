import pygame as pg
from pygame.sprite import Sprite 


class SpaceMin(Sprite):
	def __init__(self, ai_settings, screen):
		super(SpaceMin, self).__init__()

		self.ai_settings = ai_settings

		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.health = ai_settings.spacemin_health
		self.speed = ai_settings.spacemin_speed
		sm_img_url = ['img/spacemin1.png', 'img/spacemin2.png', 'img/spacemin3.png', 'img/spacemin4.png', 'img/spacemin5.png']
		self.spacemin_img = []
		self.index = 0
		self.sm_interval = ai_settings.anm_interval
		for img in sm_img_url:
			self.spacemin_img.append(pg.image.load(img))

		self.rect = self.spacemin_img[0].get_rect()
		self.x = ai_settings.screen_w +50
		self.rect.y = ai_settings.sm_position
		self.move_left = True
		self.move_right = False

	def update(self):
		if self.rect.left > self.screen_rect.left and self.move_left:
			self.x -= self.speed
			if self.rect.left == self.screen_rect.left+1:
				self.move_left = False
				self.move_right = True

		if self.move_right:
			self.x += self.speed
			if self.rect.right == self.screen_rect.right:
				self.move_left = True
				self.move_right = False
		self.rect.x = self.x

	def blitme(self):
		if self.sm_interval == 0:
			self.index += 1
			self.sm_interval = 20
		self.sm_interval -= 1

		if self.index >= len(self.spacemin_img):
			self.index = 0

		self.screen.blit(self.spacemin_img[self.index], self.rect)
