import pygame
from globals import SCREEN_X, SCREEN_Y
import math
from pygame import Vector2

class Snake:
	def __init__(self, pos, xScale, yScale, length = 5):
		self.grid = []
		self.xScale = xScale
		self.yScale = yScale
		self.xTiles = SCREEN_X//xScale
		self.yTiles = SCREEN_Y//yScale
		self.length = length
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
		self.grid = [["" for i in range(self.xScale)] for i in range(self.yScale)]

		for i in range(self.length-1, 0-1, -1):
			self.velo[i] = self.velo[i - 1]

		keys = pygame.key.get_pressed()
		if True:#keys[pygame.K_w]:
			self.velo[0] = Vector2(0, -1)
		elif keys[pygame.K_a]:
			self.velo[0] = Vector2(-1, 0)
		elif keys[pygame.K_s]:
			self.velo[0] = Vector2(0, 1)
		elif keys[pygame.K_d]:
			self.velo[0] = Vector2(1, 0)
		else:
			self.velo[0] = self.velo[1]

		self.body[0] += self.velo[0]

		try:
			for i in range(self.length):
				self.grid[math.floor(self.body[i].x)][math.floor(self.body[i].y)] = "X"
		except:
			pass

		print(self.body[0], self.body[self.length-1])