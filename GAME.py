import pygame
from MENU import Menu
from random import randint





class Game_M(Menu):
	def __init__(self, game):
		Menu.__init__(self, game)
		self.state = 'Answer1'
		self.answer1x, self.answer1y = self.mid_w - 150, self.mid_h + 150
		self.answer2x, self.answer2y = self.mid_w + 150, self.mid_h + 150
		self.answer3x, self.answer3y = self.mid_w - 150, self.mid_h + 250
		self.answer4x, self.answer4y = self.mid_w + 150, self.mid_h + 250
		self.cursor_rect.midtop = (self.answer1x + self.offset, self.answer1y)

		self.round = 1
		self.score = 0
		self.good_answer = False

	def display_menu(self):
		self.run_display = True
		self.playing = True
		while self.run_display:
			self.game.check_events()
			self.check_input()
			self.game.display.fill(self.game.CELESTE)

			# Add Image
			self.game.draw_image()
			self.game.write_text(self.game.posible_answer[0], 40, self.answer1x, self.answer1y)
			self.game.write_text(self.game.posible_answer[1], 40, self.answer2x, self.answer2y)
			self.game.write_text(self.game.posible_answer[2], 40, self.answer3x, self.answer3y)
			self.game.write_text(self.game.posible_answer[3], 40, self.answer4x, self.answer4y)
			self.draw_cursor()
			self.blit_screen()

	def move_cursor(self):
		if self.game.DOWN_KEY or self.game.UP_KEY:
			if self.state == 'Answer1':
				self.cursor_rect.midtop = (self.answer3x + self.offset, self.answer3y)
				self.state = 'Answer3'
			elif self.state == 'Answer3':
				self.cursor_rect.midtop = (self.answer1x + self.offset, self.answer1y)
				self.state = 'Answer1'
			elif self.state == 'Answer2':
				self.cursor_rect.midtop = (self.answer4x + self.offset, self.answer4y)
				self.state = 'Answer4'
			elif self.state == 'Answer4':
				self.cursor_rect.midtop = (self.answer2x + self.offset, self.answer2y)
				self.state = 'Answer2'

		elif self.game.LEFT_KEY or self.game.RIGHT_KEY:
			if self.state == 'Answer1':
				self.cursor_rect.midtop = (self.answer2x + self.offset, self.answer2y)
				self.state = 'Answer2'
			elif self.state == 'Answer2':
				self.cursor_rect.midtop = (self.answer1x + self.offset, self.answer1y)
				self.state = 'Answer1'
			elif self.state == 'Answer3':
				self.cursor_rect.midtop = (self.answer4x + self.offset, self.answer4y)
				self.state = 'Answer4'
			elif self.state == 'Answer4':
				self.cursor_rect.midtop = (self.answer3x + self.offset, self.answer3y)
				self.state = 'Answer3'

	def check_input(self):
		self.move_cursor()
		if self.game.START_KEY:
			self.run_display = False

	def next_round(self):
		""""""