import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
	""" Bullet object """

	def __init__(self, ss_game):
		"""initialize a bullet"""
		super().__init__() #super() calls the SideShooter class as the ss_game variable here
		self.settings = Settings()
		self.screen = ss_game.screen
		self.screen_rect = ss_game.screen.get_rect()
		self.bullet_color = self.settings.bullet_color

		# Generate the bullet rect
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.center = ss_game.ship.rect.center

		# Store the bullet's x position as decimal value
		self.x = float(self.rect.x)

	def update(self):
		# update the bullet's position on each 
		self.x = self.x + 1
		self.rect.x = self.x

	def draw_bullet(self):
		# draw the bullet to screen
		pygame.draw.rect(self.screen, self.bullet_color, self.rect)
