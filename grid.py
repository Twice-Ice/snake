import pygame
from globals import SCREEN_X, SCREEN_Y, BG_COLOR

class Grid:
	def __init__(self, xScale, yScale, color = (255, 255, 255)):
		self.grid = []
		self.xScale = xScale
		self.yScale = yScale
		self.xTiles = SCREEN_X//xScale
		self.yTiles = SCREEN_Y//yScale
		self.color = color

		for y in range(self.yTiles):
			self.grid.append([])
			for x in range(self.xTiles):
				self.grid[y].append([])

	def update(self, screen, table):
		self.drawLines(screen)
		self.fillSquares(screen, table)

	def drawLines(self, screen):
		for y in range(self.yTiles):
			pygame.draw.line(screen, self.color, (0, self.yScale * y), (SCREEN_X, self.yScale * y))
		for x in range(self.xTiles):
			pygame.draw.line(screen, self.color, (self.xScale * x, 0), (self.xScale * x, SCREEN_Y))
		pygame.draw.line(screen, self.color, (0, SCREEN_Y - 1), (SCREEN_X, SCREEN_Y - 1))
		pygame.draw.line(screen, self.color, (SCREEN_X - 1, 0), (SCREEN_X - 1, SCREEN_Y))
	
	def fillSquares(self, screen, table):
		for y in range(len(table)):
			for x in range(len(table[y])):
				if table[y][x] == "X":
					pygame.draw.circle(screen, self.color, (self.yScale * y - self.yScale // 2, self.xScale * x - self.xScale // 2), self.xScale/2)