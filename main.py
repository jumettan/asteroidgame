import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.init()
    while True:
        log_state()
        screen.fill("black")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        else:
            pass
    print("Starting Asteroids with pygame version: VERSION","Screen width:",SCREEN_WIDTH,"Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
