import sys 
import pygame as pg
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from boss import Boss
from laser import Laser


pg.init()
ai_settings = Settings()
screen = pg.display.set_mode((ai_settings.screen_w, ai_settings.screen_h))

def menu():
	info = 'Buttons: Move to left: "←"; Move to right: "→"; Fire: "SPACE"; Pause: "ESC"'
	g_icon = pg.image.load('img/icon.png')
	pg.display.set_icon(g_icon)
	pg.display.set_caption("Alien Invasion")
	white = ai_settings.white  
	black = ai_settings.black
	font = ai_settings.menu_font
	start_txt = font.render('START' , True , white)  
	quit_txt = font.render('QUIT' , True , white)
	about_txt = ai_settings.font.render(info , True , white)  
	selected = "start"
	while True:  
		for event in pg.event.get():
			if event.type==pg.QUIT:
				sys.exit()
			if event.type==pg.KEYDOWN:
				if event.key==pg.K_UP:
					selected="start"
				elif event.key==pg.K_DOWN:
					selected="quit"
				if event.key==pg.K_RETURN:
					if selected=="start":
						run_game()
					if selected=="quit":
						sys.exit()

		screen.fill(black)  
   
		if selected=="start":
		    start_txt=font.render('START' , True , black)
		    pg.draw.rect(screen,white,[screen.get_rect().centerx-150, screen.get_rect().centery-50,200,50])
		else:
   			start_txt = font.render("START", True,white )
		if selected=="quit":
		    quit_txt=font.render('QUIT' , True ,black )
		    pg.draw.rect(screen,white,[screen.get_rect().centerx-150, screen.get_rect().centery,200,50])
		else:
			quit_txt = font.render("QUIT", True, white )
		screen.blit(start_txt , (screen.get_rect().centerx-100, screen.get_rect().centery-50))  
		screen.blit(quit_txt , (screen.get_rect().centerx-100, screen.get_rect().centery))
		screen.blit(about_txt , (screen.get_rect().centerx-350, screen.get_rect().centery+100))  
  
		pg.display.update()  
	
def run_game():	
	gf.play_snd(ai_settings)
	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	boss = Boss(ai_settings, screen) 
	spacemins = Group()
	sm_bullets = Group()
	laser = Laser(ai_settings, screen, boss)
	laserdrops = Group() 
	
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		gf.update_bullets(bullets)
		gf.boss_dammage(ai_settings, boss, bullets)
		gf.boss_fire(ai_settings, screen, boss)
		if ai_settings.lr_timer <= 2000:
			gf.laser_rain(ai_settings, screen, laserdrops)
			if ai_settings.lr_timer == 0:
				ai_settings.lr_timer = 3000
		ai_settings.lr_timer -= 1
		gf.lr_update(laserdrops)
		gf.add_spacemin(ai_settings, screen, spacemins)
		gf.update_spacemins(ai_settings, spacemins)
		gf.spacemin_dammage(ai_settings, spacemins, bullets)
		gf.spacemin_fire(ai_settings, screen, sm_bullets, spacemins)
		gf.smb_update(sm_bullets)
		gf.ship_dammage(ai_settings, ship, laserdrops, laser, sm_bullets)
		gf.update_screen(ai_settings, screen, ship, boss, spacemins, bullets, laserdrops, laser, sm_bullets)
		if ai_settings.g_pause:
			gf.game_stop(ai_settings, screen, ship, bullets, spacemins, laserdrops, sm_bullets)
		
menu()
