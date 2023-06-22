import pygame

#button class
class Button():
	def __init__(self, x, y, image1, image2, scale):
		width = image1.get_width()
		height = image1.get_height()
		self.image1 = pygame.transform.scale(image1, (int(width * scale), int(height * scale)))
		self.image2 = pygame.transform.scale(image2, (int(width * scale), int(height * scale)))
		self.rect1 = self.image1.get_rect()
		self.rect2 = self.image2.get_rect()
		self.rect1.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect1.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		if self.rect1.collidepoint(pos):
			surface.blit(self.image2, (self.rect1.x, self.rect1.y))

		else:
			surface.blit(self.image1, (self.rect1.x, self.rect1.y))

		return action
