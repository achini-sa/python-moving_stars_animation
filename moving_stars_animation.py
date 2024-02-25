import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shining Stars")

# Define colors
black = (0, 0, 0)

# Create a list to store the stars
stars = [{'x': random.randint(0, width), 'y': random.randint(0, height), 'speed': random.uniform(1, 3),
          'brightness': random.randint(100, 255)} for _ in range(100)]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update star positions and brightness
    for star in stars:
        star['y'] += star['speed']
        star['brightness'] = random.randint(100, 255)

        if star['y'] > height:
            star['y'] = 0
            star['x'] = random.randint(0, width)

    # Draw background
    screen.fill(black)

    # Draw stars
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255, star['brightness']), (int(star['x']), int(star['y'])), 2)

    # Update display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
