import sys
import pygame as pg
import random

from bullet import Bullet
from laser import Laser
from laserdrop import LaserDrop
from spacemin import SpaceMin
from laser import Laser
from sm_bullet import SmBullet


def check_keydown(event, ai_settings, screen, ship, bullets):
	if event.key == pg.K_RIGHT:
		ship.moving_r = True
	elif event.key == pg.K_LEFT:
		ship.moving_l = True
	elif event.key == pg.K_SPACE:
		if len(bullets) < 5:
			fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pg.K_ESCAPE:
		ai_settings.g_pause = True

def check_keyup(event, ship):
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
	ai_settings.ship_fs.play()

def update_screen(ai_settings, screen, ship, boss, spacemins, bullets, laserdrops, laser, sm_bullets):
	screen.fill(ai_settings.black)
	screen.blit(ai_settings.bg_img,(0,0))
	
	ship.blitme()
	ship.update()
	ship.blit_health()
	boss.blitme()

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	for laserdrop in laserdrops.sprites():
		laserdrop.draw_laserdrop()

	if ai_settings.lf_interval<=140:
		boss.draw_aim()

	if ai_settings.laser_fire:
		laser.draw_laser()
		
	for spacemin in spacemins:
		spacemin.blitme()

	for sm_bullet in sm_bullets.sprites():
		sm_bullet.draw_smb()

	pg.display.flip()

def add_spacemin(ai_settings, screen, spacemins):
	n_spacemin = SpaceMin(ai_settings, screen)
	if len(spacemins) < ai_settings.sm_count and ai_settings.sm_add_interval < 0:
		spacemins.add(n_spacemin)
		ai_settings.sm_position = random.randint(200,400)
		ai_settings.sm_add_interval = random.randint(400,1000)

	ai_settings.sm_add_interval -= 1
	
def update_spacemins(ai_settings, spacemins):
	spacemins.update()
	for spacemin in spacemins:
		if spacemin.health == 0:
			spacemins.remove(spacemin)

def spacemin_dammage(ai_settings, spacemins, bullets):
	collisions = pg.sprite.groupcollide(spacemins, bullets, False, True)

	for collision in collisions:
		collision.health -= 1

def spacemin_fire(ai_settings, screen, sm_bullets, spacemins):
	if len(spacemins) != 0:
		index=random.randint(0,len(spacemins)-1)
		f_spacemin = spacemins.sprites()[index]
		new_smb = SmBullet(ai_settings, screen, f_spacemin)
		if ai_settings.smb_fire == True:
			sm_bullets.add(new_smb)
			ai_settings.sm_lf.play()	
			ai_settings.smb_fire = False

		if ai_settings.smbf_interval == 0:
			ai_settings.smb_fire = True
			ai_settings.smbf_interval = random.randint(100,200)
			# index=random.randint(0,len(spacemins))
		ai_settings.smbf_interval -= 1
		

def smb_update(sm_bullets):
	sm_bullets.update()
	for sm_bullet in sm_bullets:
		if sm_bullet.rect.bottom == 700:
			sm_bullets.remove(sm_bullet)

def update_bullets(bullets):
	bullets.update()
	for bullet in bullets:
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def boss_dammage(ai_settings, boss, bullets):
	collisions = pg.sprite.spritecollide(boss, bullets, True)
	for collision in collisions:
		ai_settings.boss_health -= 1

def ship_dammage(ai_settings, ship, laserdrops, laser, sm_bullets):
	if pg.sprite.collide_rect(laser, ship) and ai_settings.laser_fire:
		ai_settings.ship_health -= 1
		ai_settings.ship_d.play()
		
	ld_collissions = pg.sprite.spritecollide(ship, laserdrops, True)
	for collission in ld_collissions:
		ai_settings.ship_health -= 1
		ai_settings.ship_d.play()
	
	sm_collissions = pg.sprite.spritecollide(ship, sm_bullets, True)
	for collission in sm_collissions:
		ai_settings.ship_health -= 1
		ai_settings.ship_d.play()
	if ai_settings.ship_health <= 0:
		ai_settings.g_pause = True

def laser_rain(ai_settings, screen, laserdrops):
	ld_postion = random.randint(1,1240)
	n_laserdrop = LaserDrop(ai_settings, screen, ld_postion)
	if len(laserdrops) < 40 and ai_settings.ld_interval==0:
		laserdrops.add(n_laserdrop)
		ai_settings.ld_sound.play()
		ai_settings.ld_interval= random.randint(1,50)
	ai_settings.ld_interval-=1

def lr_update(laserdrops):
	laserdrops.update()	
	for laserdrop in laserdrops:
		if laserdrop.rect.bottom == 700:
			laserdrops.remove(laserdrop)

def boss_fire(ai_settings, screen, boss):
	if ai_settings.lf_interval == 140:
		ai_settings.boss_fs.play()
	if ai_settings.lf_interval < 70:
		ai_settings.laser_fire = True
	if ai_settings.lf_interval == 0:
		ai_settings.lf_interval=random.randint(500,2000)
		ai_settings.laser_fire = False
	ai_settings.lf_interval -= 1

def play_snd(ai_settings):
	pg.mixer.music.play(loops=-1, start=0.0)
	
def game_stop(ai_settings, screen, ship, bullets, spacemins, laserdrops, sm_bullets):
	text = 'Press "C" to continue, "R" to restart, "Q" to quit'
	if ai_settings.boss_health <= 0:
		text = 'You win, GJ, press "R" to restart, "Q" to quit'
	elif ai_settings.ship_health <= 0:
		text = 'You loose, press "R" to restart,"Q" to quit and cry'
	pause_txt = ai_settings.font.render(text, True , (ai_settings.white))
	pg.draw.rect(screen,ai_settings.black,[screen.get_rect().centerx-250, screen.get_rect().centery,600,50])
	screen.blit(pause_txt,(screen.get_rect().centerx-200, screen.get_rect().centery+15))
	pg.mixer.music.pause()
	pg.display.update()
	while ai_settings.g_pause:
		for  event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_q:
					sys.exit()
				if event.key == pg.K_c:
					pg.mixer.music.unpause()
					ship.moving_r = False
					ship.moving_l = False
					ai_settings.g_pause = False
				if event.key == pg.K_r:
					pg.mixer.music.play(loops=-1, start=0.0)
					ship.center = float(ship.screen_rect.centerx)	
					ship.moving_r = False
					ship.moving_l = False
					bullets.empty()
					spacemins.empty()
					laserdrops.empty()
					sm_bullets.empty()
					ai_settings.boss_health = 60
					ai_settings.ship_health = 10
					ai_settings.lr_timer = 6500
					ai_settings.sm_add_interval = 300
					ai_settings.laser_fire = False
					ai_settings.lf_interval = 1000
					ai_settings.g_pause = False

		pg.time.delay(1)
		
