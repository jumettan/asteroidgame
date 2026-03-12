from circleshape import CircleShape
from constants import *
import pygame
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        new_x = self.position.x
        new_y = self.position.y
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_vector = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(new_x,new_y,new_radius)
            asteroid2 = Asteroid(new_x, new_y,new_radius)
            asteroid1.velocity = (new_vector * 1.2)
            asteroid2.velocity = (new_vector2 * 1.2)

        