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

# Function for clikcing a button
def click1(dimensions):
    # color = (255, 0, 0) # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions) # DELETE AT THE END
    # pygame.display.flip() # DELETE AT THE END

    clicked_button = None

    # Waiting for button to be clicked
    while clicked_button is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Checking if the mouse click is inside the button
                if dimensions.collidepoint(event.pos):
                    # Returning True if clicked inside the button
                    clicked_button = True
    
    return clicked_button

# Function for clicking two buttons
def click2(dimensions1, dimensions2):
    # color = (255, 0, 0)  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions1)  # DELETE AT THE END
    # pygame.display.flip()  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions2)  # DELETE AT THE END
    # pygame.display.flip()  # DELETE AT THE END

    clicked_button = None

    # Waiting for button to be clicked
    while clicked_button is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Checking if the mouse click is inside the first button
                if dimensions1.collidepoint(event.pos):
                    # Returning 1 if clicked inside the first button
                    clicked_button = 1
                # Checking if the mouse click is inside the second button
                elif dimensions2.collidepoint(event.pos):
                    # Returning 2 if clicked inside the second button
                    clicked_button = 2

    return clicked_button

# Function for clicking three buttons
def click3(dimensions1, dimensions2, dimensions3):
    # color = (255, 0, 0)  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions1)  # DELETE AT THE END
    # pygame.display.flip()  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions2)  # DELETE AT THE END
    # pygame.display.flip()  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions3)  # DELETE AT THE END
    # pygame.display.flip()  # DELETE AT THE END

    clicked_button = None

    # Waiting for button to be clicked
    while clicked_button is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Checking if the mouse click is inside the first button
                if dimensions1.collidepoint(event.pos):
                    # Returning 1 if clicked inside the first button
                    clicked_button = 1
                # Checking if the mouse click is inside the second button
                elif dimensions2.collidepoint(event.pos):
                    # Returning 2 if clicked inside the second button
                    clicked_button = 2
                # Checking if the mouse click is inside the third button
                elif dimensions3.collidepoint(event.pos):
                    # Returning 3 if clicked inside the third button
                    clicked_button = 3

    return clicked_button

# Function for Level 1
# Function for Level 2

# Function for repeating Level 1
def repeat1():
    pass

# Function for repeating Level 2

# GAME
# Display P1
display_image("P1.png")
pygame.display.flip()

# Button on P1
p1_button1 = pygame.Rect(414, 281, 239, 53) # "Play"

# Transition with button to P2
if click1(p1_button1):
    display_image("P2.png")
    pygame.display.flip()

# Buttons on P2
p2_button1 = pygame.Rect(328, 393, 84, 45) # "Yes"
p2_button2 = pygame.Rect(909, 531, 124, 53) # "Skip"
p2_click = click2(p2_button1, p2_button2)

# Transition with button 1 to P3
if p2_click == 1:
    display_image("P3.png")
    pygame.display.flip()

    # Button on P3
    p3_button1 = pygame.Rect(328, 393, 84, 45) # "Ok"
    
    # Transition with button to P4
    if click1(p3_button1):
        display_image("P4.png")
        pygame.display.flip()

        # Button on P4
        p4_button1 = pygame.Rect(328, 393, 84, 45) # "Start"
        
        # Transition with button to P5
        if click1(p4_button1):
            display_image("P5.png")
            pygame.display.flip()
            pygame.time.delay(500)

# Transition with button 2 to P5
elif p2_click == 2:
    display_image("P5.png")
    pygame.display.flip()
    pygame.time.delay(500)

# Auto transition from P6 to P10
page_list1 = ["P6.png", "P7.png", "P8.png", "P9.png", "P10.png"]

# Looping through the list and displing each image with a delay
for page in page_list1:
    display_image(page)
    pygame.display.flip()
    pygame.time.delay(500)

# Play Level 1 on P10
pygame.time.delay(3000)
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

# Button on P24
p24_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

# Transition with button to P25
if click1(p24_button1):
    display_image("P25.png")
    pygame.display.flip()

# Buttons on P25
p25_button1 = pygame.Rect(128, 286, 176, 74) # "Light" - correct
p25_button2 = pygame.Rect(351, 286, 176, 74) # "Glass" - wrong
p25_button3 = pygame.Rect(176, 396, 303, 74) # "Rubberband" - wrong
p25_click = click3(p25_button1, p25_button2, p25_button3)

