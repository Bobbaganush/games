import pygame
from player import *
from player_setup import *
import random


pygame.init()



display_width = 1200
display_height = 800

game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption('ACHTUNG DIE KURVE - Virre edition')



def text_objects(text, font):
    text_surface = font.render(text, True, red)
    return text_surface, text_surface.get_rect()

def message_display(text, x, y):
    display_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, display_text)
    text_rect.center = ((x, y))
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)




def game_loop(player_group):
    filled_locations = []
    dead_players = 0
    num_players = len(player_group)
    active_players = player_group
    frames = 0
    silence = False
    while len(active_players) > 1:
        frames += 1
        for player_name, active_player in active_players.items():
            print active_player
            if silence == False:
                if frames % 100 == 0:
                    silence = True
                    silence_turns = 10

                active_player.get_passed_pixels()
                intersections = [i for i in active_player.passed_pixels if i in filled_locations]

                if len(intersections) > 0:
                     active_player.alive = False
                     pygame.draw.circle(game_display,  active_player.color,  intersections[0], 3)
                     active_player.victory_points = num_players - len(active_players)
                     del active_players[player_name]
                else:
                     pygame.draw.circle(game_display,  active_player.color,  active_player.pos, 3)

                if active_player.x > display_width or active_player.x < 0 or active_player.y > display_height or active_player.y < 0:
                    active_player.alive = False
                    active_player.victory_points = num_players - len(active_players)
                    del active_players[player_name]


                filled_locations = filled_locations + active_player.passed_pixels
            else:
                silence_turns -= 1
                if silence_turns == 0:
                    silence = False


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            if keys[active_player.left_button]:
               active_player.left = True
            if keys[active_player.right_button]:
               active_player.right = True


            active_player.move(active_player.left,active_player.right)



        pygame.display.update()

        clock.tick(20)
    game_intro()

def game_intro():
    num_players = 3
    game_display.fill(BLACK)
    player_group = {str(i): player(player_setup[i][0], player_setup[i][1],
                random.randrange(0,display_width), random.randrange(0,display_height),
                player_setup[i][2]) for i in range(0,num_players)}
    for key, active_player in player_group.iteritems():
        pygame.draw.circle(game_display,  active_player.color,  active_player.pos, 3)
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop(player_group)
game_intro()
