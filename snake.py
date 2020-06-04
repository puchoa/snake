import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game Size
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Mine By Paulo Uchoa')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 35)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 7, dis_height / 2])


# Return a random int based on the side
def change_location(side):
    if side == "width":
        return round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    return round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = change_location("width")
    foody = change_location("height")

    bomb = []

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        for i in range(len(bomb)):
            pygame.draw.rect(dis, red, [bomb[i][0], bomb[i][1], snake_block, snake_block])


        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # If snake eats the food
        if x1 == foodx and y1 == foody:
            # Change location of the food
            foodx = change_location("width")
            foody = change_location("height")

            # Increase the snake length
            Length_of_snake += 1

            # Change location for the bombs
            for i in range(len(bomb)):
                bombx = change_location("width")
                bomby = change_location("height")

                # For bomb to not be in the same location as the food
                while bombx == foodx and bomby == foody:
                    bombx = change_location("width")
                    bomby = change_location("height")

                # Set bombs to their new location
                bomb[i][0] = bombx
                bomb[i][1] = bomby

            # Create new bomb
            bombx = change_location("width")
            bomby = change_location("height")

            # For new bomb to not be in the same location as the food
            while bombx == foodx and bomby == foody:
                bombx = change_location("width")
                bomby = change_location("height")

            # Add new bomb
            bomb.append([bombx, bomby])


        # If snake eats the bomb
        for i in range(len(bomb)):
            if x1 == bomb[i][0] and y1 == bomb[i][1]:
                game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()