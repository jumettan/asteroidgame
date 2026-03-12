import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import *
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Window created")
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    #asteroid
    Asteroid.containers = (asteroids,updatable,drawable)

    #field
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    #shot
    Shot.containers = (shots,updatable,drawable)

    while True:
        log_state()
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        else:
            pass
        dt = clock.tick(60)/1000
    print("Starting Asteroids with pygame version: VERSION","Screen width:",SCREEN_WIDTH,"Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
