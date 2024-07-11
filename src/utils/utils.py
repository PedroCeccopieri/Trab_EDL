import pygame as pg

gravidade = 5

def getImage(sheet, frame, width, height, scale, color):
	image = pg.Surface((width, height)).convert_alpha()
	image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
	image = pg.transform.scale(image, (width * scale, height * scale))
	image.set_colorkey(color)

	return image