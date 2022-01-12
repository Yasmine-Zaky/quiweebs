import pygame
import json
import os
from MENU import *
from GAME import *

class Main():
	def __init__(self):
		pygame.init()
		self.running, self.playing = True, False
		self.UP_KEY = False
		self.DOWN_KEY = False
		self.LEFT_KEY = False
		self.RIGHT_KEY = False
		self.START_KEY = False
		self.BACK_KEY = False
		self.DISPLAY_W, self.DISPLAY_H = 1000, 700
		self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
		self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
		self.font_name = 'data\\BELL.TTF'
	   
		self.BLACK, self.WHITE, self.CELESTE = (0, 0, 0), (255, 255, 255), (202, 228, 241)
		self.main_menu = Main_M(self)
		self.credits_menu = Credits_M(self)
		self.game_menu = Game_M(self)
		self.curr_menu = self.main_menu

		self.path = 'data\\collections'
		self.collection = None
		self.question = []
		self.answer = []
		self.image = None
		self.proposition1 = []
		self.proposition2 = []
		self.proposition3 = []
		self.posible_answer = []



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
				if event.key == pygame.K_LEFT:
					self.LEFT_KEY = True
				if event.key == pygame.K_RIGHT:
					self.RIGHT_KEY = True

	def reset_keys(self):
		self.UP_KEY = False
		self.DOWN_KEY = False
		self.LEFT_KEY = False
		self.RIGHT_KEY = False
		self.START_KEY = False
		self.BACK_KEY = False

	def write_text(self, text, size, x, y ):
		"""  Pour afficher un texte
		"""

		font = pygame.font.Font(self.font_name,size)
		text_surface = font.render(text, True, self.BLACK)
		text_rect = text_surface.get_rect()
		text_rect.center = (x,y)
		self.display.blit(text_surface,text_rect)

	def get_collection(self):
		"""  Récupèrer une collection aléatoire parmi celle proposé dans le fichier "data\\collections"
		"""

		self.collection = os.listdir(self.path)
		random_collections = random.randint(0, len(self.collection)-1)
		self.collection = str(self.collection[random_collections])
		data = self.get_data()
		self.question = data["Proposition"]

	def random_question(self):
		"""  Choisir une question aléatoire parti celle proposer dans le document json
		"""
		temp_listnumber = [1, 2, 3, 4]

		data = self.get_data()
		random_personnage = str(random.randint(0, len(data)-2))
		random_personnage = str("Personnage_" + random_personnage)
		self.answer = str(data[random_personnage]["Answer"])
		self.image =  str(data[random_personnage]["Image"])
		print(self.image)
		self.image = pygame.image.load(self.image)

		temp_question = self.question.copy()

		self.proposition1 = temp_question[random.randint(0, len(temp_question) - 1)]

		self.proposition2 = temp_question[random.randint(0, len(temp_question) - 1)]

		self.proposition3 = temp_question[random.randint(0, len(temp_question) - 1)]

		self.posible_answer = [self.answer, self.proposition1, self.proposition2, self.proposition3]




	def get_data(self):
		""""""
		with open(self.path+"\\"+self.collection+"\\"+self.collection+".json","r") as f:
			data = json.load(f)
		f.close()
		return data

	def draw_image(self):

		self.display.blit(self.image, (50, 50))





 