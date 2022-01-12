import pygame
import random

class Menu():
	def __init__(self, game):
		self.game = game
		self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
		self.run_display = True
		self.cursor_rect = pygame.Rect(0, 0, 20, 20)
		self.offset = - 100

	def draw_cursor(self):
		self.game.write_text('*', 30, self.cursor_rect.x, self.cursor_rect.y)

	def blit_screen(self):
		self.game.window.blit(self.game.display, (0, 0))
		pygame.display.update()
		self.game.reset_keys()

class Main_M(Menu):
	def __init__(self, game):
		Menu.__init__(self, game)
		self.state = "Start"
		self.startx, self.starty = self.mid_w, self.mid_h + 50
		self.creditsx, self.creditsy = self.mid_w, self.mid_h + 100
		self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

	def display_menu(self):
		self.run_display = True
		while self.run_display:
			self.game.check_events()
			self.check_input()
			self.game.display.fill(self.game.CELESTE)
			self.game.write_text('Quiweebs', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 4)
			self.game.write_text("Start Game", 40, self.startx, self.starty)
			self.game.write_text("Credits", 40, self.creditsx, self.creditsy)
			self.draw_cursor()
			self.blit_screen()


	def move_cursor(self):
		if self.game.DOWN_KEY or self.game.UP_KEY:
			if self.state == 'Start':
				self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
				self.state = 'Credits'
			elif self.state == 'Credits':
				self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
				self.state = 'Start'

	def check_input(self):
		self.move_cursor()
		if self.game.START_KEY:
			if self.state == 'Start':
				self.game.get_collection()
				print(self.game.collection)
				self.game.random_question()
				self.game.curr_menu = self.game.game_menu
			elif self.state == 'Credits':
				self.game.curr_menu = self.game.credits_menu
			self.run_display = False

class Credits_M(Menu):
	def __init__(self, game):
		Menu.__init__(self, game)

	def display_menu(self):
		self.run_display = True
		while self.run_display:
			self.game.check_events()
			if self.game.START_KEY or self.game.BACK_KEY:
				self.game.curr_menu = self.game.main_menu
				self.run_display = False
			self.game.display.fill(self.game.CELESTE)
			self.game.write_text('Credits', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 4)
			self.game.write_text('Moi  |  Game', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
			self.game.write_text('Daniil  |  Menu', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 100)
			self.blit_screen()