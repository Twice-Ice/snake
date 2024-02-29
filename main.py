import pygame
from pygame import Vector2
from grid import Grid
from snake import Snake
from globals import SCREEN_X, SCREEN_Y, BG_COLOR
pygame.init

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Snake")

doExit = False
clock = pygame.time.Clock()

bg = Grid(20, 20, (255, 155, 155))
player = Snake(Vector2(5, 5), 20, 20)
ticker = 0

while not doExit:
	delta = clock.tick(60) / 1000
	screen.fill(BG_COLOR)
	ticker += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True

	bg.update(screen, player.grid)
	if ticker % 5 == 0:
		player.update()

	pygame.display.flip()
pygame.quit()