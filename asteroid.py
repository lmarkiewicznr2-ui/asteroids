import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = None  # Will be set in main.py

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Optional: set default velocity
        # self.velocity = pygame.Vector2(50, 0)

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            (200, 200, 200),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        # Move asteroid at constant velocity
        self.position += self.velocity * dt
    
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(angle) * 1.2
        vel2 = self.velocity.rotate(-angle) * 1.2
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2

        for group in self.groups():
            group.add(asteroid1, asteroid2)