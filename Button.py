import pygame
from const import *


class Button(pygame.sprite.Sprite):
	def __init__(self, x_pos, y_pos, button_text, group, image_path, is_text_button, button_width, button_height):
		super().__init__(group)
		self.image = pygame.image.load(image_path).convert_alpha()
		self.image = pygame.transform.scale(self.image, (button_width, button_height))
		self.image_path = image_path
		self.button_width = button_width
		self.button_height = button_height
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.is_text_button = is_text_button
		self.button_text = button_text
		if self.is_text_button:
			# Text
			self.font = pygame.font.SysFont(GAME_FONT, 48)
			self.textSurf = self.font.render(button_text, 1, HIGHLIGHT_PINK)
			W = self.textSurf.get_width()
			H = self.textSurf.get_height()
			self.image.blit(self.textSurf, [self.rect.width/2 - W/2, self.rect.height/2 - H/2])

	def update(self, position):
		if self.is_text_button:
			self.onHoverChange(position)
			W = self.textSurf.get_width()
			H = self.textSurf.get_height()
			self.image.blit(self.textSurf, [self.rect.width/2 - W/2, self.rect.height/2 - H/2])

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def onHoverChange(self, position):
		if self.is_text_button:
			if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
				self.textSurf = self.font.render(self.button_text, True, "green")
			else:
				self.textSurf = self.font.render(self.button_text, True, HIGHLIGHT_PINK)

	def changeText(self, new_text):
		if self.is_text_button:
			self.button_text = new_text
			self.image = pygame.image.load(self.image_path).convert_alpha()
			self.image = pygame.transform.scale(self.image, (self.button_width, self.button_height))
			# Text
			self.textSurf = self.font.render(self.button_text, 1, HIGHLIGHT_PINK)