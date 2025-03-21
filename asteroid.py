import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        vec1 = pygame.Vector2(self.velocity) * 1.2
        vec2 = pygame.Vector2(self.velocity) 
        random_angle = random.uniform(20,50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS).velocity = vec1.rotate(random_angle)
        Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS).velocity = vec2.rotate(-random_angle)

# hello world
