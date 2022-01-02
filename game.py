import pygame
from menu import *


class Game():
	def __init__(self):
		pygame.init()
		self.running, self.playing = False, False
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 700
		self.display = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		self.font_name = "BELL.TTF"

		self.BLUE, self.white = (142,229,238), (255,255,255)
		self.main_menu = Main_M(self)
		self.options = Options_M(self)
		self.credits = Credits_M(self)
		self.currently_in_menu = self.main_menu

		def game_loop(self):

			while self.playing:
				self.check_events()

				if self.START_KEY:
					self.playing = False

				self.display.fill(self.BLACK)
				self.write_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
				self.window.blit(self.display, (0,0))
				pygame.display.update()
				self.reset_keys()

		def check_events(self):

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					self.running, self.playing = False, False
					self.curr_menu.run_display = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.START_KEY = True
					if event.key == pygame.K_BACKSPACE:
						self.BACK_KEY = True
					if event.key == pygame.K_DOWN:
						self.DOWN_KEY = True
					if event.key == pygame.K_UP:
						self.UP_KEY = True

		def reset_keys(self):
			self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False