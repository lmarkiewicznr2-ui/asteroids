import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    containers = ()  # Set in main.py

    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity  # pygame.Vector2

    def update(self, dt):
        # Move the shot based on velocity and delta time
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (int(self.position.x), int(self.position.y)),
            self.radius
        )
