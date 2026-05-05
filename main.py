import pygame
import constants
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    # screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        dt = clock.tick(60) / 1000
        pygame.display.flip()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
