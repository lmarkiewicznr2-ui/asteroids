import pygame
from constants import *
from player import Player
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.container = (updatable, drawable)

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
        # Handle events
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # stops the loop when user clicks close 
        updatable.update(dt)  # Update player state
        # Fill the screen black
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        # Refresh the display
        pygame.display.flip()

    pygame.quit()  # cleanly close Pygame

if __name__ == "__main__":
    main()

