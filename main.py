#By Jack Savini
import pygame

#Before the game begins, this gives the controls to the player
print("Controls:")
print("Use WASD to move")
print("K to use Lasereyes")
print("J to Punch (When Unlocked)")
print("L to use Shield (When Unlocked)")
x = input("Press enter to begin")

pygame.init()
#To see if the fire is raging in the right room
fireplace = True

tickspeed = 60

#Accounts for door in main room
door = True

#accounts for fire movement in zelda room & fancy room
firetimer = 0

#Accounts for freeze graphic
frzz = False

#accounts for fire in zelda room
fire = True

#Accounts for lava in left room
lava = True

#Checks to see if Clyde dies
clydedeath = False

#Accounts for the tip of the laser so as t know when to freeze an object
lasertipx = 0
lasertipy = 0
lasertipx2 = 0
lasertipy2 = 0

#You start off in room 2
#Room Placement (a bit confusing)

#    4
#6-3-2-5-7
#    1

room1 = False
room02 = True
room03 = False
room04 = False
room05 = False
room06 = False
room07 = False

#checks to see if player is using attack
punching = False

#Determines which hand is punching
hand = "left"
rightpunch = True
leftpunch = False

#This is a variable which changes the size of the entire game
size = 5

#Enemy health bar length
elw = 14 * size

#Setting the size of the display
display_width = 200 * size
display_height = 150 * size
#showing the display and giving it a caption
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Macarena of Thyme')

#Starting the game not crashed
crashed = False

#enemy speed
evx = size
evy = size

# checks to see if enemy is hit by either glove
hit = True
hit2 = True

#These are all the timers needed for various reasons
frozentimer = 121
clydetimer = 0
flashtimer = 0
walktimer= 1
shieldtimer = 3600
punchtimer = 10
lavatimer = 0
wintimer = 0

#Player starting location, the postions he's facing, number of hearts he has,
x = 94 * size
y = 45 * size
facing = "down"
hearts = 4
#Player sizes(width, height, width when facing the side)
pw = 12 * size
ph = 16 * size
pw2 = 12 * size
#Making it so that when the program starts, the game knows that none of the arrow keys sre pressed
adown = False
ddown = False
wdown = False
sdown = False
#Setting the player velocity to 0
vx = 0
vy = 0
#setting a constant speed for the player
speed = size

#Setting variables for the clyde, ie starting position, size and color
ex = 93 * size
ey = display_height - 45 * size
ew = eh = 14 * size
#Setting variables for goomba
gx = 150 * size
gy = 60 * size
gw=gh=14 * size
#Checking if the clyde is frozen
frozen = False
#seeing if the player has been damaged by the clyde
damaged = False
#kb is the knockback done by the clyde when the player runs into it
kb = 20 * size

#Seeing if the player has unlocked laser eyes and seeing if their using them
lasereyes = True
lasering = False
lasereyemenu = True
#Setting laser color
lasercolor = (0,0,255)
#l represents the laser eyes on the player, lx lx2 ly and ly2 are their positions
lx = x + 4 * size
ly = y + 3 * size
lx2 = x + 7 * size
ly2 = y + 3 * size
#velocity of laser in the y and x
vlx = 0
vly = 0
#setting laser size
lw = size 
lh = size 

#w = weapon
weapon = False

ww = size * 2
ww2 = size * 2
wh = size * 2
wx = x
wy = y + 9 * size
wx2 = x + 10 * size
wy2 = y + 9 * size

#if the player is using the shield
shielding = False
#True when the player acquires the shield
shieldon = False
#places a belt buckle on the player is he has the shield

