import pygame
from pygame.math import Vector2
from typing import cast

from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED

class Player(CircleShape):
    
    def __init__(self, x, y):
        self.rotation = 0
        super().__init__(x, y, PLAYER_RADIUS)
        
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90)
        forward_scaled = cast(Vector2, forward * self.radius)
        right_scaled = cast(Vector2, right * (self.radius / 1.5))

        a = self.position + forward_scaled
        b = self.position - forward_scaled - right_scaled
        c = self.position - forward_scaled + right_scaled
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)