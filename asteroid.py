import pygame
from circleshape import CircleShape

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
