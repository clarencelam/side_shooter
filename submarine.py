import pygame
from pygame.sprite import Sprite
from settings import Settings

class Submarine(Sprite):
	""" Class to represent enemy submarines """

	def __init__(self, ss_game):
		super().__init__()
		self.screen = ss_game.screen
		self.screen_rect = ss_game.screen.get_rect()

		self.movement_speed = 1

		sub_img = pygame.image.load('images/submarine.bmp')
		self.image = pygame.transform.scale(sub_img, (75,75))
		self.rect = self.image.get_rect()

		# Start each submarine at top right of screen
		self.rect.x = self.screen_rect.width - self.rect.width
		self.rect.y = self.rect.height

		# Store the submarine's position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	def update(self):
		""" move the submarines to the left """
		self.x = self.x - self.movement_speed
		self.rect.x = self.x