bx = x + 5 * size
by = y + 9 * size
bw = size * 2
bh = size
shieldcolor = (255, 160, 0)
#when shield is activated, this is where the players jacket will be
jx = x
jy = y + 4 * size
#Setting variables for the User Interface
#setting the width of a bar, which will go down as the player uses the laser / shield
msw = 30 * size
mfw = 30 * size
#Color of menu bars
mscolor = (160, 20, 200)
mscolor2 = (255, 160, 0)
mfcolor = (0,0,255)
#Checking to see if the player can use laser
nofreeze = False
#A bunch of downloaded sprites. the if statement is so i can minimize them in geany
if 1 < 2:
	sprite1 = pygame.image.load('sprite1.gif').convert()
	sprite1 = pygame.transform.scale(sprite1, (pw, ph))
	leftsprite = pygame.image.load('leftsprite.gif').convert()
	leftsprite = pygame.transform.scale(leftsprite, (pw2, ph))
	rightsprite = pygame.image.load('rightsprite.gif').convert()
	rightsprite = pygame.transform.scale(rightsprite, (pw2, ph))
	backsprite = pygame.image.load('backsprite.gif').convert()
	backsprite = pygame.transform.scale(backsprite, (pw, ph))
	leftsprite2 = pygame.image.load('leftsprite2.gif').convert()
	leftsprite2 = pygame.transform.scale(leftsprite2, (pw2, ph))
	rightsprite2 = pygame.image.load('rightsprite2.gif').convert()
	rightsprite2 = pygame.transform.scale(rightsprite2, (pw2, ph))
	backleftfootup = pygame.image.load('backleftfootup.gif').convert()
	backleftfootup = pygame.transform.scale(backleftfootup, (pw, ph + size))
	backrightfootup = pygame.image.load('backrightfootup.gif').convert()
	backrightfootup = pygame.transform.scale(backrightfootup, (pw, ph + size))
	rightfootup = pygame.image.load('rightfootup.gif').convert()
	rightfootup = pygame.transform.scale(rightfootup, (pw, ph + size))
	leftfootup = pygame.image.load('leftfootup.gif').convert()
	leftfootup = pygame.transform.scale(leftfootup, (pw, ph + size))
	
	room = pygame.image.load('room.gif').convert()
	room = pygame.transform.scale(room, (200 * size, 150 * size))
	room2 = pygame.image.load('room2.gif').convert()
	room2 = pygame.transform.scale(room2, (200 * size, 150 * size))
	room3 = pygame.image.load('room3.gif').convert()
	room3 = pygame.transform.scale(room3, (200 * size, 150 * size))
	room4 = pygame.image.load('room4.gif').convert()
	room4 = pygame.transform.scale(room4, (200 * size, 150 * size))
	room5 = pygame.image.load('room5.gif').convert()
	room5 = pygame.transform.scale(room5, (200 * size, 150 * size))
	room6 = pygame.image.load('room6.gif').convert()
	room6 = pygame.transform.scale(room6, (200 * size, 150 * size))
	room7 = pygame.image.load('room7.gif').convert()
	room7 = pygame.transform.scale(room7, (200 * size, 150 * size))
	
	clydepic = pygame.image.load('clyde.gif').convert()
	clydepic = pygame.transform.scale(clydepic, (14 * size, 14 * size))
	ghost = pygame.image.load('ghost.gif').convert()
	ghost = pygame.transform.scale(ghost, (14 * size, 14 * size))
	
	door2 = pygame.image.load('door2.gif').convert()
	door2 = pygame.transform.scale(door2, (13 * size, 29 * size))
	
	fire1 = pygame.image.load('fire1.gif').convert()
	fire1 = pygame.transform.scale(fire1, (16 * size, 16 * size))
	fire2 = pygame.image.load('fire2.gif').convert()
	fire2 = pygame.transform.scale(fire2, (16 * size, 16 * size))
	fireplace1 = pygame.image.load('fireplace1.gif').convert()
	fireplace1 = pygame.transform.scale(fireplace1, (13 * size, 25 * size))
	fireplace2 = pygame.image.load('fireplace2.gif').convert()
	fireplace2 = pygame.transform.scale(fireplace2, (13 * size, 25 * size))
	
	
	Shieldsprite = pygame.image.load('Shield.gif').convert()
	Shieldsprite = pygame.transform.scale(Shieldsprite, (12 * size, 11 * size))
	Shieldleftsprite = pygame.image.load('Shieldleftsprite.gif').convert()
	Shieldleftsprite = pygame.transform.scale(Shieldleftsprite, (10 * size, 11 * size))
	Shieldrightsprite = pygame.image.load('Shieldrightsprite.gif').convert()
	Shieldrightsprite = pygame.transform.scale(Shieldrightsprite, (10 * size, 11 * size))
	Shieldbacksprite = pygame.image.load('Shieldbackside.gif').convert()
	Shieldbacksprite = pygame.transform.scale(Shieldbacksprite, (12 * size, 13 * size))
	Shieldleftsprite2 = pygame.image.load('Shieldleftsprite2.gif').convert()
	Shieldleftsprite2 = pygame.transform.scale(Shieldleftsprite2, (10 * size, 11 * size))
	Shieldrightsprite2 = pygame.image.load('Shieldrightsprite2.gif').convert()
	Shieldrightsprite2 = pygame.transform.scale(Shieldrightsprite2, (10 * size, 11 * size))
	Shieldbackleftfootup = pygame.image.load('Shieldbackleftfootup.gif').convert()
	Shieldbackleftfootup = pygame.transform.scale(Shieldbackleftfootup, (12 * size, 13 * size))
	Shieldbackrightfootup = pygame.image.load('Shieldbackrightfootup.gif').convert()
	Shieldbackrightfootup = pygame.transform.scale(Shieldbackrightfootup, (12 * size, 13 * size))
	Shieldrightfootup = pygame.image.load('Shieldrightfootup.gif').convert()
	Shieldrightfootup = pygame.transform.scale(Shieldrightfootup, (12 * size, 12 * size))
	Shieldleftfootup = pygame.image.load('Shieldleftfootup.gif').convert()
	Shieldleftfootup = pygame.transform.scale(Shieldleftfootup, (12 * size, 12 * size))
	bam = pygame.image.load('bam.gif').convert()
	bam = pygame.transform.scale(bam, (11 * size, 11 * size))
	frzzz = pygame.image.load('frzzz.gif').convert()
	frzzz = pygame.transform.scale(frzzz, (11 * size, 11 * size))
	
	lava1 = pygame.image.load('lava1.gif').convert()
	lava1 = pygame.transform.scale(lava1, (70 * size, 103 * size))
	lava2 = pygame.image.load('lava2.gif').convert()
	lava2 = pygame.transform.scale(lava2, (70 * size, 103 * size))
	lava3 = pygame.image.load('lava3.gif').convert()
	lava3 = pygame.transform.scale(lava3, (70 * size, 103 * size))
	lava4 = pygame.image.load('lava4.gif').convert()
	lava4 = pygame.transform.scale(lava4, (70 * size, 103 * size))
	lava5 = pygame.image.load('lava5.gif').convert()
	lava5 = pygame.transform.scale(lava5, (70 * size, 103 * size))
	lava6 = pygame.image.load('lava6.gif').convert()
	lava6 = pygame.transform.scale(lava6, (70 * size, 103 * size))
	lava7 = pygame.image.load('lava7.gif').convert()
	lava7 = pygame.transform.scale(lava7, (70 * size, 103 * size))
	lava8 = pygame.image.load('lava8.gif').convert()
	lava8 = pygame.transform.scale(lava8, (70 * size, 103 * size))
	lava9 = pygame.image.load('lava9.gif').convert()
	lava9 = pygame.transform.scale(lava9, (70 * size, 103 * size))
	lava10 = pygame.image.load('lava10.gif').convert()
	lava10 = pygame.transform.scale(lava10, (70 * size, 103 * size))
	lava11 = pygame.image.load('lava11.gif').convert()
	lava11 = pygame.transform.scale(lava11, (70 * size, 103 * size))
	lava12 = pygame.image.load('lava12.gif').convert()
	lava12 = pygame.transform.scale(lava12, (70 * size, 103 * size))
	
	def backrightfootupside(x, y):
		gameDisplay.blit(backrightfootup, (x,y))

	def backleftfootupside(x, y):
		gameDisplay.blit(backleftfootup, (x,y))

	def rightfootupside(x, y):
		gameDisplay.blit(rightfootup, (x,y))

	def leftfootupside(x, y):
		gameDisplay.blit(leftfootup, (x,y))

	def leftside2(x, y):
		gameDisplay.blit(leftsprite2, (x,y))
		
	def rightside2(x, y):
		gameDisplay.blit(rightsprite2, (x,y))

	def cat(x, y):
		gameDisplay.blit(sprite1, (x,y))

	def leftside(x, y):
		gameDisplay.blit(leftsprite,(x,y))
		
	def rightside(x, y):
		gameDisplay.blit(rightsprite,(x,y))
		
	def backside(x, y):
		gameDisplay.blit(backsprite,(x,y))
		
	def laser(lx, ly, lw, lh, color):
		pygame.draw.rect(gameDisplay, color, [lx, ly, lw, lh])
		
	def shield(jx, jy):
		gameDisplay.blit(Shieldsprite, (jx, jy))
	
	def Shieldbackrightfootupside(x, y):
		gameDisplay.blit(Shieldbackrightfootup, (x,y))

	def Shieldbackleftfootupside(x, y):
		gameDisplay.blit(Shieldbackleftfootup, (x,y))

	def Shieldrightfootupside(x, y):
		gameDisplay.blit(Shieldrightfootup, (x,y))

	def Shieldleftfootupside(x, y):
		gameDisplay.blit(Shieldleftfootup, (x,y))

	def Shieldleftside2(x, y):
		gameDisplay.blit(Shieldleftsprite2, (x,y))
		
	def Shieldrightside2(x, y):
		gameDisplay.blit(Shieldrightsprite2, (x,y))

	def Shieldleftside(x, y):
		gameDisplay.blit(Shieldleftsprite,(x,y))
		
	def Shieldrightside(x, y):
		gameDisplay.blit(Shieldrightsprite,(x,y))
		
	def Shieldbackside(x, y):
		gameDisplay.blit(Shieldbacksprite,(x,y))
	
	def Room(x, y):
		gameDisplay.blit(room,(x,y))
		
	def Room2(x, y):
		gameDisplay.blit(room2,(x,y))
		
	def Room3(x, y):
		gameDisplay.blit(room3,(x,y))
	
	def Room4(x, y):
		gameDisplay.blit(room4,(x,y))
		
	def Room5(x, y):
		gameDisplay.blit(room5,(x,y))
		
	def Room6(x, y):
		gameDisplay.blit(room6,(x,y))
		
	def Room7(x, y):
		gameDisplay.blit(room7,(x,y))
		
	def Clyde(x, y):
		gameDisplay.blit(clydepic,(x,y))
		
	def Ghost(x, y):
		gameDisplay.blit(ghost,(x,y))
		
	def bamn(x, y):
		gameDisplay.blit(bam,(x,y))
		
	def frz(x, y):
		gameDisplay.blit(frzzz,(x,y))
		
	def Lava1(x, y):
		gameDisplay.blit(lava1,(x,y))
		
	def Lava2(x, y):
		gameDisplay.blit(lava2,(x,y))
		
	def Lava3(x, y):
		gameDisplay.blit(lava3,(x,y))
		
	def Lava4(x, y):
		gameDisplay.blit(lava4,(x,y))
		
	def Lava5(x, y):
		gameDisplay.blit(lava5,(x,y))
		
	def Lava6(x, y):
		gameDisplay.blit(lava6,(x,y))
		
	def Lava7(x, y):
		gameDisplay.blit(lava7,(x,y))
		
	def Lava8(x, y):
		gameDisplay.blit(lava8,(x,y))
		
	def Lava9(x, y):
		gameDisplay.blit(lava9,(x,y))
		
	def Lava10(x, y):
		gameDisplay.blit(lava10,(x,y))
		
	def Lava11(x, y):
		gameDisplay.blit(lava11,(x,y))
		
	def Lava12(x, y):
		gameDisplay.blit(lava12,(x,y))
		
	def Fire1(x, y):
		gameDisplay.blit(fire1,(x,y))
		
	def Fire2(x, y):
		gameDisplay.blit(fire2,(x,y))
		
	def Door(x, y):
		gameDisplay.blit(door2,(x,y))
		
	def Fireplace1(x, y):
		gameDisplay.blit(fireplace1,(x,y))
		
	def Fireplace2(x, y):
		gameDisplay.blit(fireplace2,(x,y))

