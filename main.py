import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Sprite groups
asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

# Set static containers
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Player.containers = (updatable, drawable)

# Create asteroid field
asteroid_field = AsteroidField()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    running = True
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        dt = clock.tick(60) / 1000  # Time in seconds since last loop

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all updatable sprites
        updatable.update(dt)

        # Draw all drawable sprites
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
