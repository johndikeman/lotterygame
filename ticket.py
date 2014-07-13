import pygame,random
from pygame.locals import *

class TicketManager(object):
	def __init__(self,chance,prize):
		self.chance = chance
		self.prize = prize

	def set_prize(self,prize):
		self.prize = prize

	def set_chance(self,chance):
		self.chance = chance

	def check(self):
		if(random.randint(0,self.chance)==int(self.chance/2)):
			return True
		else:
			return False
