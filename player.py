import pygame
import random
import math

class player:
    def __init__(self,name,left_button,right_button, display_width, display_height,color):
        self.name = name
        self.left_button = left_button
        self.right_button = right_button

        self.display_width = display_width
        self.display_height = display_height
        self.left = False
        self.right = False
        self.color = color
        self.alive = True
        self.victory_points = 0
        self.won = False
        self.rotate_degree = 0
        self.restart()

    def restart(self):
        self.x = random.randrange(0,self.display_width)
        self.y = random.randrange(0,self.display_height)
        self.pos = (self.x,self.y)
        self.prev_pos = self.pos
        self.speed = 5
        self.turn_speed = 12
        self.x_speed = random.randrange(-5,5)
        self.alive = True

    def move(self, left, right):
        self.prev_pos = self.pos
        if left:
            if self.rotate_degree < 360:
                self.rotate_degree += self.turn_speed
            else:
                self.rotate_degree = 0
        if right:
            if self.rotate_degree > 0:
                self.rotate_degree -= self.turn_speed
            else:
                self.rotate_degree = 360

        if self.alive == False:
            self.speed = 0
        self.left = False
        self.right = False
        dx = math.cos(math.radians(self.rotate_degree))
        dy = math.sin(-math.radians(self.rotate_degree))
        if self.speed > 0:
            self.pos = (self.pos[0] + dx * self.speed, self.pos[1] + dy * self.speed)
            self.x = int(self.pos[0])
            self.y = int(self.pos[1])
            self.pos = (self.x,self.y)


    def get_passed_pixels(self):
        self.passed_pixels = []
        x = self.x
        y = self.y
        x_p = self.prev_pos[0]
        y_p = self.prev_pos[1]
        while x != x_p or y != y_p:
            self.passed_pixels.append((x,y))
            if abs(x - x_p) > abs(y - y_p):
                if x > x_p:
                    x -= 1
                elif x < x_p:
                    x += 1
            else:
                if y > y_p:
                    y -= 1
                elif y < y_p:
                    y += 1
