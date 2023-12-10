import pygame
from const import *


class Button(pygame.sprite.Sprite):
	def __init__(self, x_pos, y_pos, button_text, group, image_path, is_text_button):
		super().__init__(group)
		self.image = pygame.image.load(image_path).convert_alpha()
		self.image = pygame.transform.scale(self.image, (210, 50))
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.is_text_button = is_text_button
		self.button_text = button_text
		if self.is_text_button:
			# Text
			self.font = pygame.font.SysFont(GAME_FONT, 48)
			self.textSurf = self.font.render(button_text, 1, WHITE)
			W = self.textSurf.get_width()
			H = self.textSurf.get_height()
			self.image.blit(self.textSurf, [self.rect.width/2 - W/2, self.rect.height/2 - H/2])

	def update(self, position):
		# sur.blit(self.image, self.rect)

		self.onHoverChange(position)

		W = self.textSurf.get_width()
		H = self.textSurf.get_height()
		self.image.blit(self.textSurf, [self.rect.width/2 - W/2, self.rect.height/2 - H/2])

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print(self.button_text + " Pressed!")
			return True
		return False

	def onHoverChange(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.textSurf = self.font.render(self.button_text, True, "green")
		else:
			self.textSurf = self.font.render(self.button_text, True, "white")