import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # stops the loop when user clicks close

        # Fill the screen black
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip()

    pygame.quit()  # cleanly close Pygame

if __name__ == "__main__":
    main()
