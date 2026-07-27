import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random as rd
from player import Player

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle1 = rd.uniform(60, 180)
            random_angle2 = rd.uniform(20, 50)
            new_ast1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
            new_ast2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
            new_ast1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle1)*1.2
            new_ast2.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle2)*1.3