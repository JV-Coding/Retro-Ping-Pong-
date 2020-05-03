# This is my ping pong game #


import time


# This positions the window in the middle of the screen
# This also imports pygame
import pygame, os 
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Clock for the fps of the game
clock = pygame.time.Clock()

# Window of the game
game_window = pygame.display.set_mode((1000, 800))

# Title of the window
pygame.display.set_caption("Retro Ping Pong")


# This initialises pygame
pygame.init()

# import the button function #
import button_function

##################################################################################################
end = False

def intro():

	# background music 
	pygame.mixer.music.load('Stranger_Danger.mp3')
	pygame.mixer.music.set_volume(0.3)
	pygame.mixer.music.play(-1)

	# Title Text #
	title_font = pygame.font.SysFont("comicsans", 110, True)
	TITLE_text = title_font.render("RETRO PING PONG", 1, (255, 255, 255))

	# message
	message_font = pygame.font.SysFont("comicsans", 50)
	message = message_font.render("A classic two player game!", 1, (255, 255, 255))


	def draw_to_window():

		play_btn = button_function.button(game_window, "PLAY RETRO PONG", 310, 350, 400, 100, (100, 100, 100), (250, 250, 250), main_gameloop)

		game_window.blit(TITLE_text, (90, 90))
		game_window.blit(message, (285, 210))
		pygame.display.update()



	intro = True
	# Event handling
	while intro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		draw_to_window()



#######################################################################################


# Pausing function during the gameplay #
pause = False

def unpause_game():
	global pause
	pygame.mixer.music.unpause()
	pause = False


def paused():
	global pause
	pause = True
	# music stops
	pygame.mixer.music.pause()

	# Paused Text #
	font = pygame.font.SysFont("comicsans", 80, True)
	pause_text = font.render("Retro Ping Pong Paused", 1, (255, 255, 255))

	# FPS
	clock.tick(30)


	# Drawing to the window #
	def draw_to_window():

		# fill background #
		game_window.fill((0, 0, 0))

		# title #
		game_window.blit(pause_text, (110, 100))

		# Pause Buttons #
		unpause_btn = button_function.button(game_window, "Continue Ping Pong!", 300, 200, 400, 100, (100, 100, 100), (250, 250, 250), unpause_game)
		restart_btn = button_function.button(game_window, "Restart Game", 300, 350, 400, 100, (100, 100, 100), (250, 250, 250), main_gameloop)
		quit_btn = button_function.button(game_window, "Quit Game", 300, 500, 400, 100, (100, 100, 100), (250, 250, 250),quit_game)
		

	# Event handling
	while pause:

		draw_to_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()




##################################################################################################

def quit_game():
	pygame.quit()
	quit()



def end_game_1():
	global end 

	# stopping the music
	pygame.mixer.music.pause()

	# end game title
	title_font = pygame.font.SysFont("comicsans", 110, True)
	TITLE_text = title_font.render("PLAYER 1 WON!!!", 1, (255, 255, 255))

	def draw_to_window():


		game_window.blit(TITLE_text, (120, 100))

		replay_btn = button_function.button(game_window, "REPLAY RETRO PONG", 310, 350, 400, 100, (100, 100, 100), (250, 250, 250), main_gameloop)
		return_btn = button_function.button(game_window, "RETURN TO MENU", 310, 550, 400, 100, (100, 100, 100), (250, 250, 250), quit_game)

		pygame.display.update()

	end = True
	# Event handling
	while end:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		draw_to_window()

	pygame.quit()




def end_game_2():
	global end 

	# stopping the music
	pygame.mixer.music.pause()

	# end game title
	title_font = pygame.font.SysFont("comicsans", 110, True)
	TITLE_text = title_font.render("PLAYER 2 WON!!!", 1, (255, 255, 255))

	def draw_to_window():


		game_window.blit(TITLE_text, (120, 100))

		replay_btn = button_function.button(game_window, "REPLAY RETRO PONG", 310, 350, 400, 100, (100, 100, 100), (250, 250, 250), main_gameloop)
		return_btn = button_function.button(game_window, "QUIT GAME", 310, 550, 400, 100, (100, 100, 100), (250, 250, 250), quit_game)

		pygame.display.update()

	end = True
	# Event handling
	while end:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		draw_to_window()

	pygame.quit()

##################################################################################################