#shortcut to change fps
clock = pygame.time.Clock()

#Setting the appearances of the player and the shield
shielded = shield
player = cat

#while loop for whole game
while crashed == False:
	#saying that is the lasereys are normal sized, then the player is not using the laser
	if lw == lh == size:
		lasering = False
	#setting some variables for certain key presses
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				tickspeed = 60
			#if a is pressed, x velocity is negative speed, moving the player left
			#y velocity is cancelled, because i want the player to move in only 4 directions
			#walktimer resets, thus resetting the character walk animation
			#laser velocity is reset to 0, so the player doesnt laser while walking
			#adown = True allows a variable to check if a is pushed
			#I did the same thing for all asdw keys
			if event.key == pygame.K_a:
				walktimer= 1
				vx -= speed
				vy-=vy
				lw = size
				lh = size
				vlx = 0
				vly = 0
				adown = True
			if event.key == pygame.K_d:
				walktimer= 1
				vx += speed
				vy-=vy
				lw = size
				lh = size
				vlx = 0
				vly = 0
				ddown = True
			if event.key == pygame.K_w:
				walktimer= 1
				vy -= speed
				vx-=vx
				lw = size
				lh = size
				vlx = 0
				vly = 0
				wdown = True
			if event.key == pygame.K_s:
				walktimer= 1
				vy += speed
				vx-=vx
				lw = size
				lh = size
				vlx = 0
				vly = 0
				sdown = True
			#The I key shoots lasers! pew pew
			if event.key == pygame.K_k:
				if nofreeze == False:
					lasering = True
					if lasereyes == True:
						#Stops the player
						vx = vy = 0
						#checks if player is facing a certain direction
						if facing == "left":
							#increases velocity of lasers
							vlx = 2 * size

						if facing == "right":
							vlx = 2 * size
							
						if facing == "up":
							#changes laser color to chracters skin color as to hide it
							lasercolor = (0,0,255)
							vly = 2 * size
							ly = ly2 = y - size

						if facing == "down":
							vly = 2 * size

			#L key activates magic shield
			if event.key == pygame.K_l:
				if shieldon == True:
					if shieldtimer > 3600:
						shieldtimer = 0
						shielding = True
			if event.key == pygame.K_j:
				#~ vx = 0
				#~ vy = 0
				if facing == "right":
					if punchtimer == 10:
						punching = True
						punchtimer = 0
				if facing == "left":
					if punchtimer == 10:
						punching = True
						punchtimer = 0
				if facing == "down":
					if punchtimer == 10:
						punching = True
						punchtimer = 0
				if facing == "up":
					if punchtimer == 10:
						punching = True
						punchtimer = 0
			
		if event.type == pygame.KEYUP:
			#Tests for a key being unpressed and stops the player movement
			if event.key == pygame.K_a:
				vx -= vx
				adown = False
				#moves the player in a different direction if a different button is pressed
				if sdown == True and wdown == True:
					vy -= vy
				elif sdown == True:
					walktimer= 1
					vy = speed
				elif wdown == True:
					walktimer= 1
					vy = -speed
				if ddown == True:
					walktimer= 1
					vx += speed
			if event.key == pygame.K_d:
				vx -= vx
				ddown = False
				if sdown == True and wdown == True:
					vy -= vy
				elif sdown == True:
					walktimer= 1
					vy = speed
				elif wdown == True:
					walktimer= 1
					vy = -speed
				if adown == True:
					walktimer= 1
					vx -= speed
			if event.key == pygame.K_s:
				vy -= vy
				sdown = False
				if adown == True and ddown == True:
					vx -= vx
				elif adown == True:
					walktimer= 1
					vx = -speed
				elif ddown == True:
					walktimer= 1
					vx = speed
				if wdown == True:
					walktimer= 1
					vy -= speed
			if event.key == pygame.K_w:
				vy -= vy
				wdown = False
				if adown == True and ddown == True:
					vx -= vx
				elif adown == True:
					walktimer= 1
					vx = -speed
				elif ddown == True:
					walktimer= 1
					vx = speed
				if sdown == True:
					walktimer= 1
					vy += speed
			if event.key == pygame.K_k:
				#deactivates lasereyes if k is unpressed
				if lasereyes == True:
					if lasering == True:
						if facing == "left":
							lx = lx2 = x + 3 * size
							ly = ly2 = y + 3 * size
							vlx = 0
							vly = 0
							lw = size
							lh = size
							lasering == False
							if ddown == True:
								vx += speed
							elif adown == True:
								vx -= speed
							elif sdown == True:
								vy += speed
							elif wdown == True:
								vy -= speed
						if facing == "right":
							rs = 0
							vlx = 0
							vly = 0
							lw = size
							lh = size
							lasering == False
							if ddown == True:
								vx += speed
							elif adown == True:
								vx -= speed
							elif sdown == True:
								vy += speed
							elif wdown == True:
								vy -= speed
						if facing == "up":
							lx = x + 4 * size
							lx2 = x + 7 * size
							ly = ly2 = y
							vlx = 0
							vly = 0
							lw = size
							lh = size
							lasercolor = (153,229,80)
							lasering == False
							if ddown == True:
								vx += speed
							elif adown == True:
								vx -= speed
							elif sdown == True:
								vy += speed
							elif wdown == True:
								vy -= speed
						if facing == "down":
							vlx = 0
							vly = 0
							lw = size
							lh = size
							lasering == False
							if ddown == True:
								vx += speed
							elif adown == True:
								vx -= speed
							elif sdown == True:
								vy += speed
							elif wdown == True:
								vy -= speed
	#makes the laser grow/move & accounts for the location of the tip
	if lasering == True:
		if facing == "left":
			lasertipx = lasertipx2 = lx
			lasertipy = lasertipy2 = ly
		if facing == "right":
			lasertipx = lasertipx2 = lx + lw
			lasertipy = lasertipy2 = ly + lh
		if facing == "up":
			lasertipx = lx
			lasertipx2 = lx2
			lasertipy = lasertipy2 = ly
		if facing == "down":
			lasertipx = lx
			lasertipx2 = lx2
			lasertipy = lasertipy2 = ly + lh
	
	#For when the player is punching
	if punchtimer <= 9:
		if facing == "left":
			#moves boxing glove forward
			wx = wx2 = x - 6 * size
			wy = wy2 = y + 9 * size
			#switches hands with each punch
			if punchtimer == 9:
				if hand == "left":
					hand = "right"
				elif hand == "right":
					hand = "left"
				wx = wx2 = x + 4 * size
				wy = wy2 = y + 9 * size
		#same but for the right side, etc etc
		if facing == "right":
			wx = wx2 = x + 16 * size
			wy = wy2 = y + 9 * size
			if punchtimer == 9:
				if hand == "left":
					hand = "right"
				elif hand == "right":
					hand = "left"
				wx = wx2 = x + 6 * size
				wy = wy2 = y + 9 * size
		if facing == "up":
			wx = x
			wx2 = x + 11 * size
			if hand == "left":
				ww = 2 * size
				wy = y - 6 * size
			elif hand == "right":	
				ww2 = 2 * size
				wy2 = y - 6 * size
				wx2 = x + 10 * size
			if punchtimer == 9:
				if hand == "left":
					hand = "right"
					ww = size
				elif hand == "right":
					hand = "left"
					ww2 = size
				
				wx = x
				wx2 = x + 11 * size
				wy = wy2 = y + 9 * size
		if facing == "down":
			wx = x
			wx2 = x + 10 * size
			if hand == "left":
				wy2 = y + 20 * size
			elif hand == "right":
				wy = y + 20 * size
			if punchtimer == 9:
				if hand == "left":
					hand = "right"
				elif hand == "right":
					hand = "left"
				wx = x
				wx2 = x + 10 * size
				wy = wy2 = y + 9 * size
				
	#sets up boundaries for every room
	if room1 == True:
		if x <= 16 * size:
			if adown == True:
				vx -= vx
				
		if y <= 20 * size:
			#accounts for specific y coordinates which the player can pass (doorways)
			if x < 87 * size:
				if wdown == True:
					vy -= vy
				
			if x + pw > 113 * size:
				if wdown == True:
					vy -= vy
					
			if y < 20 * size:
				if x <= 87 * size:
					if ddown == False:
						vx -= vx
				if x + pw >= 113 * size:
					if adown == False:
						vx -= vx
				
		if x + pw2 >= display_width - 16 * size:
			if ddown == True:
				vx -= vx
				
				
		if y + ph >= display_height - 16 * size:
			if sdown == True:
				vy -= vy			
	#same as room 1, so on and so forth
	if room02 == True:
		if door == False:
			if x <= 16 * size:
				if y < 70 * size:
					if adown == True:
						vx -= vx
				if y + ph > 95 * size:
					if adown == True:
						vx -= vx
				if x < 16 * size:
					if y <= 70 * size:
						if sdown == False:
							vy -= vy
					if y + ph >= 95 * size:
						if wdown == False:
							vy -= vy
		elif door == True:
			if x<= 16 * size:
				if adown == True:
					vx -= vx
				
		if y <= 20 * size:
			if x < 87 * size:
				if wdown == True:
					vy -= vy
			if x + pw > 113 * size:
				if wdown == True:
					vy -= vy
			if y < 20 * size:
				if x <= 87 * size:
					if ddown == False:
						vx -= vx
				if x + pw >= 113 * size:
					if adown == False:
						vx -= vx
			
				
		if x + pw2 >= display_width - 16 * size:
			if y < 70 * size:
				if ddown == True:
					vx -= vx
			if y + ph > 95 * size:
				if ddown == True:
					vx -= vx
			if x + pw > display_width - 16 * size:
				if y <= 70 * size:
					if sdown == False:
						vy -= vy
				if y + ph >= 95 * size:
					if wdown == False:
						vy -= vy
		if y + ph >= display_height - 16 * size:
			if x < 87 * size:
				if sdown == True:
					vy -= vy
			if x + pw > 113 * size:
				if sdown == True:
					vy -= vy
			if y + ph > display_height - 16 * size:
				if x <= 87 * size:
					if ddown == False:
						vx -= vx
				if x + pw >= 113 * size:
					if adown == False:
						vx -= vx
	if room03 == True:
		if x <= 16 * size:
			if y < 70 * size:
				if adown == True:
					vx -= vx
			if y + ph > 95 * size:
				if adown == True:
					vx -= vx
			if x < 16 * size:
				if y <= 70 * size:
					if sdown == False:
						vy -= vy
				if y + ph >= 95 * size:
					if wdown == False:
						vy -= vy
				
		if y <= 20 * size:	
			if wdown == True:
					vy -= vy
			
				
		if x + pw2 >= display_width - 16 * size:
			if y < 70 * size:
				if ddown == True:
					vx -= vx
			if y + ph > 95 * size:
				if ddown == True:
					vx -= vx
			if x + pw > display_width - 16 * size:
				if y <= 70 * size:
					if sdown == False:
						vy -= vy
				if y + ph >= 95 * size:
					if wdown == False:
						vy -= vy
		if y + ph >= display_height - 16 * size:
			if sdown == True:
				vy -= vy
		
		if lava == True:
			if room03 == True:
				if x < 127 * size:
					x = 160 * size
					y = 74 * size
					hearts -= 1					
	if room04 == True:
		if y + ph >= display_height - 16 * size:
			if x < 87 * size:
				if sdown == True:
					vy -= vy
			if x + pw > 113 * size:
				if sdown == True:
					vy -= vy
			if y + ph > display_height - 16 * size:
				if x <= 87 * size:
					if ddown == False:
						vx -= vx
				if x + pw >= 113 * size:
					if adown == False:
						vx -= vx
		if y <= 80 * size:
			if wdown == True:
				vy -= vy
		if x <= 16 * size:
			if adown == True:
				vx -= vx
		if x + pw >= display_width - 16 * size:
			if ddown == True:
				vx -= vx				
	if room05 == True:
		if x <= 16 * size:
			if y < 70 * size:
				if adown == True:
					vx -= vx
			if y + ph > 95 * size:
				if adown == True:
					vx -= vx
			if x < 16 * size:
				if y <= 70 * size:
					if sdown == False:
						vy -= vy
				if y + ph >= 95 * size:
					if wdown == False:
						vy -= vy
				
		if y <= 20 * size:	
			if wdown == True:
				vy -= vy
	
			
		if fireplace == True:		
			if x + pw2 >= display_width - 16 * size:	
				if ddown == True:
					vx -= vx
		elif fireplace == False:
			if x + pw2 >= display_width - 16 * size:
				if y < 70 * size:
					if ddown == True:
						vx -= vx
				if y + ph > 95 * size:
					if ddown == True:
						vx -= vx
				if x + pw > display_width - 16 * size:
					if y <= 70 * size:
						if sdown == False:
							vy -= vy
					if y + ph >= 95 * size:
						if wdown == False:
							vy -= vy
			
		if y + ph >= display_height - 16 * size:
			if sdown == True:
				vy -= vy	
	if room06 == True:
		if x <= 16 * size:
			if adown == True:
				vx -= vx

				
		if y <= 20 * size:
			if wdown == True:
				vy -= vy

		if x + pw2 >= display_width - 16 * size:
			if y < 70 * size:
				if ddown == True:
					vx -= vx
			if y + ph > 95 * size:
				if ddown == True:
					vx -= vx
			if x + pw > display_width - 16 * size:
				if y <= 70 * size:
					if sdown == False:
						vy -= vy
				if y + ph >= 95 * size:
					if wdown == False:
						vy -= vy
		if y + ph >= display_height - 16 * size:	
			if sdown == True:
				vy -= vy				
	if room07 == True:
		if x <= 16 * size:
			if y < 70 * size:
				if adown == True:
					vx -= vx
			if y + ph > 95 * size:
				if adown == True:
					vx -= vx
			if x < 16 * size:
				if y <= 70 * size:
					if sdown == False:
						vy -= vy
				if y + ph >= 95 * size:
					if wdown == False:
						vy -= vy
				
		if y <= 50 * size:	
			if wdown == True:
				vy -= vy
	
		if x + pw2 >= display_width - 141 * size:	
			if ddown == True:
				vx -= vx
		
		if y + ph >= display_height - 46 * size:
			if sdown == True:
				vy -= vy
	
	#Makes it so that if the character moves in the y, 
	#it can't move in the x, for an arcady feel
	if vy == vx:
		vy = 0
	if vy == -vx:
		vy = 0
	
	#When the enemy has been frozen for 2 seconds, it is unfrozen
	if frozentimer == 120:
		frozen = False
	
	#Checks if the player & enemy overlap
	if x + pw > ex and y + ph > ey and y < ey + eh and x < ex + ew:
		if frozen == False:
			#if the enemy in not frozen, the player will be knocked back
			if x > ex + ew - 4 * size:
				if x + pw + kb < display_width - 17 * size:
					x += kb
					lx += kb
					lx2 += kb
					bx += kb
					jx += kb
					wx += kb
					wx2 += kb
				else:
					x1 = x
					x = display_width - pw - 17 * size
					x2 = x - x1
					lx += x2
					lx2 += x2
					bx += x2
					jx += x2
					wx += x2
					wx2 += x2
			if x + pw < ex + 4 * size:
				if x - kb > 17 * size:
					x -= kb
					lx -= kb
					lx2 -= kb
					bx -= kb
					jx -= kb
					wx -= kb
					wx2 -= kb
				else:
					x1 = x
					x = 17 * size
					x2 = x - x1
					lx += x2
					lx2 += x2
					bx += x2
					jx += x2
					wx += x2
					wx2 += x2
			if y > ey + eh - 4 * size:
				if y + ph + kb < display_height - 17 * size:
					y += kb
					ly += kb
					ly2 += kb
					by += kb
					jy += kb
					wy += kb
					wy2 += kb
				else:
					y1 = y
					y = display_height - ph - 17 * size
					y2 = y - y1
					ly += y2
					ly2 += y2
					by += y2
					jy += y2
					wy += y2
					wy2 += y2
			if y + ph < ey + 4 * size:
				if y - kb > 20 * size:
					y -= kb
					ly -= kb
					ly2 -= kb
					by -= kb
					jy -= kb
					wy -= kb
					wy2 -= kb
				else:
					y1 = y
					y = 20 * size
					y2 = y - y1
					ly += y2
					ly2 += y2
					by += y2
					jy += y2
					wy += y2
					wy2 += y2
			if shielding == False:
				hearts -= 1
		if frozen == True:
			
			if x >= ex + ew and adown == True:
				vx -= vx
			if x + pw <= ex and ddown == True:
				vx -= vx
			if y >= ey + eh and wdown == True:
				vy -= vy
			if y + ph <= ey and sdown == True:
				vy -= vy
	
	#checks to see if the enemy is frozen, and if it isnt, it makes
	#Clyde move towards the player
	#Clyde only moves every fifth tick, so that the player can be quicker
	#than him, and so there are no visually unappealling disjoined pixels
	if frozen == False:	
		if clydetimer < 2:	
			if shielding == False:	
				if x > ex and ex + ew < display_width - 17 * size:
					ex += evx
				if x < ex and ex > 17 * size:
					ex -= evx
				if y > ey and ey + eh < display_height - 17 * size:
					ey += evy
				if y < ey and ey > 32 * size:
					ey -= evy

			elif shielding == True:
				if x > ex and ex > 17 * size:
					ex -= evx
				if x < ex and ex + ew < display_width - 17 * size:
					ex += evx
				if y > ey and ey > 32 * size:
					ey -= evy
				if y < ey and ey + eh < display_height - 17 * size:
					ey += evy
	

	#Freezes the enemy if the freeze laser tip equals its location	
	if lasertipx >= ex and lasertipx <= ex + ew and lasertipy <= ey + eh and lasertipy >= ey and lasering == True: 
		frzz = True
		frozen = True
		ecolor = (200,200,255)
		vlx = 0
		vly = 0
		frozentimer = 0
	elif lasertipx2 >= ex and lasertipx2 <= ex + ew and lasertipy2 <= ey + eh and lasertipy2 >= ey and lasering == True: 
		frzz = True
		frozen = True
		ecolor = (200,200,255)
		vlx = 0
		vly = 0
		frozentimer = 0
	else:
		frzz = False
	
	#Adds velocity to the player so it moves
	#Moves everything else with the player(eg beltbuckle, eyes, jacket etc)
	x += vx
	y += vy
	lw += vlx
	lh += vly
	if facing == "left":
		lx -= vlx
		lx2 -= vlx
	if facing == "up":
		ly -= vly
		ly2 -= vly
	wx += vx
	wy += vy
	wx2 += vx
	wy2 += vy
	
	#Stops the laser from growing if the player isnt pressing it
	if lasering == False:
		lx += vx
		ly += vy
		lx2 += vx
		ly2 += vy
	
	
	jx += vx
	jy += vy
	
	bx += vx
	by += vy
	
	#If the player moves right, then the player faces right, and all of 
	#its equipment too.
	if vx == speed:
		facing = "right"
		if punchtimer >= 10:
			wh = ww = ww2 = size * 2
			wx = wx2 = x + 6 * size
			wy = wy2 = y + size * 9
		jx = x + size
		jy = y + 4 * size
		lasercolor = (0,0,255)
		lx = x + 8 * size
		lx2 = x + 8 * size
		ly = y + 3 * size
		ly2 = y + 3 * size
		bx = x + 10 * size
		by = y + 9 * size
		bw = size
		bh = size
		shieldcolor = (255,160,0)	
		if walktimer== 1:
			player = rightside2
			shielded = Shieldrightside2
		elif walktimer== 10:
			player = rightside
			shielded = Shieldrightside
		elif walktimer== 20:
			player = rightside2
			shielded = Shieldrightside2
		elif walktimer== 30:
			player = rightside
			shielded = Shieldrightside
	#Same as above but left now
	elif vx == -speed:
		facing = "left"
		if punchtimer >= 10:
			ww = ww2 = wh = size * 2
			wx = wx2 = x + size * 4
			wy = wy2 = y + 9 * size
		jx = x + size
		jy = y + 4 * size
		lasercolor = (0,0,255)
		lx = x + 3 * size
		lx2 = x + 3 * size
		ly = y + 3 * size
		ly2 = y + 3 * size
		bx = x + size
		by = y + 9 * size
		bw = size
		bh = size
		shieldcolor = (255,160,0)		
		if walktimer== 1:
			player = leftside2
			shielded = Shieldleftside2
		elif walktimer== 10:
			player = leftside
			shielded = Shieldleftside
		elif walktimer== 20:
			player = leftside2
			shielded = Shieldleftside2
		elif walktimer== 30:
			player = leftside
			shielded = Shieldleftside
	#etc
	elif vy == speed:
		facing = "down"
		if punchtimer >= 10:
			wh = ww2 = ww = size * 2
			wx = x
			wx2 = x + 10 * size
		bx = x + 5 * size
		by = y + 9 * size
		bw = 2 * size
		bh = size
		shieldcolor = (255,160,0)
		jy = y + 4 * size
		jx = x
		lasercolor = (0,0,255)
		lx = x + 4 * size
		ly = y + 3 * size
		lx2 = x + 7 * size
		ly2 = y + 3 * size
		if walktimer== 1:
			player = leftfootupside
			shielded = Shieldrightfootupside
		elif walktimer== 10:
			shielded = shield
			player = cat
		elif walktimer== 20:
			player = rightfootupside
			shielded = Shieldleftfootupside
		elif walktimer== 30:
			shielded = shield
			player = cat
	#etc
	elif vy == -speed:
		facing = "up"
		if punchtimer >= 10:
			wh = size * 2
			ww = ww2 = size
			wx = x
			wx2 = x + 11 * size
		jx = x 
		jy = y + 3 * size
		bx = x + 5 * size
		by = y + 8 * size
		bw = 2 * size
		shieldcolor = (251,242,54)
		bh = size
		lasercolor = (153,229,80)
		lx = x + 4 * size
		ly = y
		lx2 = x + 7 * size
		ly2 = y
		if walktimer== 1:
			player = backleftfootupside
			shielded = Shieldbackleftfootupside
		elif walktimer== 10:
			player = backside
			shielded = Shieldbackside
		elif walktimer== 20:
			player = backrightfootupside
			shielded = Shieldbackrightfootupside
		elif walktimer== 30:
			player = backside
			shielded = Shieldbackside
	#Makes the player sprite stay in the correct direction if the
	#player stops in its tracks
	if vx == 0 and vy == 0:
		if facing == "up":
			player = backside
			shielded = Shieldbackside
		if facing == "down":
			player = cat	
			shielded = shield
		if facing == "left":
			player = leftside
			shielded = Shieldleftside
		if facing == "right":
			player = rightside
			shielded = Shieldrightside
	
	#Makes Clyde a spooky ghost when the shield is activated
	if shielding == True:
		clyde = Ghost
	elif shielding == False:
		clyde = Clyde
		
	#Makes sure the golves are in an idle position
	hit = False
	hit2 = False
	
	#If the boxing glove is in contact with the ghost, the ghost loses
	#health on its lifebar
	if weapon == True:
		if wx < ex + ew and wx + ww > ex and wy < ey + eh and wy + wh > ey:
			if clyde == Ghost:
				if elw > 0:
					hit = True
					if punching == True:
						elw -= size
						punching = False
		if wx2 < ex + ew and wx2 + ww > ex and wy2 < ey + eh and wy2 + wh > ey:
			if clyde == Ghost:
				if elw > 0:
					hit2 = True
					if punching == True:
						elw -= size
						punching = False
	
	#If the enemy is frozen, the player cannot pass through it				
	if frozen == True:
		if x < ex - size + 15 * size and x + pw2 > ex and y < ey - size + 16 * size and y + ph > ey - size:
			if x >= ex - size + 14 * size:
				x += speed
				bx += speed
				wx+= speed
				wx2+= speed
				jx+= speed
				lx+= speed
				lx2+= speed
			if x + pw2 <= ex + size:
				x -= speed
				bx -= speed
				wx-= speed
				wx2-= speed
				jx-= speed
				lx-= speed
				lx2-= speed
			if y >= ey + 14 * size:
				y += speed
				by += speed
				wy+= speed
				wy2+= speed
				jy+= speed
				ly+= speed
				ly2+= speed
			if y + ph <= ey:
				y -= speed
				by -= speed
				wy-= speed
				wy2-= speed
				jy-= speed
				ly-= speed
				ly2-= speed
	#Sets a black screen for the background
	laser(0,0,display_width,display_height,(0,0,0))
	
	#Visualizes room one over the black screen, and shows clyde if he is
	#still alive. Moves clyde 10000 pixels out of screen if he's dead
	if room1 == True:
		Room(0,0)
		if elw > 0:
			if frozen == True:
				laser(ex - size, ey - size, 16 * size, 16 * size, (200,200,255))
			clyde(ex,ey)
		else:
			ex = 10000 * size
			ey = 10000 * size			
	elif room1 == False:
		ex = 10000 * size
		ey = 10000 * size
	
	#Shows the visual of room 2(pink room)
	if room02 == True:
		Room2(0,0)
	
	#Visual of room 3(lava room). There is an animation of moving lava
	#as well, which is due to its changing sprite every 3 frames
	if room03 == True:
		Room3(0,0)
		if lava == True:
			if 0 <= lavatimer <= 2:
				Lava1(65 * size,31 * size)
			if 3 <= lavatimer <= 5:
				Lava2(65 * size,31 * size)
			if 6 <= lavatimer <= 8:
				Lava3(65 * size,31 * size)
			if 9 <= lavatimer <= 11:
				Lava4(65 * size,31 * size)
			if 12 <= lavatimer <= 14:
				Lava5(65 * size,31 * size)
			if 15 <= lavatimer <= 17:
				Lava6(65 * size,31 * size)
			if 18 <= lavatimer <= 20:
				Lava7(65 * size,31 * size)
			if 21 <= lavatimer <= 23:
				Lava8(65 * size,31 * size)
			if 24 <= lavatimer <= 26:
				Lava9(65 * size,31 * size)
			if 27 <= lavatimer <= 29:
				Lava10(65 * size,31 * size)
			if 30 <= lavatimer <= 32:
				Lava11(65 * size,31 * size)
			if 33 <= lavatimer <= 35:
				Lava12(65 * size,31 * size)
	#If the enemy uses his laser on the lava, it freezes
	if room03 == True:
		if lasering == True:
			if lasertipx < 100 * size:
				if lava == True:
					vlx = 0
					lw = lw2 = size
					lh = lh2 = size
					lx = lx2 = x + 3 * size
					ly = ly2 = y + 3 * size
					lava = False
	#makes a icy rectangle in place of lava if the enemy freezes the river
	if lava == False:
		if room03 == True:
			laser(65 * size, 31 * size, 70 * size, 103 * size, (200,200,255))
	
	#Visualizes room 4(zelda room)
	#Makes a fire animation in the room, and adds 2 2x2 pixel sprites
	#to represent a weapon, which disappear when the player comes across
	#them, giving them the ability to use the boxing gloves	
	if room04 == True:
		Room4(0,0)
		if fire == True:
			if firetimer <= 2:
				Fire1(140 * size, 59 * size)
				Fire1(44 * size, 59 * size)
			if firetimer >= 3:
				Fire2(140 * size, 59 * size)
				Fire2(44 * size, 59 * size)
		if weapon == False:
			laser(96 * size, 90 * size, 2 * size, 2 * size, (200,0,0))
			laser(102 * size, 90 * size, 2 * size, 2 * size, (200,0,0))
		if weapon == True:
			laser(16 * size, 31 * size, 168 * size, 25 * size,(0,0,0))
		if y <= 85 * size and x >= 90 * size and x + pw <= 110 * size:
			weapon = True
	
	#Sets up room 5(fancy room)
	#Has a moving fire animation, lest the player uses his ice eyes on it
	if room05 == True:
		Room5(0,0)
		if fireplace == True:
			if firetimer <= 2:
				Fireplace1(184 * size, 71 * size)
			elif firetimer > 2:
				Fireplace2(184 * size, 71 * size)
		
	#Sets up final room, sets a timer for the game to quit eventually
	if room06 == True:
		Room6(0,0)
		###################################wintimer += 1
	
	#Shows the secret room behind the fireplace, has the belt buckle which
	#Gives the power to use the shield
	if room07 == True:
		Room7(0,0)
		if shieldon == False:
			laser(35 * size, 82 * size, size, 2 * size, (255,160,0))
		if x > 25 * size:
			shieldon = True
	
	#Crashes the game after 4 seconds in the final room	
	if wintimer > 240:
		crashed = True
		print("You Won!")
		
	#visual of the player
	player(x, y)
	#Visual of the jacket/shield
	if shielding == True:
		shielded(jx, jy)
	
	#Visual of the enemy health bar
	if elw > 0:
		laser( ex, ey - 4 * size, 14 * size, 2 * size, (0,0,0))
		laser( ex, ey - 4 * size, elw, 2 * size, (200,0,0))
	
	#Visual of a belt buckle when the player has the shield
	if shieldon == True:
		laser(bx, by, bw, bh, shieldcolor)
	
	#Visual of the boxing gloves
	if weapon == True:
		laser(wx,wy,ww,wh,(200,0,0))
		laser(wx2,wy2,ww2,wh,(200,0,0))
	
	#Visual of the blue icy eyes
	if lasereyes == True:
		laser(lx, ly, lw, lh, lasercolor)
		laser(lx2, ly2, lw, lh, lasercolor)

	#Visual of a pure black bar to put the UI on
	laser(0,0,display_width,15*size,(0,0,0))
	
	#Shield bar
	if shieldon == True:
		laser(5*size,5*size,30*size,5*size,mscolor)
		if msw > 1:
			laser(5*size,5*size,msw,5*size, mscolor2)
	
	#Sets a bar on top of the player over the doorway, so if the player
	#goes under a doorway it looks as if he is leaving the room		
	if room1 == True:
		laser(80 * size,16 * size,40 * size,2 * size,(172,50,50))
		laser(80 * size,15 * size,40 * size,1 * size,(142,20,20))
	#Same as above... etc etc
	if room02 == True:
		laser(87 * size,display_height - 3 * size,26 * size,2 * size,(215, 123, 186))
		laser(87 * size,display_height - 1 * size,26 * size,1 * size,(154,35,117))
		
		laser(80 * size,16 * size,40 * size,2 * size,(215, 123, 186))
		laser(80 * size,15 * size,40 * size,1 * size,(154,35,117))
		
		laser(0,30 * size,size, 90 * size,(154,35,117))
		laser(size,30 * size,2 * size,90 * size,(215, 123, 186))
		
		laser(display_width - size,30 * size,size, 90 * size,(154,35,117))
		laser(display_width - 3 * size,30 * size,2 * size,90 * size,(215, 123, 186))
	
	if room03 == True:
		laser(0,30 * size,size, 90 * size,(81,89,89))
		laser(size,30 * size,2 * size,90 * size,(125, 142, 142))
		
		laser(display_width - size,30 * size,size, 90 * size,(81,89,89))
		laser(display_width - 3 * size,30 * size,2 * size,90 * size,(125, 142, 142))
	
	if room04 == True:
		laser(80 * size,display_height - 3 * size,40 * size,2 * size,(40, 40, 40))
		laser(80 * size,display_height - 1 * size,40 * size,1 * size,(20,20,20))
		
	if room05 == True:
		laser(0,30 * size,size, 90 * size,(100,100,100))
		laser(size,30 * size,2 * size,90 * size,(255,255,255))
		
		laser(display_width - size,64 * size,size,39 * size,(142,55,55))
		laser(display_width - 3 * size,64 * size,2 * size,39 * size,(119,0,0))	
	
	if room06 == True:
		laser(display_width - size,30 * size,size, 90 * size,(18,0,152))
		laser(display_width - 3 * size,30 * size,2 * size,90 * size,(79,58,255))
	
	if room07 == True:
		laser(0,50 * size,size,50 * size,(100,100,100))
		laser(size,50 * size,2 * size,50 * size,(255,255,255))	
	
	#Shows a door if the player does not have the ability to enter room3
	if door == True:
		if room02 == True:
			Door(3*size,68*size)

	#Shows a bar to keep track of lasereye cooldown
	if lasereyemenu == True:
		laser(40 * size,5 * size,30 * size,5 * size,(255,255,255))
		laser(40 * size,5 * size,mfw,5 * size,mfcolor)
	
	#If the player hits the enemy, an animation of a hit will show
	if weapon == True:
		if hit == True:
			bamn(wx - 4 * size, wy - 4 * size)
		elif hit2 == True:
			bamn(wx2 - 4 * size, wy2 - 4 * size)
	#If the player hits the enemy, an animation of a freeze will show
	if frzz == True:
		frz(lasertipx - 4 * size,lasertipy - 4 * size)
		frz(lasertipx2 - 4 * size,lasertipy2 - 4 * size)
	
	#Shows a series of red squares which acts as hearts
	if hearts >= 4:
		laser(display_width - 40 * size, 5*size, 5*size, 5*size,(255,0,0))
	if hearts >= 3:
		laser(display_width - 30 * size, 5*size, 5*size, 5*size,(255,0,0))
	if hearts >= 2:
		laser(display_width - 20 * size, 5*size, 5*size, 5*size,(255,0,0))
	if hearts >= 1:
		laser(display_width - 10 * size, 5*size, 5*size, 5*size,(255,0,0))
	
		
	#Makes the shield UI bar flash when in use
	if flashtimer == 0:
			mscolor = (160,20,200)
			mscolor2 = (255, 160, 0)
	if flashtimer == 10:
			mscolor = (255,0,255)
			mscolor2 = (255,255,0)
		 
	#increases the size of the orange bar until it fills up
	if shieldtimer <= 3600:
		shieldtimer += 2
	
	#If the shield is used, the bar runs out for 7.5 seconds
	if shieldtimer >= 900:
		shielding = False
		msw = 0
	
	#Increases the shield bar at a certain speed
	if msw < 30 * size:
		msw = ((shieldtimer - 900) / 90) * size
	
	if shielding == True:
		msw = (30 * size) - ((shieldtimer/30) * size)
	
	#Timer to scroll through player sprites to give the illusion of motion
	if walktimer < 40:
		walktimer+=1
	else:
		walktimer= 1
	
	#More things for the shield bar, makes it flash when in use
	if shielding == True:
		if flashtimer < 20:
			flashtimer += 1
		else:
			flashtimer = 0
	else:
		flashtimer = 0
	
	#If the freeze bar runs out, it will slowly fill back up
	if mfw >= .5 * size and nofreeze == False:
		if lasering == True:
			mfw -= .5 * size
		elif lasering == False and mfw < 30 * size:
			mfw += .1 * size
	elif mfw < .5 * size:
		#Turns off laser eyes when the bar runs out
		nofreeze = True
		lasereyes = False
		vlx = 0
		vly = 0
		lw = size
		lh = size
		lasering == False
		if ddown == True:
			vx += speed
		elif adown == True:
			vx -= speed
		elif sdown == True:
			vy += speed
		elif wdown == True:
			vy -= speed
	
	#More of the same from above, changes the bar color when it fills up
	if nofreeze == True:
		mfcolor = (0,50,170)
		mfw += .1 * size
		if mfw > 30 * size - 1:
			nofreeze = False
			lasereyes = True
			mfcolor = (100,100,255)
			if facing == "left":
				ly = ly2 = y + 3 * size
				lx = lx2 = x + 3 * size
			if facing == "up":
				ly = ly2 = y
				lx = x + 4 * size
				lx2 = x + 7 * size
				lasercolor =  (153,229,80)
	
	#Sets ten frams for which a boxing glove is extended at a time	
	if punchtimer < 10:
		punchtimer += 1
	
	#Sets a timer to shift between fire sprites, giving the illusion of
	#an open flame
	firetimer += 1
	if firetimer == 5:
		firetimer = 0
	
	#Gives a game over screen when you run out of hearts
	if hearts == 0:
		print("You Lose!")
		crashed = True
	
	#Timer to change the sprites of the lava and show a flowing river
	if room03 == True and lavatimer <= 34:
		lavatimer += 1
	else:
		lavatimer = 0
		
	frozentimer += 1
	
	#Makes sure that clyde moves only every forth frame
	if clydetimer < 4:
		clydetimer += 1
	else:
		clydetimer = 0
	
	#Makes it so that when you go past the boundary of the wall in one room
	#You then enter the next. Basically, it moves the player to the other 
	#door entrance, and changes the layout of the room, the player does not
	#actually move past the screen in any way
	if y + ph < 15 * size:
		if room1 == True:
			room1 = False
			room02 = True
			y = display_height - ph - 4 * size
			x = 94 * size
			wh = size * 2
			ww = ww2 = size
			wx = x
			wx2 = x + 11 * size
			wy = wy2 = y + 9 * size
			jx = x 
			jy = y + 3 * size
			bx = x + 5 * size
			by = y + 8 * size
			bw = 2 * size
			shieldcolor = (251,242,54)
			bh = size
			lasercolor = (153,229,80)
			lx = x + 4 * size
			ly = y
			lx2 = x + 7 * size
			ly2 = y
	#Same as above, etc etc	
	if room02 == True:
		if y > display_height - 3 * size:
			room1enter = True
			room02 = False
			room1 = True
			if room1enter == True:
				if elw > 0:
					ex = 93 * size
					ey = display_height - 45 * size
					room1enter = False
			y = 19 * size
			x = 94 * size
			facing = "down"
			wh = ww2 = ww = size * 2
			wy = wy2 = y + 9 * size
			wx = x
			wx2 = x + 10 * size
			bx = x + 5 * size
			by = y + 9 * size
			bw = 2 * size
			bh = size
			shieldcolor = (255,160,0)
			jy = y + 4 * size
			jx = x
			lasercolor = (0,0,255)
			lx = x + 4 * size
			ly = y + 3 * size
			lx2 = x + 7 * size
			ly2 = y + 3 * size
		if x + pw < 0:
			room02 = False
			room03 = True
			x = display_width - 16 * size
			y = 74 * size
			ww = ww2 = wh = size * 2
			wx = wx2 = x + size * 4
			wy = wy2 = y + 9 * size
			jx = x + size
			jy = y + 4 * size
			lasercolor = (0,0,255)
			lx = x + 3 * size
			lx2 = x + 3 * size
			ly = y + 3 * size
			ly2 = y + 3 * size
			bx = x + size
			by = y + 9 * size
			bw = size
			bh = size
		if y + ph < 15 * size:
			room02 = False
			room04 = True
			x = 94 * size
			y = display_height - 20 * size
			jx = x 
			jy = y + 3 * size
			bx = x + 5 * size
			by = y + 8 * size
			bw = 2 * size
			wy = wy2 = y + 9 * size
			shieldcolor = (251,242,54)
			bh = size
			lasercolor = (153,229,80)
			lx = x + 4 * size
			ly = y
			lx2 = x + 7 * size
			ly2 = y
		if x > display_width:
			room02 = False
			room05 = True
			x = 3 * size
			y = 74 * size
			jx = x + size
			jy = y + 4 * size
			lasercolor = (0,0,255)
			lx = x + 8 * size
			lx2 = x + 8 * size
			ly = y + 3 * size
			ly2 = y + 3 * size
			bx = x + 10 * size
			by = y + 9 * size
			bw = size
			bh = size
			wh = ww = ww2 = size * 2
			wx = wx2 = x + 6 * size
			wy = wy2 = y + size * 9
			
		
	if room03 == True:
		if x >= display_width:
			room03 = False
			room02 = True
			x = 5 * size
			y = 74 * size
			jx = x + size
			jy = y + 4 * size
			lasercolor = (0,0,255)
			lx = x + 8 * size
			lx2 = x + 8 * size
			ly = y + 3 * size
			ly2 = y + 3 * size
			bx = x + 10 * size
			by = y + 9 * size
			bw = size
			bh = size
			wh = ww = ww2 = size * 2
			wx = wx2 = x + 6 * size
			wy = wy2 = y + size * 9
		if x + pw < 0:
			room03 = False
			room06 = True
			x = display_width - 16 * size
			y = 74 * size
			ww = ww2 = wh = size * 2
			wx = wx2 = x + size * 4
			wy = wy2 = y + 9 * size
			jx = x + size
			jy = y + 4 * size
			lasercolor = (0,0,255)
			lx = x + 3 * size
			lx2 = x + 3 * size
			ly = y + 3 * size
			ly2 = y + 3 * size
			bx = x + size
			by = y + 9 * size
			bw = size
			bh = size
			
	if room04 == True:
		if y > display_height:
			room04 = False
			room02 = True
			y = 19 * size
			x = 94 * size
			facing = "down"
			wh = ww2 = ww = size * 2
			wy = wy2 = y + 9 * size
			wx = x
			wx2 = x + 10 * size
			bx = x + 5 * size
			by = y + 9 * size
			bw = 2 * size
			bh = size
			shieldcolor = (255,160,0)
			jy = y + 4 * size
			jx = x
			lasercolor = (0,0,255)
			lx = x + 4 * size
			ly = y + 3 * size
			lx2 = x + 7 * size
			ly2 = y + 3 * size
	
	if room05 == True:
		if x + pw < 0:
			room05 = False
			room02 = True
			x = display_width - 16 * size
			y = 74 * size
			ww = ww2 = wh = size * 2
			wx = wx2 = x + size * 4
			wy = wy2 = y + 9 * size
			jx = x + size
			jy = y + 4 * size
			lasercolor = (0,0,255)
			lx = x + 3 * size
			lx2 = x + 3 * size
			ly = y + 3 * size
			ly2 = y + 3 * size
			bx = x + size
			by = y + 9 * size
			bw = size
			bh = size
			
		if x >= display_width:
			room05 = False
			room07 = True
			x = 5 * size
			y = 74 * size
			jx = x + size
			jy = y + 4 * size
			lasercolor = (0,0,255)
			lx = x + 8 * size
			lx2 = x + 8 * size
			ly = y + 3 * size
			ly2 = y + 3 * size
			bx = x + 10 * size
			by = y + 9 * size
			bw = size
			bh = size
			wh = ww = ww2 = size * 2
			wx = wx2 = x + 6 * size
			wy = wy2 = y + size * 9
			
	if room06 == True:
		if x >= display_width:
			room06 = False
			room03 = True
			x = 5 * size
			y = 74 * size
			jx = x + size
			jy = y + 4 * size
			lasercolor = (0,0,255)
			lx = x + 8 * size
			lx2 = x + 8 * size
			ly = y + 3 * size
			ly2 = y + 3 * size
			bx = x + 10 * size
			by = y + 9 * size
			bw = size
			bh = size
			wh = ww = ww2 = size * 2
			wx = wx2 = x + 6 * size
			wy = wy2 = y + size * 9
			
	if room07 == True:
		if x + pw < 0:
			room07 = False
			room05 = True
			x = display_width - 16 * size
			y = 74 * size
			ww = ww2 = wh = size * 2
			wx = wx2 = x + size * 4
			wy = wy2 = y + 9 * size
			jx = x + size
			jy = y + 4 * size
			lasercolor = (0,0,255)
			lx = x + 3 * size
			lx2 = x + 3 * size
			ly = y + 3 * size
			ly2 = y + 3 * size
			bx = x + size
			by = y + 9 * size
			bw = size
			bh = size
		
	#Controls the player so that he cannot exceed a fixed speed(one pixel per frame)
	if vx > size:
		vx = size
	elif vy > size:
		vy = size
	if vx < -size:
		vx = -size
	elif vy < -size:
		vy = -size
	
	#opens the door in room 2 when clyde dies
	if elw <= .5 and clydedeath == False:
		door = False
		clydedeath = True
	
	#Checks to see if the tip of the freeze laser hits the fireplace in
	#room 5
	if room05 == True:
		if lasertipx > display_width - 16 * size:
			fireplace = False

	pygame.display.update()
	clock.tick(tickspeed)

pygame.quit()
quit()

#Sources:
#https://pythonprogramming.net/pygame-python-3-part-1-intro/
#http://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
#I mostly figured everything out from the first source, and used the second
#source for one specific purpose

#Here are some images from which I recieved HEAVY influence
#https://vignette1.wikia.nocookie.net/pacman/images/b/be/2469743-orange.png/revision/latest/scale-to-width-down/185?cb=20160120210434
#https://upload.wikimedia.org/wikipedia/en/b/b2/It%27s_dangerous_to_go_alone%21_Take_this..png
