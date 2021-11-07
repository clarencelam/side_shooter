class GameStats:

	def __init__(self, ss_game):
		"""initalize game stats"""
		self.settings = ss_game.settings
		self.reset_stats()

	def reset_stats(self):
		"""reset stats for a fresh game"""
		self.ship_lives = self.settings.ship_lives