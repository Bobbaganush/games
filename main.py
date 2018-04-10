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

class game:
    def __init__(self, num_players):
        self.num_players = num_players

    def text_objects(text, font):
        text_surface = font.render(text, True, red)
        return text_surface, text_surface.get_rect()

    def message_display(text, x, y, size = 15):
        display_text = pygame.font.Font('freesansbold.ttf', size)
        text_surf, text_rect = text_objects(text, display_text)
        text_rect.center = ((x, y))
        game_display.blit(text_surf, text_rect)
        pygame.display.update()
        time.sleep(2)

    def create_score_board(self):
        text_size = 25
        x = 70
        y = 100
        font = pygame.font.SysFont(None, text_size)
        for active_player in self.player_group.values():
            score = font.render(active_player.name + ': ' + str(active_player.victory_points),
                True, YELLOW)
            game_display.blit(score, (x,y))
            y += text_size + 25

    def game_loop(self):
        game_display.fill(BLACK)
        filled_locations = []
        dead_players = 0
        active_players = self.player_group.copy()
        frames = 0
        silence = False
        while len(active_players) > 1:
            frames += 1
            for player_name, active_player in active_players.items():
                if silence == False:
                    if frames % 100 == 0:
                        silence = True
                        silence_turns = 10

                    active_player.get_passed_pixels()
                    intersections = [i for i in active_player.passed_pixels if i in filled_locations]

                    if len(intersections) > 0:
                         active_player.alive = False
                         pygame.draw.circle(game_display,  active_player.color,  intersections[0], 3)
                         active_player.victory_points += self.num_players - len(active_players)
                         del active_players[player_name]
                    else:
                         pygame.draw.circle(game_display,  active_player.color,  active_player.pos, 3)

                    if active_player.x > display_width or active_player.x < 0 or active_player.y > display_height or active_player.y < 0:
                        active_player.alive = False
                        active_player.victory_points += self.num_players - len(active_players)
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
        active_players.values()[0].victory_points += self.num_players - 1
        self.game_intro()

    def create_players(self):
        self.player_group = {str(i): player( 'Player ' + str(i),player_setup[i][0], player_setup[i][1],
                display_width, display_height, player_setup[i][2]) for i in range(0,self.num_players)}


    def game_intro(self):
        game_display.fill(BLACK)
        self.create_score_board()

        for player_name, active_player in self.player_group.items():
            print active_player.name
            active_player.restart()
            active_player.alive = True
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
                        self.game_loop()
achtung = game(2)
achtung.create_players()
achtung.game_intro()
