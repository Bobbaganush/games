import pygame

class player:
    def __init__(self,left_button,right_button,start_x,start_y,color):
        self.left_button = left_button
        self.right_button = right_button
        self.x = start_x
        self.y = start_y
        self.pos = (start_x,start_y)
        self.prev_pos = (start_x,start_y)
        self.speed = 5
        self.turn_speed = 1
        self.x_speed = 3
        self.y_speed = 3
        self.left = False
        self.right = False
        self.color = color
        self.alive = True

    def move(self, left, right):
        self.prev_pos = self.pos
        if left:
            if self.x_speed > 0 and self.y_speed >= 0:
                self.y_speed -= self.turn_speed
                self.x_speed += self.turn_speed
            elif self.x_speed <= 0 and self.y_speed >= 0:
                self.y_speed += self.turn_speed
                self.x_speed += self.turn_speed
            elif self.x_speed > 0 and self.y_speed < 0:
                self.x_speed -= self.turn_speed
                self.y_speed -= self.turn_speed
            elif self.x_speed <= 0 and self.y_speed < 0:
                self.x_speed -= self.turn_speed
                self.y_speed += self.turn_speed
        if right:
            if self.x_speed > 0 and self.y_speed >= 0:
                self.y_speed += self.turn_speed
                self.x_speed -= self.turn_speed
            elif self.x_speed <= 0 and self.y_speed >= 0:
                self.y_speed -= self.turn_speed
                self.x_speed -= self.turn_speed
            elif self.x_speed > 0 and self.y_speed < 0:
                self.x_speed += self.turn_speed
                self.y_speed += self.turn_speed
            elif self.x_speed <= 0 and self.y_speed < 0:
                self.x_speed += self.turn_speed
                self.y_speed -= self.turn_speed

        if self.x_speed > self.speed:
            self.x_speed = self.speed
        if self.y_speed > self.speed:
            self.y_speed = self.speed
        if self.x_speed < -self.speed:
            self.x_speed = -self.speed
        if self.y_speed < -self.speed:
            self.y_speed = -self.speed
        self.x += self.x_speed
        self.y += self.y_speed
        self.pos = (self.x,self.y)
        self.left = False
        self.right = False

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