# Transition with button 2 and 3 to P61 then P62
if p25_click == 2 or p25_click == 3:
    display_image("P61.png")
    pygame.display.flip()
    pygame.time.delay(1500)
    display_image("P62.png")
    pygame.display.flip()
    pygame.time.delay(1000)
    # Repeat here

# Transition to P26
display_image("P26.png")
pygame.display.flip()

# Button on P26
p26_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

# Transition with button to P27
if click1(p26_button1):
    display_image("P27.png")
    pygame.display.flip()
    pygame.time.delay(500)

# Auto transition from P28 to P32
page_list3 = ["P28.png", "P29.png", "P30.png", "P31.png", "P32.png"]

# Looping through the list and displing each image with a delay
for page in page_list3:
    display_image(page)
    pygame.display.flip()
    pygame.time.delay(500)

# Play Level 2 on P32
pygame.time.delay(3000)
    # If obstacle hit, go to P60

# Auto transition from P33 to P46
page_list4 = ["P33.png", "P34.png", "P35.png", "P36.png", "P37.png",
              "P38.png", "P39.png", "P40.png", "P41.png", "P42.png",
              "P43.png", "P44.png", "P45.png", "P46.png"]

# Looping through the list and displing each image with a delay
for page in page_list4:
    display_image(page)
    pygame.display.flip()
    pygame.time.delay(150)

# Button on P46
p46_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

# Transition with button to P47
if click1(p46_button1):
    display_image("P47.png")
    pygame.display.flip()

# Buttons on P47
p47_button1 = pygame.Rect(128, 300, 176, 74) # "Food" - wrong
p47_button2 = pygame.Rect(351, 300, 176, 74) # "Age" - wrong
p47_button3 = pygame.Rect(176, 410, 303, 74) # "Footsteps" - correct
p47_click = click3(p47_button1, p47_button2, p47_button3)

# Transition with button 1 and 2 to P61 then P63
if p47_click == 1 or p47_click == 2:
    display_image("P61.png")
    pygame.display.flip()
    pygame.time.delay(1500)
    display_image("P63.png")
    pygame.display.flip()
    pygame.time.delay(1000)
    # Repeat here

# Transition to P48
display_image("P48.png")
pygame.display.flip()

# Button on P48
p48_button1 = pygame.Rect(454, 370, 84, 45) # "Go"

# Transition with button to P49
if click1(p48_button1):
    display_image("P49.png")
    pygame.display.flip()

# Button on P49
p49_button1 = pygame.Rect(382, 392, 84, 45) # "Ok"

# Transition with button to P50
if click1(p49_button1):
    display_image("P50.png")
    pygame.display.flip()

# Buttons on P50
p50_button1 = pygame.Rect(128, 319, 176, 74) # "Coins" - wrong
p50_button2 = pygame.Rect(351, 319, 176, 74) # "Time" - wrong
p50_button3 = pygame.Rect(176, 430, 303, 74) # "Secret" - correct
p50_click = click3(p50_button1, p50_button2, p50_button3)

# Transition with button 1 and 2 to P60 then P1
if p50_click == 1 or p50_click == 2:
    display_image("P60.png")
    pygame.display.flip()

    # Button on P60
    p60_button1 = pygame.Rect(414, 370, 239, 53) # "Play Again"

    # Restart if button is clicked
    if click1(p60_button1):
        display_image("P1.png")
        pygame.display.flip()
        pygame.time.delay(1000)

# Transition to P51
display_image("P51.png")
pygame.display.flip()

# Button on P51
p51_button1 = pygame.Rect(382, 392, 84, 45) # "Ok"

# Transition with button to P52
if click1(p51_button1):
    display_image("P52.png")
    pygame.display.flip()

# Button on P52
p52_button1 = pygame.Rect(675, 362, 112, 45) # "Collect"

# Transition with button to P53
if click1(p52_button1):
    display_image("P53.png")
    pygame.display.flip()
    pygame.time.delay(500)

# Auto transition from P54 to P58
page_list5 = ["P54.png", "P55.png", "P56.png", "P57.png", "P58.png"]

# Looping through the list and displing each image with a delay
for page in page_list5:
    display_image(page)
    pygame.display.flip()
    pygame.time.delay(500)

# Button on P58
p58_button1 = pygame.Rect(753, 355, 84, 45) # "Ok"

# Transition with button to P59
if click1(p58_button1):
    display_image("P59.png")
    pygame.display.flip()

# Button on P59
p59_button1 = pygame.Rect(414, 281, 239, 53) # "Play Again"

# Restart if button is clicked
if click1(p59_button1):
    display_image("P1.png")
    pygame.display.flip()

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