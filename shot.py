from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x: float, y: float, velocity: pygame.Vector2):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.x = x
        self.y = y
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity * PLAYER_SHOOT_SPEED) * dt
