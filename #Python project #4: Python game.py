#Python project #4: Python game

import pygame
import time 
import random 

#Pygame intialization
pygame.init

#Define colors
white = (225, 225, 225)
yellow = (225, 225, 102)
black = (0,0,0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#window dimensions
width = 600
height = 400
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game!")

#Clock for the speed of the game
clock = pygame.time.Clock()

#Size of snake and speed
snake_block = 10
snake_speed = 15

#Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def snake_chr(snake_block, snake_lists):
    for x in snake_lists:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_block, snake_block])

def player_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    game_window.blit(value,[0,0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width/6, height/3])

#Game Loop
def gameLoop(): 
    game_over = False 
    game_close = False 

    x1 = width / 2
    y1 = height / 2 

    x1_change = 0
    y1_change = 0 

    snake_Lists = []
    Length_of_snake = 1

    #1st Apple
    apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    apple_y = round(random.rangerange(0, height - snake_block) / 10.0) * 10.0
#Game over screen
    while not game_over:

        while game_close: 
            game_window.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            player_score(Length_of_snake-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_over = False 
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                game_over = True 
            if event.type == pygame.KEYDOWN:
                x1_change = -snake_block
                y1_change = 0 
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0 
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0 
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
        
        #check boundaries
        if x1 >= width or  x1 < 0 or y1 >= height or y1 < 0:
            game_close = True 

        x1 += x1_change
        y1 += y1_change
        game_window.fill(blue)
        pygame.draw.rect(game_window, green, [apple_x, apple_y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_Lists.append(snake_Head) #New head is added to the snakes body
        if len(snake_Lists) > Length_of_snake:
            del snake_Lists[0]

    # Check for collision with self
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)  # Draw the snake
        your_score(Length_of_snake - 1)  # Show the score

        pygame.display.update()

        # Check if the snake has eaten the apple
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()  # Quit Pygame
    quit()  # Quit the program


# Run the game
gameLoop()        
                

    