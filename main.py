import pygame
import constants
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    # screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    player = Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
    asteroidField = AsteroidField()

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for obj in updatable:
            obj.update(dt)
            
        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for s in shots:
                if obj.collides_with(s):
                    log_event("asteroid_shot")
                    obj.kill()
                    s.kill()

        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
