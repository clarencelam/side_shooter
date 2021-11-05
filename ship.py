import pygame
from settings import Settings


class Ship:
	""" Ship on left side of screen, moves up and down, shoots right """

	def __init__(self, ss_game):
		""" initialize ship """
		self.screen = ss_game.screen
		self.screen_rect = ss_game.screen.get_rect()

		# Load ship image and get its rect
		sharkimg = pygame.image.load('images/shark.bmp')
		self.image = pygame.transform.scale(sharkimg, (100,100))
		self.rect = self.image.get_rect()

		self.rect.midleft = self.screen_rect.midleft

		# store a decimal float for the Y position of the ship
		self.y = float(self.rect.y)

		self.moving_up = False
		self.moving_down = False

	def update(self):
		""" update the ships location given the current actions"""
		if self.moving_up == True:
			self.y = self.y - 1
			self.rect.y = self.y

		if self.moving_down == True:
			self.y = self.y + 1
			self.rect.y = self.y

	def blitme(self):
		"""draw the ship at its position"""
		self.screen.blit(self.image, self.rect)
