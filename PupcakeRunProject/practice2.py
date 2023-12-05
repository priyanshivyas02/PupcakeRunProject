import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Click Detection")

# Set up some colors
black = (0, 0, 0)
white = (255, 255, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse coordinates
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Define a clickable area (for example, a rectangle)
            clickable_area = pygame.Rect(300, 200, 200, 100)

            # Check if the mouse click is within the clickable area
            if clickable_area.collidepoint(mouse_x, mouse_y):
                print("You clicked the area!")
                # Add your code here to perform actions when the area is clicked

    # Clear the screen
    screen.fill(white)

    # Draw the clickable area
    pygame.draw.rect(screen, black, clickable_area)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()