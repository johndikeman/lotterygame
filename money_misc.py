import pygame, sys
from pygame.locals import *

class Money(object):
	def __init__(self,pos,img,surf):
		self.pos = pos
		self.surf = surf
		self.stage = 0
		self.alive = True
		self.img = img

	def blit(self):
		if(self.alive):
			self.surf.blit(self.img,self.pos)
		else:
			pass

class MoneyGroup(object):
	def __init__(self, money):
		self.money_list = money

	def add(self, money):
		self.money_list.append(money)

	def pop(self, money):
		return self.money_list.pop()

	def blit(self):
		for a in self.money_list:
			a.blit()

	def update(self,funds):
		bills_needed = int(funds/100)
		if(self.money_list.__len__()>bills_needed):
			self.money_list.pop()
			return -1
		else:
			return bills_needed-self.money_list.__len__()


