import pygame
from globals import SCREEN_X, SCREEN_Y
import math
from pygame import Vector2

class Snake:
	def __init__(self, pos, xScale, yScale):
		self.grid = []
		self.xScale = xScale
		self.yScale = yScale
		self.xTiles = SCREEN_X//xScale
		self.yTiles = SCREEN_Y//yScale
		self.length = 5
		self.body = []
		self.velo = []
		for y in range(self.yTiles):
			self.grid.append([])
			for x in range(self.xTiles):
				self.grid[y].append([])

		for _ in range(self.length):
			self.body.append(pos)
			self.velo.append(Vector2(0, 0))

		self.grid[math.floor(pos.x)][math.floor(pos.y)] = "X"

	def update(self):
		for i in range(self.length-1, 0-1, -1):
			self.velo[i] = self.velo[i - 1]

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.velo[0] = Vector2(0, -1)
		elif keys[pygame.K_a]:
			self.velo[0] = Vector2(-1, 0)
		elif keys[pygame.K_s]:
			self.velo[0] = Vector2(0, 1)
		elif keys[pygame.K_d]:
			self.velo[0] = Vector2(1, 0)
		else:
			self.velo[0] = self.velo[1]

		for i in range(self.length):
			self.body[i] += self.velo[i]

		try:
			self.grid[math.floor(self.body[0].x)][math.floor(self.body[0].y)] = "X"
			endx = math.floor(self.body[self.length-1].x)
			endy = math.floor(self.body[self.length-1].y)
			self.grid[endx][endy] = ""
		except:
			pass

		print(self.body[0], self.body[self.length-1])