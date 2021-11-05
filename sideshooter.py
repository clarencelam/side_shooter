import sys, pygame
from pygame.sprite import Sprite
from settings import Settings
from bullet import Bullet
from ship import Ship
from submarine import Submarine
from random import randint


class SideShooter:
	""" Game that places ship on left side of screen, moves up and down, fires bullets to the right"""

	def __init__(self):
		"""initialize game, create resources"""
		pygame.init()

		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		self.screen_rect = self.screen.get_rect()

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.submarines = pygame.sprite.Group()

		self._create_fleet()

		pygame.display.set_caption("Side Shooter")

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			if event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _update_bullets(self):
		""" update positions of bullets and get rid of old bullets """
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.x > self.settings.screen_width:
				self.bullets.remove(bullet)

		#check for bullet /submarine collissions
		collisions = pygame.sprite.groupcollide(self.bullets, self.submarines, False, True)

	def _check_sub_edges(self):
		""" for submarines, check if they hit the left, if so, remove"""
		for submarine in self.submarines:
			the_subs = self.submarines
			if submarine.check_edges() == True:
				the_subs.remove(submarine)
				self.submarines = the_subs

	def _update_submarines(self):
		""" update submarine objects"""
		self._check_sub_edges()
		self.submarines.update()

		if not self.submarines:
			self._create_fleet()

	def _update_screen(self):
		""" update images on screen """
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.submarines.draw(self.screen)

		# Make most recent screen visible
		pygame.display.flip()


	def run_game(self):
		""" start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_submarines()
			self._update_bullets()
			self._update_screen()


	def _check_keydown_events(self, event):
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _check_keyup_events(self,event):
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _create_fleet(self):
		submarine = Submarine(self)
		submarine_height = submarine.rect.height
		available_space_y = self.screen_rect.height - (2 * submarine_height)
		number_of_subs = available_space_y // (2 * submarine_height) # // symbol to generate whole number

		for sub_number in range(number_of_subs):
			y_rand_adjust = randint(-1 * submarine_height, submarine_height)

			submarine = Submarine(self)
			submarine.y = submarine_height + (2 * sub_number * submarine_height) + y_rand_adjust
			submarine.rect.y = submarine.y
			self.submarines.add(submarine)


if __name__ == '__main__':
	# make an instance of the game and run it
	ss = SideShooter()
	ss.run_game()