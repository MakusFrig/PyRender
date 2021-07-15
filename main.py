import pygame

from pygame.locals import *

import math

import os

WIDTH, HEIGHT = 1200,800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First Game")

WHITE = (255, 255, 255)

FPS = 30

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)

#YELLOW_SPACESHIP_IMAGE = pygame.image.load('put the location here')
#YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(YELLOW_SPACE_SHIP_IMAGE, (X, Y))   This is to resize

pygame.font.init()


class cube:

	def __init__(self, l, w, h):
		self.dimensions = [l, w, h]
		self.l, self.w, self.h = l,w,h
		self.ratio = l/WIDTH

	def equation(self, y = None, x = None):
		b = self.h/2
		m = -1*b/(WIDTH/2)
		if y != None:
			return (y-b)/m
		elif x != None:
			return m*x+b



def conv_coords(x = None, y = None):

	if x == None:
		if y < 0:
			return HEIGHT/2 + y
		return HEIGHT/2 - y
	elif y == None:
		if x > 0:
			return WIDTH/2 + x

		return WIDTH/2 - x
	else:
		return HEIGHT/2 + y, WIDTH/2 + x





def draw_3d(c):
	draw_window()

	vis  = int(c.l/math.sqrt(2))

	pygame.draw.polygon(WIN, RED, [(conv_coords(x = 0), conv_coords(y = c.h/2)), 
		(conv_coords(x = vis), conv_coords(y = c.equation(x = vis))), 
		(conv_coords(x = vis), conv_coords(y = 0)),
		(conv_coords(x = 0), conv_coords(y = 0))  ])


	pygame.display.update()

def draw_window():
	WIN.fill(WHITE)

	myfont = pygame.font.SysFont("Times New Roman", 30)

	textsurface = myfont.render(str(round(clock.get_fps())), False, (0,0,0))

	WIN.blit(textsurface, (0,0))

	pygame.draw.rect(WIN, (0,0,0), (0, 400, 1200, 1))

	pygame.draw.rect(WIN, (0,0,0), (600, 0, 1, 800))

	#pygame.draw.polygon(WIN, RED, [(20, 20), (25, 50), (90, 80)])






def main():
	global clock

	my_cube = cube(400, 200, 300)

	cubes = [my_cube]

	clock = pygame.time.Clock()

	running = True

	while running:
		clock.tick(FPS)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False
			

		draw_window()
		for i in cubes:	
			draw_3d(i)

		pygame.display.update()





	pygame.quit()

if __name__ == "__main__":
	main()
