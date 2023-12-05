import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1066, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pupcake Run")

# Function to display image
def display_image(image_filename):
    # Getting the current working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Specifing the folder names where the image is located
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

# Function to display a button and switch to a new image
def display_button_and_new_image(new_image):
    # Function to draw a button
    def draw_button():
        button_rect = pygame.Rect(450, 500, 150, 50)
        button_color = (100, 100, 255)
        text_color = (255, 255, 255)
        font = pygame.font.Font(None, 36)

        pygame.draw.rect(screen, button_color, button_rect)
        text = font.render("Next Image", True, text_color)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

        return button_rect

    # Looping the game for the button
    button_running = True
    while button_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                button_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    button_rect = draw_button()
                    if button_rect.collidepoint(event.pos):
                        # Switch to the new image when the button is clicked
                        display_image(new_image)
                        button_running = False  # Exit the button loop

        # Draw the button
        draw_button()

        # Updating the display
        pygame.display.flip()

# Displaying P1
display_image("P1.png")

# Displaying P2
display_button_and_new_image("P2.png")

# Looping the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating the display
    pygame.display.flip()

# Quiting
pygame.quit()
sys.exit()