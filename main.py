import pygame
from player import *
from player_setup import *
import random


pygame.init()



display_width = 1000
display_height = 800

game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption('ACHTUNG DIE KURVE - Virre edition')

num_players = 2



player_group = {str(i): player(player_setup[i][0], player_setup[i][1],
            3, 2, player_setup[i][2]) for i in range(0,num_players - 1)}

print player_group

player_1 = player(player_setup[0][0], player_setup[0][1], 3, 2, player_setup[0][2])
player_2 = player(player_setup[1][0], player_setup[1][1], 3, 2, player_setup[1][2])



def game_loop():
    filled_locations = []


    frames = 0
    while player_1.alive and player_2.alive:

        frames +=1

        player_1.get_passed_pixels()
        player_2.get_passed_pixels()

        intersections_p1 = [i for i in player_1.passed_pixels if i in filled_locations]
        intersections_p2 = [i for i in player_2.passed_pixels if i in filled_locations]

        pygame.draw.circle(game_display, player_1.color, player_1.pos, 4)
        pygame.draw.circle(game_display, player_2.color, player_2.pos, 4)

        if len(intersections_p1) > 0:
            player_1.alive = False
        if len(intersections_p2) > 0:
            player_2.alive = False

        filled_locations = filled_locations + player_1.passed_pixels + player_2.passed_pixels

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[player_1.left_button]:
           player_1.left = True
        if keys[player_1.right_button]:
           player_1.right = True

        if keys[player_2.left_button]:
           player_2.left = True
        if keys[player_2.right_button]:
           player_2.right = True

        player_1.move(player_1.left,player_1.right)
        player_2.move(player_2.left,player_2.right)

        #pygame.draw.circle(game_display, player_1.color, player_1.pos, 4)
        #pygame.draw.circle(game_display, player_2.color, player_2.pos, 4)


        pygame.display.update()

        clock.tick(20)
game_loop()
