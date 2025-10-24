import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Sprite groups
asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

# Set static containers
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Player.containers = (updatable, drawable)
Shot.containers = (updatable,drawable)  # add shots to drawable automatically

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

    # Create player and shots list
    shots = []
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)

    running = True
    while running:
        dt = clock.tick(60) / 1000  # Delta time in seconds

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all updatable sprites (includes player & asteroids)
        updatable.update(dt)

        # Check collisions between player and asteroids
        for asteroid in list(asteroids):
            if player.collides_with(asteroid):
                print("Game Over!")
                pygame.quit()
                exit()
            for shot in shots[:]:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    if shot in shots:
                        shots.remove(shot)

        # Update bullets and remove off-screen shots
        for shot in shots[:]:
            shot.update(dt)
            if (shot.position.x < 0 or shot.position.x > SCREEN_WIDTH or
                shot.position.y < 0 or shot.position.y > SCREEN_HEIGHT):
                shots.remove(shot)

        # Draw everything
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
