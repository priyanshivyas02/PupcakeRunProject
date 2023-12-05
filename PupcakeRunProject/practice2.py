# IMPORTS
import pygame
import sys
import os

# INITIALIZING
# Initialize Pygame
pygame.init()

# Set up display
width, height = 1066, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pupcake Run")

# FUNCTIONS
# Function to display image
def display_image(image_filename):
    # Getting the current working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Specifying the folder names where the image is located
    parent_folder = "Pupcake Run Images"
    images_folder = "Pages"

    # Combining the current directory with the folder names and filenames
    image_path = os.path.join(current_directory, parent_folder, images_folder, image_filename)

    # Loading the image
    original_image = pygame.image.load(image_path)

    # Setting the desired size
    desired_width, desired_height = 1066, 600

    # Scaling the image to the desired size
    scaled_image = pygame.transform.scale(original_image, (desired_width, desired_height))

    # Calculating the position to center the image on the screen
    x_pos = (width - scaled_image.get_width()) // 2
    y_pos = (height - scaled_image.get_height()) // 2

    # Drawing the image on the screen and centering it
    screen.blit(scaled_image, (x_pos, y_pos))

# GAME
# Display P1
display_image("P1.png")
pygame.display.flip()
# pygame.time.delay(1000)

# Draw a rectangle on P1
rect_color = (0,0,0)  # Red color for the rectangle
rect_dimensions = pygame.Rect(100, 100, 200, 150)  # Change dimensions as needed

# Flag to track if the rectangle is visible
rectangle_visible = True

# Auto transition start flag
auto_transition_start = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is inside the rectangle
            if rect_dimensions.collidepoint(event.pos):
                # Toggle rectangle visibility
                rectangle_visible = not rectangle_visible
                if not rectangle_visible:
                    auto_transition_start = True  # Start auto transition after rectangle disappears

    # Draw the rectangle if it is visible
    # if rectangle_visible:
    #     pygame.draw.rect(screen, rect_color, rect_dimensions)

    # Updating the display
    pygame.display.flip()

    # If auto transition is started, break out of the loop to proceed with the auto transition
    if auto_transition_start:
        break

# Auto transition from P6 to P10 (Example transition, replace with your logic)
page_list1 = ["P6.png", "P7.png", "P8.png", "P9.png", "P10.png"]

# Looping through the list and displaying each image with a delay
for page in page_list1:
    display_image(page)
    pygame.display.flip()
    pygame.time.delay(150)

# Continue with the rest of your game logic...

# Quitting
pygame.quit()
sys.exit()