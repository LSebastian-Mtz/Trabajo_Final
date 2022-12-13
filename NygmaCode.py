import pygame
import sys
import random

#Window
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

pygame.mixer.music.load("CancionMenu.mp3")
pygame.mixer.music.play(-1)

credit = pygame.image.load("Creditos.jpg")
credit = pygame.transform.scale(credit, (800, 600))
screen.blit(credit, (0, 0))
pygame.display.update()
pygame.time.delay(2000)

backg = pygame.image.load("MENU.jpg")
backg = pygame.transform.scale(backg, (800, 600))
pygame.display.set_caption("NYGMA CODE")

main_font = pygame.font.SysFont("OCR A Extended", 45)
game_font = pygame.font.SysFont("OCR A Extended", 100)

#Colors
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

#Buttons
class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "#E6FF00FF")
		else:
			self.text = main_font.render(self.text_input, True, "white")

#Start Game
def start():
	pygame.display.update()
	#Bomb Image
	Img_tnt = []
	bomb_status = 0
	for i in range(6):
		image = pygame.image.load(f"xBomb{i}.png")
		image = pygame.transform.scale(image, (600, 200))
		Img_tnt.append(image)

	#Boxes-Letters
	Rows = 2
	Cols = 13
	Gap = 10
	Size = 50
	Boxes = []

	for row in range(Rows):
		for col in range(Cols):
			x = (((col * Gap) + Gap) + (Size * col)) + 5
			y = (((row * Gap) + Gap) + (Size * row)) + 410
			box = pygame.Rect(x, y, Size, Size)
			Boxes.append(box)

	#Buttons w/Letters
	BtnLetter = []
	A = 65

	for ind, box in enumerate(Boxes):
		letter = chr(A+ind)
		button = [box, letter]
		BtnLetter.append(button)

	#WORD
	WORDS= ["BE", "CHOOSE", "DRINK", "EAT", "FIGHT", "GROW", "HAVE", "KNOW", "LOSE", "MAKE", "PAY", "SEE", "WIN"]
	WORD = random.choice(WORDS)
	#WORD = "SUS"
	GUESSED = []

	while True:
		GameOver = False
		Mouse_pos = pygame.mouse.get_pos()
		#Title
		Title = "Level 1"
		Title_text = main_font.render(Title, True, BLACK)
		Title_rect = Title_text.get_rect(center=(WIDTH//2, Title_text.get_height()//2 + 10))

		#BackGround
		backg = pygame.image.load("escenariox1.png")
		backg = pygame.transform.scale(backg, (800, 600))
		screen.blit(backg, (0, 0))

		#Button
		button_surface = pygame.image.load("Arrowx2.png")
		button_surface = pygame.transform.scale(button_surface, (100, 70))
		btnBack = Button(button_surface, 80, 65, "BACK")

		btnBack.changeColor(Mouse_pos)
		btnBack.update()

		#General
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if btnBack.checkForInput(Mouse_pos):
					menu()
				click_pos = event.pos
				for button, letter in BtnLetter:
					if button.collidepoint(click_pos):
						if letter not in WORD:
							bomb_status += 1

						if bomb_status == 5:
							GameOver = True

						GUESSED.append(letter)

						BtnLetter.remove([button, letter])

		screen.blit(Img_tnt[bomb_status], (110, 100))
		screen.blit(Title_text, Title_rect)

		#Generate Boxes
		for box in Boxes:
			pygame.draw.rect(screen, BLACK, box, 100)

		#Generate Boxes w/ Letters
		for box, letter in BtnLetter:
			btnText = main_font.render(letter, True, WHITE)
			btn_rect = btnText.get_rect(center=(box.x + 25, box.y + 22))
			screen.blit(btnText, btn_rect)
			pygame.draw.rect(screen, BLACK, box, 1)

		display_text = " "

		for letter in WORD:
			if letter in GUESSED:
				display_text += f"{letter}"
			else:
				display_text += "_ "

		text = game_font.render(display_text, True, WHITE)
		screen.blit(text, (90, 280))

		pygame.display.update()

		won = True

		for letter in WORD:
			if letter not in GUESSED:
				won = False

		if won:
			GameOver = True
			GameOver_msg = "You Won"
			img = pygame.image.load("YWin.png")
		else:
			GameOver_msg = "You Lost"
			img = pygame.image.load("YLose.png")

		if GameOver:
			pygame.time.delay(3000)
			img = pygame.transform.scale(img, (800, 600))
			screen.blit(img, (0, 0))
			pygame.display.update()
			pygame.time.delay(3000)
			menu()

#Instructions
def Ins():
	pygame.display.update()
	while True:
		Mouse_pos = pygame.mouse.get_pos()

		backg = pygame.image.load("Instructions.png")
		backg = pygame.transform.scale(backg, (800, 600))
		screen.blit(backg, (0, 0))

		button_surface = pygame.image.load("Arrowx2.png")
		button_surface = pygame.transform.scale(button_surface, (100, 70))
		btnBack = Button(button_surface, 112, 137, "BACK")

		button_surface = pygame.image.load("Bat(ck)x2.png")
		button_surface = pygame.transform.scale(button_surface, (155, 70))
		btnStart = Button(button_surface, 355, 500, "START")

		btnBack.changeColor(Mouse_pos)
		btnBack.update()

		btnStart.changeColor(Mouse_pos)
		btnStart.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if btnBack.checkForInput(Mouse_pos):
					menu()
				if btnStart.checkForInput(Mouse_pos):
					start()

		pygame.display.update()

#Buttons f/Menu
#Button Start
surface = pygame.image.load("BUTTON1.png")
surface = pygame.transform.scale(surface, (350, 80))
btnStart = Button(surface, 250, 300, "PLAY")
#Button Instructions
surface = pygame.image.load("BUTTON2.png")
surface = pygame.transform.scale(surface, (350, 80))
btnIns = Button(surface, 250, 400, "INSTRUCTIONS")
#Button Exit
surface = pygame.image.load("BUTTON3.png")
surface = pygame.transform.scale(surface, (350, 80))
btnExit = Button(surface, 250, 500, "EXIT")

#Main Menu
def menu():
	while True:
		screen.blit(backg, (0, 0))
		Mouse_pos = pygame.mouse.get_pos()

		for button in [btnStart, btnIns, btnExit]:
			button.changeColor(Mouse_pos)
			button.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if btnStart.checkForInput(Mouse_pos):
					start()
				if btnIns.checkForInput(Mouse_pos):
					Ins()
				if btnExit.checkForInput(Mouse_pos):
					pygame.quit()
					sys.exit()

		pygame.display.update()

menu()
