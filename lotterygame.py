import pygame, sys, random
from pygame.locals import *
from money_misc import *
from button_misc import *
from ticket import *

menustate = True
playstate = False
loadstate = False
losestate = False

pygame.init()

display = pygame.display.set_mode((600,600))
pygame.display.set_caption("play the lottery!")

buybutton = pygame.image.load('buy.png')
cash = pygame.image.load('cash.png')
playbutton = pygame.image.load('playbutton.png')
buybutton = pygame.image.load('buy.png')
stash = pygame.image.load('stash.png')
bg = pygame.image.load('bg.png')

fps = pygame.time.Clock()

hasMadeStuff = False

money = 2000
price = 10

group = MoneyGroup([])
buttongroup = ButtonManager([])
ticket = TicketManager(10,10000)
buttongroup.add(Button(display,(100,200),playbutton,'playbutton'))
font = pygame.font.SysFont("None",30)

while True:
	display.blit(bg,(0,0))
	for event in pygame.event.get():
		if(event.type == QUIT):
			pygame.quit()
			sys.exit()
		if(menustate):
			if(event.type==MOUSEBUTTONDOWN):
				temp = pygame.mouse.get_pos()
				result = buttongroup.poll(temp)
				for a in result:
					if(a=='playbutton'):
						menustate = False
						playstate = True
		if(playstate):
			if(event.type==MOUSEBUTTONDOWN):
				temp = pygame.mouse.get_pos()
				result = buttongroup.poll(temp)
				for a in result:
					if(a=='buybutton'):
						money-=price
						if(ticket.check()):
							money+=ticket.prize


	if(menustate):
		buttongroup.blit()
			
		

	if(playstate):
		display.blit(stash,(0,0))
		#one tim operation, making the money/
		if not hasMadeStuff:
			for x in range(0,int(money/100)):
				group.add(Money((random.randint(30,450),random.randint(0,130)),cash,display))
				buttongroup.clear()
				buttongroup.add(Button(display,(150,150),buybutton,'buybutton'))
				hasMadeStuff = True
		#updating the bills on the screen
		group.blit()
		result = group.update(money)
		if(result!= -1):
			for x in range(0,result):
				group.add(Money((random.randint(30,450),random.randint(0,130)),cash,display))
		#bltting the buttons
		buttongroup.blit()
		
		#this makes the text and whatnot
		money_render = font.render(str(money),0,(0,0,0))
		display.blit(money_render,(550,500))

	pygame.display.update()
	fps.tick(30)









	