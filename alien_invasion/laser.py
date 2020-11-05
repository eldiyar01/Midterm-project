import pygame as pg
from pygame.sprite import Sprite 


class Laser(Sprite):
	
	def __init__(self, ai_settings, screen, boss):
		super(Laser, self).__init__()

		self.screen = screen
		lb_img_url = ['img/lb1.png', 'img/lb2.png', 'img/lb3.png', 
		'img/lb4.png', 'img/lb5.png', 'img/lb6.png', 'img/lb7.png', 
		'img/lb8.png', 'img/lb9.png', 'img/lb10.png', ]

		self.lb_images = []
		for img in lb_img_url:
			self.lb_images.append(pg.image.load(img)) 

		self.lb_interval = 7
		self.index = 0
		self.rect = pg.Rect(600,0,10,600)
		

	def draw_laser(self):	
		if self.lb_interval == 0:
			self.index += 1
			self.lb_interval = 7
		self.lb_interval -= 1

		if self.index >= len(self.lb_images):
			self.index = 0

		self.screen.blit(self.lb_images[self.index], (490,110))