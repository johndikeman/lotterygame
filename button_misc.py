import pygame
from pygame.locals import *


class Button(object):
	def __init__(self,surf,pos,img,ide):
		self.x, self.y = pos
		self.img = img
		self.id = ide
		self.surf = surf

	def blit(self):
		self.surf.blit(self.img,(self.x,self.y))

	def poll(self,clickpos):
		x,y = clickpos
		if(x>self.x and x<self.x+self.img.get_width() and y>self.y and y<self.y+self.img.get_height()):
			return [self.id,True]
		else:
			return [self.id,False]

class ButtonManager(object):
	def __init__(self,buttons):
		self.buttons = buttons
		self.results = []

	def poll(self,clickpos):
		self.results = []
		for a in self.buttons:
			result = a.poll(clickpos)
			if(result[1]):
				self.results.append(result[0])
		return self.results

	def blit(self):
		for a in self.buttons:
			a.blit()

	def add(self,button):
		self.buttons.append(button)

	def clear(self):
		self.buttons = []




		