import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

player_setup = {
1:(pygame.K_LEFT, pygame.K_RIGHT, RED),
2:(pygame.K_q, pygame.K_w, GREEN),
3:(pygame.K_b, pygame.K_n, YELLOW),
4:(pygame.K_k, pygame.K_l, BLUE),
5:(pygame.K_z, pygame.K_x, WHITE)}
