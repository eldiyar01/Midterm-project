import sys 
import pygame as pg 
import random

from bullet import Bullet 
from laser import Laser
from laserdrop import LaserDrop
from spacemin import SpaceMin
from laser import Laser


def check_keydown(event, ai_settings, screen, ship, bullets):
	if event.key == pg.K_RIGHT:
		ship.moving_r = True
	elif event.key == pg.K_LEFT:
		ship.moving_l = True
	elif event.key == pg.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
		

def check_keyup(event, ship, ):
	if event.key == pg.K_RIGHT:
		ship.moving_r = False
	elif event.key == pg.K_LEFT:
		ship.moving_l = False


def check_events(ai_settings, screen, ship, bullets):	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			check_keydown(event, ai_settings, screen, ship, bullets)
		elif event.type == pg.KEYUP:
			check_keyup(event, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
	n_bullet = Bullet(ai_settings, screen, ship)
	bullets.add(n_bullet)	
	ai_settings.bullet_fs.play()


def update_screen(ai_settings, screen, ship, boss, spacemins, bullets, laserdrops, laser):
	screen.fill(ai_settings.bg_color)
	screen.blit(ai_settings.bg_img,(0,0))
	
	ship.blitme()
	boss.blitme()
	

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	for laserdrop in laserdrops.sprites():
		laserdrop.draw_laserdrop()	
		
	if ai_settings.laser_fire:
		laser.draw_laser()
		
	for spacemin in spacemins:
		spacemin.blitme()

	pg.display.flip()

def add_spacemin(ai_settings, screen, spacemins):
	n_spacemin = SpaceMin(ai_settings, screen)
	if len(spacemins) < 4 and ai_settings.sm_add_interval == 0:
		spacemins.add(n_spacemin)
		ai_settings.sm_position = random.randint(200,400)
		ai_settings.sm_add_interval = random.randint(200,600)
	ai_settings.sm_add_interval -= 1

def update_spacemins(ai_settings, spacemins):
	spacemins.update()
	for spacemin in spacemins:
		# print(spacemin.health)
		if spacemin.health == 0:
			spacemins.remove(spacemin)

def spacemin_dammage(ai_settings, spacemins, bullets):
	collisions = pg.sprite.groupcollide(spacemins, bullets, False, True)

	for collision in collisions:
		print(len(spacemins))
		collision.health -= 1

def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

# def update_boss(ai_settings, boss):
# 	pass

def boss_dammage(ai_settings, boss, bullets):
	collisions = pg.sprite.spritecollide(boss, bullets, True)
	for collision in collisions:
		ai_settings.boss_health -= 1

def ship_dammage(ai_settings, ship, laserdrops, laser):
	if pg.sprite.collide_rect(laser, ship) and ai_settings.laser_fire == True:
		ai_settings.ship_health -= 1
		print(ai_settings.ship_health)

	collissions = pg.sprite.spritecollide(ship, laserdrops, True)
	for collission in collissions:
		ai_settings.ship_health -= 1
		print(ai_settings.ship_health)

def laser_rain(ai_settings, screen, laserdrops):
	ld_postion = random.randint(1,1240)
	n_laserdrop = LaserDrop(ai_settings, screen, ld_postion)
	if len(laserdrops) < 40 and ai_settings.ld_interval==0:
		laserdrops.add(n_laserdrop)
		ai_settings.ld_interval= random.randint(1,100)
	ai_settings.ld_interval-=1

def lr_update(laserdrops):
	laserdrops.update()	
	for laserdrop in laserdrops:
		if laserdrop.rect.bottom == 700:
			laserdrops.remove(laserdrop)

def boss_fire(ai_settings, screen, boss):
	if ai_settings.lf_interval < 70:
		ai_settings.laser_fire = True
	if ai_settings.lf_interval == 0:
		ai_settings.lf_interval=random.randint(300,1500)
		ai_settings.laser_fire = False
	ai_settings.lf_interval -= 1

def play_snd(ai_settings):
	# pg.mixer.music.play(loops=1, start=0.0,)
	pass
