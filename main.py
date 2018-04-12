import pygame
from player import *
from player_setup import *
import random
import time


pygame.init()



display_width = 1200
display_height = 800

game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption('ACHTUNG DIE KURVE - Virre edition')

class game:
    def __init__(self, display_width, display_height, win_points):
        self.num_players = 2
        self.display_width = display_width
        self.display_height = display_height
        self.win_points = win_points
        self.game_over = False
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))

    def text_objects(self,text, font):
        text_surface = font.render(text, True, RED)
        return text_surface, text_surface.get_rect()

    def message_display(self,text, x, y, size = 15):
        display_text = pygame.font.Font('freesansbold.ttf', size)
        text_surf, text_rect = self.text_objects(text, display_text)
        text_rect.center = ((x, y))
        self.game_display.blit(text_surf, text_rect)
        pygame.display.update()

    def blit_img(self,img_path, center_x_y, size):
        img_temp = pygame.image.load(img_path)
        img = pygame.transform.scale(img_temp, size)
        img_rect = img.get_rect()
        img_rect.center = (center_x_y)
        self.game_display.blit(img, img_rect)

    def check_for_victory(self):
        for active_player in self.player_group.values():
            if active_player.victory_points >= self.win_points:
                self.game_over = True

    def create_score_board(self):
        text_size = 25
        x = 70
        y = 100
        font = pygame.font.SysFont(None, text_size)
        for active_player in self.player_group.values():
            score = font.render(active_player.name + ': ' + str(active_player.victory_points),
                True, active_player.color)
            self.game_display.blit(score, (x,y))
            y += text_size + 25

    def game_loop(self):
        self.game_display.fill(BLACK)
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
                         pygame.draw.circle(self.game_display,  active_player.color,  intersections[0], 3)
                         active_player.victory_points += self.num_players - len(active_players)
                         del active_players[player_name]
                    else:
                         pygame.draw.circle(self.game_display,  active_player.color,  active_player.pos, 3)

                    if active_player.x > self.display_width or active_player.x < 0 or active_player.y > self.display_height or active_player.y < 0:
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
        self.check_for_victory()
        self.game_intro()

    def create_players(self):
        self.player_group = {str(i): player( 'Player ' + str(i),player_setup[i][0], player_setup[i][1],
                self.display_width, self.display_height, player_setup[i][2]) for i in range(1,self.num_players + 1)}


    def game_intro(self):
        self.game_display.fill(BLACK)
        self.create_score_board()
        if self.game_over == True:
            self.message_display('GAME OVER', self.display_width/2, int(round(self.display_height/2)), size = 30)
            time.sleep(2)
            self.game_main_menu()
        else:
            for player_name, active_player in self.player_group.items():
                active_player.restart()
                pygame.draw.circle(self.game_display,  active_player.color,  active_player.pos, 3)
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
                            running = False

    def game_main_menu(self):
        self.game_over = False
        self.game_display.fill(BLACK)
        welcoming_img = self.blit_img('ACHTUNG.png',(self.display_width/2, self.display_height/3),(900, 300))
        num_players_text = 'Number of players: '
        running = True
        self.message_display(num_players_text + str(self.num_players), self.display_width/2, int(round(self.display_height/1.5)), size = 20)
        while running:
                self.game_display.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.create_players()
                            self.game_intro()
                            running = False
                        if event.key == pygame.K_UP:
                            self.num_players += 1
                            self.game_display.fill(BLACK)
                            self.blit_img('ACHTUNG.png',(self.display_width/2, self.display_height/3),(600, 200))
                            self.message_display(num_players_text + str(self.num_players), self.display_width/2, int(round(self.display_height/1.5)), size = 20)

                        if event.key == pygame.K_DOWN:
                            self.num_players -= 1
                            self.game_display.fill(BLACK)
                            self.blit_img('ACHTUNG.png',(self.display_width/2, self.display_height/3),(600, 200))
                            self.message_display(num_players_text + str(self.num_players), self.display_width/2, int(round(self.display_height/1.5)), size = 20)

achtung = game(display_width, display_height, 5)
achtung.game_main_menu()
