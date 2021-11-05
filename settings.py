import pygame 

class Settings:
	""" A class to store all settings for Alien Invasion """

	def __init__(self):
		"""initialize the game settings"""
		# Screen Settings
		self.screen_width = 1500
		self.screen_height = 900
		self.bg_color = (100,200,100)

		# Ship settings
		self.ship_speed = 1.5
		
		# Bullet Settings 
		self.bullet_speed = 1.0
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)		
