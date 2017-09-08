import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARK_CYAN = (9,143,136)
GOLD = (237,222,14)

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

SCREEN = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

# Snake Parameters
SNAKE_RECT_SIZE = 10
SNAKE_X_HEAD_START = DISPLAY_WIDTH / 2
SNAKE_Y_HEAD_START = DISPLAY_HEIGHT / 2 
BORDER_WIDTH = 10
# Snake Parameters


pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

# Functions
def snake_head(snake_head_x,snake_head_y):
    pygame.draw.rect(SCREEN,WHITE,[snake_head_x,snake_head_y,SNAKE_RECT_SIZE,SNAKE_RECT_SIZE],0)

def food(food_x,food_y):
    pygame.draw.circle(SCREEN,DARK_CYAN,(food_x,food_y),2)

def borders():
    pygame.draw.line(SCREEN,GOLD,[0,0],[0,DISPLAY_HEIGHT],BORDER_WIDTH)
    pygame.draw.line(SCREEN,GOLD,[DISPLAY_WIDTH - 3, 0],[DISPLAY_WIDTH - 3,DISPLAY_HEIGHT],BORDER_WIDTH)
    pygame.draw.line(SCREEN,GOLD,[0,0],[DISPLAY_WIDTH,0],BORDER_WIDTH)
    pygame.draw.line(SCREEN,GOLD,[0,DISPLAY_HEIGHT],[DISPLAY_WIDTH - 3,DISPLAY_HEIGHT],BORDER_WIDTH)

def game_loop():
    # Contadores de colisiones
    cont = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    eaten_food_s = 0
    eaten_food_c = 0
    # Contadores de colisiones

    snake_body_blobs = 0
    snake_up_movement = True
    snake_down_movement = False
    snake_left_movement = False
    snake_right_movement = False
    snake_head_x = SNAKE_X_HEAD_START
    snake_head_y = SNAKE_Y_HEAD_START
    snake_speed = 1
    food_x = random.randrange(16,DISPLAY_WIDTH - 16)
    food_y = random.randrange(16,DISPLAY_HEIGHT - 16)

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake_left_movement == False:
                    snake_up_movement = False
                    snake_down_movement = False
                    snake_left_movement = False
                    snake_right_movement = True
                elif event.key == pygame.K_LEFT and snake_right_movement == False:
                    snake_up_movement = False
                    snake_down_movement = False
                    snake_left_movement = True
                    snake_right_movement = False
                elif event.key == pygame.K_DOWN and snake_up_movement == False:
                    snake_up_movement = False
                    snake_down_movement = True
                    snake_left_movement = False
                    snake_right_movement = False
                elif event.key == pygame.K_UP and snake_down_movement == False:
                    snake_up_movement = True
                    snake_down_movement = False
                    snake_left_movement = False
                    snake_right_movement = False
            # Controls     

        # Spawns a new blob of food if the snake has eaten the one already there
        if eaten_food_s > eaten_food_c:
            food_x = random.randrange(16,DISPLAY_WIDTH - 16)
            food_y = random.randrange(16,DISPLAY_HEIGHT - 16)
            eaten_food_c = eaten_food_s   
            snake_body_blobs += 1
            print 'food blobs eaten: ', eaten_food_c

        
            
        SCREEN.fill(BLACK)

        # Drawing
        borders()
        food(food_x,food_y)
        snake_head(snake_head_x,snake_head_y)
        if snake_up_movement == True:
            for a in range(SNAKE_RECT_SIZE):
                if (snake_head_x + a == food_x and snake_head_y == food_y):
                    # Describes the type of collision it happened and how many times that side has registered a collision
                    cont += 1
                    print 'frontal_collision ' + str(cont)
                    # Describes the type of collision it happened and how many times that side has registered a collision
                    eaten_food_s +=1
                    break
            snake_head_y += snake_speed * -1

        elif snake_down_movement == True:
            for b in range(SNAKE_RECT_SIZE):
                if (snake_head_x + b == food_x and snake_head_y + SNAKE_RECT_SIZE == food_y):
                    # Describes the type of collision it happened and how many times that side has registered a collision
                    cont2 += 1
                    print 'rear_collision ' + str(cont2)
                    # Describes the type of collision it happened and how many times that side has registered a collision
                    eaten_food_s += 1
                    break
            snake_head_y += snake_speed

        elif snake_left_movement == True:
            for c in range(SNAKE_RECT_SIZE):
                if(snake_head_x == food_x and snake_head_y + c == food_y):
                    # Describes the type of collision it happened and how many times that side has registered a collision
                    cont3 += 1
                    print 'left_side_collision ' + str(cont3)
                    # Describes the type of collision it happened and how many times that side has registered a collision
                    eaten_food_s += 1
                    break
            snake_head_x += snake_speed * -1

        elif snake_right_movement == True:
            for d in range(SNAKE_RECT_SIZE):
                if (snake_head_x + SNAKE_RECT_SIZE == food_x and snake_head_y + d == food_y):
                    # Describes the type of collision it happened and how many times that side has registered a collision
                    cont4 += 1
                    print 'right_side_collision ' + str(cont4)
                    # Describes the type of collision it happened and how many times that side has registered a collision
                    eaten_food_s += 1
                    break
            snake_head_x += snake_speed
        # Drawing

        pygame.display.update()
        clock.tick(150)

# Main
game_loop()

pygame.quit()
quit()