def main_gameloop():

	time.sleep(1)

	# background music 
	pygame.mixer.music.load('Stranger_Danger.mp3')
	pygame.mixer.music.set_volume(0.3)
	pygame.mixer.music.play(-1)

	# sound effect 
	hit = pygame.mixer.Sound('Beep_Short.wav')
	hit.set_volume(0.4)
	
	# Defining some colours for the graphics and background
	background_colour = (0, 0, 0)
	paddle1_colour = (255, 255, 255)
	paddle2_colour = (255, 255, 255)
	ball_colour = (255, 255, 255)
	net_colour = (255, 255, 255)

	# Scores for the players
	player1_score = 0
	player2_score = 0

	font = pygame.font.Font('freesansbold.ttf', 60)

	TextX_1 = 700
	TestY_1 = 725

	TextX_2 = 230
	TextY_2 = 725

	TextX_3 = 400
	TextY_3 = 725

	def show_score1(x, y):
		score_1 = font.render(str(player1_score), True, (255, 255, 255))
		game_window.blit(score_1, (x, y))

	def show_score2(x, y):
		score_2 = font.render(str(player2_score), True, (255, 255, 255))
		game_window.blit(score_2, (x, y))

	def show_score_label(x, y):
		score_label = font.render("Score", True, (255, 255, 255))
		game_window.blit(score_label, (x, y))


	#Player 1 coordinates
	start_x = 920
	start_y = 250
	y_change = 0

	#Player2 coordinates
	start_x2 = 55
	start_y2 = 250
	y2_change = 0

	#Ball starting coordinates
	start_x3 = 500
	start_y3 = 350
	dx = 8
	dy = 8

	#Defining a loop
	game = True

	# Main Game loop
	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False

			# These are the movements for the paddle for player 1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					y_change = 11.5
				if event.key == pygame.K_RIGHT:
					y_change = -11.5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					y_change = 0
				if event.key == pygame.K_RIGHT:
					y_change = 0

			# These are the movements for the paddle for player 2
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:
					y2_change = -11.5
				if event.key == pygame.K_a:
					y2_change = 11.5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_d:
					y2_change = 0
				if event.key == pygame.K_a:
					y2_change = 0

			# PAUSE EVENT 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					paused()

		# This button starts the ball's movements
		start_x3 += dx
		start_y3 += dy

		# If the ball hits either sides of width
		if start_x3 < 0 + 20:
			start_x = 920
			start_y = 650

			start_x3 = 500
			start_y3 = 350

			dx = -10
			dy = 10

			dx *= -1

			player1_score += 1

			time.sleep(1)

		if start_x3 > 1000-20:
			start_x2 = 55
			start_y2 = 650

			start_x3 = 500
			start_y3 = 350
			
			dx = 10
			dy = 10

			dx *= -1

			player2_score += 1

			time.sleep(1)

		# If ball hits either sides of height
		if start_y3 < 0 + 40 or start_y3 > 700-40:
			dy *= -1
			hit.play(0)

		# If ball hits player 1 paddle
		if (start_x3 > start_x - 26 and start_x3 < start_x) and (start_y3 < start_y + 150 and start_y3 > start_y):
			dx *= -1
			dy *= 1
			dx -= 1
			dy += 0
			hit.play(0)

		

		# If ball hits player 2 paddle
		if (start_x3 < start_x2 + 50 and start_x3 > start_x2) and (start_y3 < start_y2 + 150 and start_y3 > start_y2):
			dx *= -1
			dy *= 1
			dx += 1
			dy += 0
			hit.play(0)
		
		
		# change in position for paddle 1 + boundries
		start_y += y_change

		if start_y < 0:
			start_y = 0
		elif start_y > 550:
			start_y = 550

		# change in position for paddle 2 + boundries
		start_y2 += y2_change

		if start_y2 < 0:
			start_y2 = 0
		elif start_y2 > 550:
			start_y2 = 550

		# If either of the players score 4 points
		if player1_score == 4:

			dx = 0
			dy = 0

			y_change = 0
			start_y = 250

			y2_change = 0
			start_y2 = 250

			end_game_1()

		if player2_score == 4:
			dx = 0
			dy = 0

			y_change = 0
			start_y = 250

			y2_change = 0
			start_y2 = 250

			end_game_2()


		# putting a limit onto the ball speed #
		if dx == 25:
				dx = 24
		elif dx == -25:
			dx = -24


		game_window.fill(background_colour)


		# Show the score for player 1
		show_score1(TextX_1, TestY_1)

		# Show the score for player 2
		show_score2(TextX_2, TextY_2)

		# show score label 
		show_score_label(TextX_3, TextY_3)

		#Paddle 1
		pygame.draw.rect(game_window, paddle1_colour, [start_x, start_y, 30, 150])

		#Paddle 2
		pygame.draw.rect(game_window, paddle2_colour, [start_x2, start_y2, 30, 150])

		#Ball
		pygame.draw.circle(game_window, ball_colour, (start_x3, start_y3), 15)

		# Net (I had to draw each individual square. Each gap is 15 pixels)
		pygame.draw.rect(game_window, net_colour, [490, 10, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 25, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 40, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 55, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 70, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 85, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 100, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 115, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 130, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 145, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 160, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 175, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 190, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 205, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 220, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 235, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 250, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 265, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 280, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 295, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 310, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 325, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 340, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 355, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 370, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 385, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 400, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 415, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 430, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 445, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 460, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 475, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 490, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 505, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 520, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 535, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 550, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 565, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 580, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 595, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 610, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 625, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 640, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 655, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 670, 10, 10])
		pygame.draw.rect(game_window, net_colour, [490, 685, 10, 10])

		#borders of the game
		pygame.draw.rect(game_window, (255, 255, 255), [0, 0, 1000, 10])
		pygame.draw.rect(game_window, (255, 255, 255), [0, 0, 10, 700])
		pygame.draw.rect(game_window, (255, 255, 255), [0, 690, 1000, 10])
		pygame.draw.rect(game_window, (255, 255, 255), [990, 0, 10, 700])
		
		# This updates the display of the game
		pygame.display.update()

		#FPS
		clock.tick(30)

	# This is to quit the game
	pygame.quit()


intro()





