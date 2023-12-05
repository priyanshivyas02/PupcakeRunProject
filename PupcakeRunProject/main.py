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
pygame.time.delay(1000)

# Transition with button to P2
# Transition with button to P3
# Transition with button to P4
# Transition with button to P5
    # Time delay here

# Auto transition from P6 to P10

# Play Level 1 on P10
    # If obstacle hit, go to P60

# Auto transition from P11 to P24
page_list2 = ["P11.png", "P12.png", "P13.png", "P14.png", "P15.png",
                   "P16.png", "P17.png", "P18.png", "P19.png", "P20.png",
                   "P21.png", "P22.png", "P23.png", "P24.png"]

# Looping through the list and displing each image with a delay
for page in page_list2:
    display_image(page)
    pygame.display.flip()
    pygame.time.delay(150)

# Transition with button to P25
# Transition with button to P26
# Transition with button to P27
    # Time delay here

# Auto transition from P28 to P32

# Play Level 2 on P32
    # If obstacle hit, go to P60

# Auto transition from P33 to P46

# Transition with button to P47
# Transition with button to P48
# Transition with button to P49
# Transition with button to P50
# Transition with button to P51
# Transition with button to P52
# Transition with button to P53
    # Time delay here

# Auto transition from P54 to P58
# Transition with button to P59
# Restart if button is clicked on P59


# Looping the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating the display
    pygame.display.flip()

# Quitting
pygame.quit()
sys.exit()