from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        log_event("asteroid_split")
    
        angle = random.uniform(20, 50)
        vec_1 = self.velocity.rotate(angle)
        vec_2 = self.velocity.rotate(-1 * angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        (x, y) = self.position
        ast_1 = Asteroid(x, y, self.radius / 2)
        ast_2 = Asteroid(x, y, self.radius / 2)
        ast_1.velocity = vec_1 * 1.2
        ast_2.velocity = vec_2 * 1.2
        self.kill()
        