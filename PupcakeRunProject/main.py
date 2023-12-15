# IMPORTS
import pygame
import sys
import os
import random
import asyncio
from pygame import mixer
#Instantiate mixer
mixer.init()

#Load audio file
mixer.music.load('cruising-down-8bit-lane-159615.mp3')



#Set preferred volume
mixer.music.set_volume(0.2)

#Play the music
mixer.music.play()

# INITIALIZING
# Initialize Pygame
pygame.init()

# Set up display
width, height = 1066, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pupcake Run")

# FUNCTIONS
# DISPLAYS
# Function to display page
def display_page(image_filename):
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

    # Drawing the scalred image on the screen and centering it
    screen.blit(scaled_image, (x_pos, y_pos))

# Function to display Sprinkles
def display_sprinkles(image_filename):
    # Getting the current working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Specifying the folder names where the image is located
    parent_folder = "Pupcake Run Images"
    images_folder = "Sprinkles"
    # Combining the current directory with the folder names and filenames
    image_path = os.path.join(current_directory, parent_folder, images_folder, image_filename)
    # Loading the image
    original_image = pygame.image.load(image_path)

    # Setting the desired size
    desired_width, desired_height = 120, 168 # Standing: 141, 168
    # Scaling the image to the desired size
    scaled_image = pygame.transform.scale(original_image, (desired_width, desired_height))

    return scaled_image

# Function to display bush
def display_bush(image_filename):
    # Getting the current working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Specifying the folder names where the image is located
    parent_folder = "Pupcake Run Images"
    images_folder = "Bushes"
    # Combining the current directory with the folder names and filenames
    image_path = os.path.join(current_directory, parent_folder, images_folder, image_filename)
    # Loading the image
    original_image = pygame.image.load(image_path)

    # Setting the desired size
    desired_height = 50
    aspect_ratio = original_image.get_height() / original_image.get_width()
    desired_width = int(desired_height / aspect_ratio)
    # Scaling the image to the desired size
    scaled_image = pygame.transform.scale(original_image, (desired_width, desired_height))

    return scaled_image

# Function to display rock
def display_rock(image_filename):
    # Getting the current working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Specifying the folder names where the image is located
    parent_folder = "Pupcake Run Images"
    images_folder = "Rocks"
    # Combining the current directory with the folder names and filenames
    image_path = os.path.join(current_directory, parent_folder, images_folder, image_filename)
    # Loading the image
    original_image = pygame.image.load(image_path)

    # Setting the desired size
    desired_height = 50
    aspect_ratio = original_image.get_height() / original_image.get_width()
    desired_width = int(desired_height / aspect_ratio)
    # Scaling the image to the desired size
    scaled_image = pygame.transform.scale(original_image, (desired_width, desired_height))

    return scaled_image

# Function to display crystal
def display_crystal(image_filename):
    # Getting the current working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Specifying the folder names where the image is located
    parent_folder = "Pupcake Run Images"
    images_folder = "Crystals"
    # Combining the current directory with the folder names and filenames
    image_path = os.path.join(current_directory, parent_folder, images_folder, image_filename)
    # Loading the image
    original_image = pygame.image.load(image_path)

    # Setting the desired size
    desired_height = 50
    aspect_ratio = original_image.get_height() / original_image.get_width()
    desired_width = int(desired_height / aspect_ratio)
    # Scaling the image to the desired size
    scaled_image = pygame.transform.scale(original_image, (desired_width, desired_height))

    return scaled_image

# Function to display cupcake
def display_cupcake():
    # Getting the current working directory
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Specifying the folder names where the image is located
    images_folder = "Pupcake Run Images"
    image_filename = "Cupcake.png"
    # Combining the current directory with the folder names and filenames
    image_path = os.path.join(current_directory, images_folder, image_filename)
    # Loading the image
    original_image = pygame.image.load(image_path)

    # Setting the desired size
    desired_width, desired_height = 32, 40
    # Scaling the image to the desired size
    scaled_image = pygame.transform.scale(original_image, (desired_width, desired_height))

    return scaled_image

# BUTTONS
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

# Function for clicking four buttons
def click4(dimensions1, dimensions2, dimensions3, dimensions4):
    # color = (255, 0, 0)  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions1)  # DELETE AT THE END
    # pygame.display.flip()  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions2)  # DELETE AT THE END
    # pygame.display.flip()  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions3)  # DELETE AT THE END
    # pygame.display.flip()  # DELETE AT THE END
    # pygame.draw.rect(screen, color, dimensions4)  # DELETE AT THE END
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
                # Checking if the mouse click is inside the fourth button
                elif dimensions4.collidepoint(event.pos):
                    # Returning 4 if clicked inside the fourth button
                    clicked_button = 4

    return clicked_button

# CLASSES
# Timer Class
class Timer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.__highscore = 0
    
    # Getting highscore
    def get_highscore(self):
        return self.__highscore
    
    # Setting highscore
    def set_highscore(self, score):
        # Updating score
        if score >= self.get_highscore():
            self.__highscore = score

# Sprinkles Class
class Sprinkles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [display_sprinkles("Sprinkles Left.png"), display_sprinkles("Sprinkles Right.png")]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 37
        self.rect.y = 357
        self.jump = False
        self.jump_height = 20
        self.jump_count = 14
        self.animation_timer = pygame.time.get_ticks()
        self.animation_interval = 150

    def update(self):
        keys = pygame.key.get_pressed()
        if not self.jump:
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.jump_count >= -self.jump_height:
                direction = 1
                if self.jump_count < 0:
                    direction = -1
                self.rect.y -= (self.jump_count ** 2) * direction / 5
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 14

        # Ensure the dinosaur stays on the ground
        if self.rect.y > 357:
            self.rect.y = 357

        # Animation timer for running
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_timer >= self.animation_interval:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.animation_timer = current_time

# Bush Class
class Bush(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [display_bush(f"Bush {i}.png") for i in range(1, 5)]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 470

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = width
            self.image = random.choice(self.images)

# Rock Class
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [display_rock(f"Rock {i}.png") for i in range(1, 5)]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 470

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = width
            self.image = random.choice(self.images)

# Crystal Class
class Crystal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [display_crystal(f"Crystal {i}.png") for i in range(1, 2)]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 470

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = width
            self.image = random.choice(self.images)

# Cupcake Class
class Cupcake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = display_cupcake()
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = 440

    def update(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.left = width

# FUNCTIONS
# LEVELS
# Getting background for Level 1
dictionary1 = os.path.join(os.path.dirname(os.path.realpath(__file__)))
path1 = os.path.join(os.path.join(dictionary1), "Level1.png")
background1 = pygame.image.load(path1)

# Making socre and highscore for Level 1
score_system1 = Timer()

# Function for Level 1 (Time = 10)
time1 = 10
def level1():
    # Auto transition from P5 to P9
    page_list1 = ["P5.png" ,"P6.png", "P7.png", "P8.png", "P9.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list1:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(500)

    # Game on P10
    all_sprites = pygame.sprite.Group()
    bushes = pygame.sprite.Group()
    # Create Sprinkles
    sprinkles = Sprinkles()
    all_sprites.add(sprinkles)
    # Create bush
    bush = Bush()
    bushes.add(bush)
    all_sprites.add(bush)
    # Create cupcake
    cupcake = Cupcake()

    # Main game loop
    clock = pygame.time.Clock()
    running = True
    
    # Duration of game
    start_time = pygame.time.get_ticks()
    game_duration = time1 * 1000

    # Timer for cupcakes
    last_cupcake_time = pygame.time.get_ticks()

    # Set up font for the timer display
    font = pygame.font.Font(None, 50)

    # Game is running
    while running and pygame.time.get_ticks() - start_time < game_duration:
        # Quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()
        bushes.update()
        current_time = pygame.time.get_ticks()
        if (current_time - last_cupcake_time) >= 2000:
            cupcake.update()
        
        # Collision between Sprinkles and cupcake
        if pygame.sprite.spritecollide(sprinkles, [cupcake], False):
            cupcake.kill()
            cupcake = Cupcake()
        
        # Draw
        screen.blit(background1, (0, 0))
        all_sprites.draw(screen)
        bushes.draw(screen)
        screen.blit(cupcake.image, cupcake.rect)

        # Display the timer
        score_system1.score = ((pygame.time.get_ticks() - start_time) // 1000)
        score = font.render(f"{score_system1.score:02d}", True, (46, 27, 91))
        screen.blit(score, (945, 84))
        score_system1.set_highscore(score_system1.score)
        highscore = font.render(f"{score_system1.get_highscore():02d}", True, (46, 27, 91))
        screen.blit(highscore, (777, 84))

        # Refresh screen
        pygame.display.flip()
        clock.tick(60)
        
        # Collision between Sprinkles and bush
        if pygame.sprite.spritecollide(sprinkles, [bush], False):
            # Displaying P84
            display_page("P84.png")

            # Displaying score and highscore
            score_text = font.render(f"{score_system1.score:02d}", True, (46, 27, 91))
            screen.blit(score_text, (585, 268))
            score_system1.set_highscore(score_system1.score)
            highscore_text = font.render(f"{score_system1.get_highscore():02d}", True, (46, 27, 91))
            screen.blit(highscore_text, (585, 320))
            
            # Button on P84
            p84_button1 = pygame.Rect(414, 373, 239, 53) # "Restart"
            pygame.display.flip()
            running = False

            # Transition with button to Level 1
            if click1(p84_button1):
                level1()

# Getting background for Level 2
dictionary2 = os.path.join(os.path.dirname(os.path.realpath(__file__)))
path2 = os.path.join(os.path.join(dictionary2), "Level2.png")
background2 = pygame.image.load(path2)

# Making socre and highscore for Level 2
score_system2 = Timer()

# Function for Level 2 (Time = 20)
time2 = 20
def level2():
    # Auto transition from P27 to P31
    page_list3 = ["P27.png", "P28.png", "P29.png", "P30.png", "P31.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list3:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(500)

    # Game on P10
    all_sprites = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    # Create Sprinkles
    sprinkles = Sprinkles()
    all_sprites.add(sprinkles)
    # Create rock
    rock = Rock()
    rocks.add(rock)
    all_sprites.add(rock)
    # Create cupcake
    cupcake = Cupcake()

    # Main game loop
    clock = pygame.time.Clock()
    running = True
    
    # Duration of game
    start_time = pygame.time.get_ticks()
    game_duration = time2 * 1000

    # Timer for cupcakes
    last_cupcake_time = pygame.time.get_ticks()

    # Set up font for the timer display
    font = pygame.font.Font(None, 50)

    # Game is running
    while running and pygame.time.get_ticks() - start_time < game_duration:
        # Quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()
        rocks.update()
        current_time = pygame.time.get_ticks()
        if (current_time - last_cupcake_time) >= 2000:
            cupcake.update()
        
        # Collision between Sprinkles and cupcake
        if pygame.sprite.spritecollide(sprinkles, [cupcake], False):
            cupcake.kill()
            cupcake = Cupcake()
        
        # Draw
        screen.blit(background2, (0, 0))
        all_sprites.draw(screen)
        rocks.draw(screen)
        screen.blit(cupcake.image, cupcake.rect)

        # Display the timer
        score_system2.score = ((pygame.time.get_ticks() - start_time) // 1000)
        score = font.render(f"{score_system2.score:02d}", True, (46, 27, 91))
        screen.blit(score, (945, 84))
        score_system2.set_highscore(score_system2.score)
        highscore = font.render(f"{score_system2.get_highscore():02d}", True, (46, 27, 91))
        screen.blit(highscore, (777, 84))

        # Refresh screen
        pygame.display.flip()
        clock.tick(60)
        
        # Collision between Sprinkles and bush
        if pygame.sprite.spritecollide(sprinkles, [rock], False):
            # Displaying P86
            display_page("P86.png")

            # Displaying score and highscore
            score_text = font.render(f"{score_system2.score:02d}", True, (46, 27, 91))
            screen.blit(score_text, (585, 268))
            score_system2.set_highscore(score_system2.score)
            highscore_text = font.render(f"{score_system2.get_highscore():02d}", True, (46, 27, 91))
            screen.blit(highscore_text, (585, 320))
            
            # Button on P86
            p86_button1 = pygame.Rect(414, 373, 239, 53) # "Restart"
            pygame.display.flip()
            running = False

            # Transition with button to Level 2
            if click1(p86_button1):
                level2()

# Getting background for Level 3
dictionary3 = os.path.join(os.path.dirname(os.path.realpath(__file__)))
path3 = os.path.join(os.path.join(dictionary2), "Level3.png")
background3 = pygame.image.load(path3)

# Making socre and highscore for Level 3
score_system3 = Timer()

# Function for Level 3 (Time = 30)
time3 = 30
def level3():
    # Auto transition from P49 to P53
    page_list3 = ["P49.png", "P50.png", "P51.png", "P52.png", "P53.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list3:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(500)

    # Game on P10
    all_sprites = pygame.sprite.Group()
    crystals = pygame.sprite.Group()
    # Create Sprinkles
    sprinkles = Sprinkles()
    all_sprites.add(sprinkles)
    # Create crystal
    crystal = Crystal()
    crystals.add(crystal)
    all_sprites.add(crystal)
    # Create cupcake
    cupcake = Cupcake()

    # Main game loop
    clock = pygame.time.Clock()
    running = True
    
    # Duration of game
    start_time = pygame.time.get_ticks()
    game_duration = time3 * 1000

    # Timer for cupcakes
    last_cupcake_time = pygame.time.get_ticks()

    # Set up font for the timer display
    font = pygame.font.Font(None, 50)

    # Game is running
    while running and pygame.time.get_ticks() - start_time < game_duration:
        # Quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()
        crystals.update()
        current_time = pygame.time.get_ticks()
        if (current_time - last_cupcake_time) >= 2000:
            cupcake.update()
        
        # Collision between Sprinkles and cupcake
        if pygame.sprite.spritecollide(sprinkles, [cupcake], False):
            cupcake.kill()
            cupcake = Cupcake()
        
        # Draw
        screen.blit(background3, (0, 0))
        all_sprites.draw(screen)
        crystals.draw(screen)
        screen.blit(cupcake.image, cupcake.rect)

        # Display the timer
        score_system3.score = ((pygame.time.get_ticks() - start_time) // 1000)
        score = font.render(f"{score_system3.score:02d}", True, (46, 27, 91))
        screen.blit(score, (945, 84))
        score_system3.set_highscore(score_system3.score)
        highscore = font.render(f"{score_system3.get_highscore():02d}", True, (46, 27, 91))
        screen.blit(highscore, (777, 84))

        # Refresh screen
        pygame.display.flip()
        clock.tick(60)
        
        # Collision between Sprinkles and bush
        if pygame.sprite.spritecollide(sprinkles, [crystal], False):
            # Displaying P88
            display_page("P88.png")

            # Displaying score and highscore
            score_text = font.render(f"{score_system3.score:02d}", True, (46, 27, 91))
            screen.blit(score_text, (585, 268))
            score_system3.set_highscore(score_system3.score)
            highscore_text = font.render(f"{score_system3.get_highscore():02d}", True, (46, 27, 91))
            screen.blit(highscore_text, (585, 320))
            
            # Button on P88
            p88_button1 = pygame.Rect(414, 373, 239, 53) # "Restart"
            pygame.display.flip()
            running = False

            # Transition with button to Level 3
            if click1(p88_button1):
                level3()

# REPEATS
# Function for repeating start of game
def repeat_start():
    # Display P2
    display_page("P2.png")
    pygame.display.flip()

    # Buttons on P2
    p2_button1 = pygame.Rect(328, 393, 84, 45) # "Yes"
    p2_button2 = pygame.Rect(909, 531, 124, 53) # "Skip"
    p2_click = click2(p2_button1, p2_button2)

    # Transition with button 1 to P3
    if p2_click == 1:
        display_page("P3.png")
        pygame.display.flip()

        # Button on P3
        p3_button1 = pygame.Rect(328, 393, 84, 45) # "Ok"
        
        # Transition with button to P4
        if click1(p3_button1):
            display_page("P4.png")
            pygame.display.flip()

            # Button on P4
            p4_button1 = pygame.Rect(328, 393, 84, 45) # "Start"
            
            # Transition with button to P5
            if click1(p4_button1):
                display_page("P5.png")
                pygame.display.flip()

    # Transition with button 2 to P5
    elif p2_click == 2:
        display_page("P5.png")
        pygame.display.flip()

# Function for repeating Level 1
def repeat_level1():
    # Auto transition from P5 to P9
    # Play Level 1 on P10
    level1()
    pygame.time.delay(150)

    # Auto transition from P11 to P24
    page_list2 = ["P11.png", "P12.png", "P13.png", "P14.png", "P15.png",
                "P16.png", "P17.png", "P18.png", "P19.png", "P20.png",
                "P21.png", "P22.png", "P23.png", "P24.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list2:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P24
    p24_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P25
    if click1(p24_button1):
        display_page("P25.png")
        pygame.display.flip()

    # Buttons on P25
    p25_button1 = pygame.Rect(128, 286, 176, 74) # "Light" - correct
    p25_button2 = pygame.Rect(351, 286, 176, 74) # "Glass" - wrong
    p25_button3 = pygame.Rect(176, 396, 303, 74) # "Rubberband" - wrong
    p25_click = click3(p25_button1, p25_button2, p25_button3)

    # Showing if correct (green) or wrong (red)
    if p25_click == 1:
        display_page("P25-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 2:
        display_page("P25-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 3:
        display_page("P25-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 2 and 3 to P85 then P1-1
    if p25_click == 2 or p25_click == 3:
        # Display P85
        display_page("P85.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-1
        display_page("P1-1.png")
        pygame.display.flip()

        # Buttons on P1-1
        p1_1_button1 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_1_button2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_1_click = click2(p1_1_button1, p1_1_button2)

        # Repeating whole game
        if p1_1_click == 1:
            repeat_game1()
        # Repeating level 1
        elif p1_1_click == 2:
            repeat_level1()

# Function for repeating Level 2
def repeat_level2():
    # Auto transition from P27 to P31
    # Play Level 2 on P32
    level2()
    pygame.time.delay(150)

    # Auto transition from P33 to P46
    page_list4 = ["P33.png", "P34.png", "P35.png", "P36.png", "P37.png",
                "P38.png", "P39.png", "P40.png", "P41.png", "P42.png",
                "P43.png", "P44.png", "P45.png", "P46.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list4:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P46
    p46_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P47
    if click1(p46_button1):
        display_page("P47.png")
        pygame.display.flip()

    # Buttons on P47
    p47_button1 = pygame.Rect(128, 300, 176, 74) # "Food" - wrong
    p47_button2 = pygame.Rect(351, 300, 176, 74) # "Age" - wrong
    p47_button3 = pygame.Rect(176, 410, 303, 74) # "Footsteps" - correct
    p47_click = click3(p47_button1, p47_button2, p47_button3)

    # Showing if correct (green) or wrong (red)
    if p47_click == 1:
        display_page("P47-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p47_click == 2:
        display_page("P47-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p47_click == 3:
        display_page("P47-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 2 to P87 then P1-2
    if p47_click == 1 or p47_click == 2:
        # Display P87
        display_page("P87.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-2
        display_page("P1-2.png")
        pygame.display.flip()

        # Buttons on P1-2
        p1_2_button1 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_2_button2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_2_button3 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_2_click = click3(p1_2_button1, p1_2_button2, p1_2_button3)

        # Repeating whole game
        if p1_2_click == 1:
            repeat_game2()
        # Repeating level 1 and then level 2
        elif p1_2_click == 2:
            repeat_levels_1_2()
        # Repeating level 2
        elif p1_2_click == 3:
            repeat_level2()

# Function for repeating Level 3
def repeat_level3():
    # Auto transition from P49 to P53
    # Play Level 3 on P54
    level3()
    pygame.time.delay(150)

    # Auto transition from P33 to P46
    page_list5 = ["P55.png", "P56.png", "P57.png", "P58.png", "P59.png",
                "P60.png", "P62.png", "P62.png", "P63.png", "P64.png",
                "P65.png", "P66.png", "P67.png", "P68.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list5:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P68
    p68_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P69
    if click1(p68_button1):
        display_page("P69.png")
        pygame.display.flip()

    # Buttons on P69
    p69_button1 = pygame.Rect(99, 319, 176, 74) # "Rain" - wrong
    p69_button2 = pygame.Rect(298, 319, 258, 74) # "Darkness" - correct
    p69_button3 = pygame.Rect(176, 430, 303, 74) # "Sunlight" - wrong
    p69_click = click3(p69_button1, p69_button2, p69_button3)

    # Showing if correct (green) or wrong (red)
    if p69_click == 1:
        display_page("P69-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p69_click == 2:
        display_page("P69-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p69_click == 3:
        display_page("P69-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 3 to P89 then P1-3
    if p69_click == 1 or p69_click == 3:
        # Display P89
        display_page("P89.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_1 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_1 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_1 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_1 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_1 = click4(p1_3_button1_1, p1_3_button2_1, p1_3_button3_1, p1_3_button4_1)

        # Repeating whole game
        if p1_3_click_1 == 1:
            repeat_game3()
        # Repeating level 1, level 2, and then level 3
        elif p1_3_click_1 == 2:
            repeat_levels_1_2_3()
        # Repeating level 2 and then level 3
        elif p1_3_click_1 == 3:
            repeat_levels_2_3()
        # Repeating level 3
        elif p1_3_click_1 == 4:
            repeat_level3()

# Function for repeating Evil Leprechaun stage
def repeat_leprechaun():
    # Transition to P70
    display_page("P70.png")
    pygame.display.flip()

    # Button on P70
    p70_button1 = pygame.Rect(454, 370, 84, 45) # "Go"

    # Transition with button to P71
    if click1(p70_button1):
        display_page("P71.png")
        pygame.display.flip()

    # Button on P71
    p71_button1 = pygame.Rect(382, 392, 84, 45) # "Ok"

    # Transition with button to P50
    if click1(p71_button1):
        display_page("P72.png")
        pygame.display.flip()

    # Buttons on P72
    p72_button1 = pygame.Rect(128, 319, 176, 74) # "Coins" - wrong
    p72_button2 = pygame.Rect(351, 319, 176, 74) # "Time" - wrong
    p72_button3 = pygame.Rect(176, 430, 303, 74) # "Secret" - correct
    p72_click = click3(p72_button1, p72_button2, p72_button3)

    # Showing if correct (green) or wrong (red)
    if p72_click == 1:
        display_page("P72-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p72_click == 2:
        display_page("P72-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p72_click == 3:
        display_page("P72-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 2 to P90
    if p72_click == 1 or p72_click == 2:
        display_page("P90.png")
        pygame.display.flip()

        # Button on P90
        p64_button1 = pygame.Rect(414, 324, 239, 53) # "Restart"

        # Transition with button to P1-3
        if click1(p64_button1):
            # Display P1-3
            display_page("P1-3.png")
            pygame.display.flip()

            # Buttons on P1-3
            p1_3_button1_2 = pygame.Rect(414, 281, 239, 53) # "Play"
            p1_3_button2_2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
            p1_3_button3_2 = pygame.Rect(472, 397, 122, 35) # "Level 2"
            p1_3_button4_2 = pygame.Rect(472, 441, 122, 35) # "Level 3"
            p1_3_click_2 = click4(p1_3_button1_2, p1_3_button2_2, p1_3_button3_2, p1_3_button4_2)

            # Repeating whole game
            if p1_3_click_2 == 1:
                repeat_game4()
            # Repeating level 1, level 2, level 3, and then evil leprechaun
            elif p1_3_click_2 == 2:
                repeat_levels_1_2_3_L()
            # Repeating level 2, level 3, and then evil leprechaun
            elif p1_3_click_2 == 3:
                repeat_levels_2_3_L()
            # Repeating level 3 and then evil leprechaun
            elif p1_3_click_2 == 4:
                repeat_levels_3_L()

# Function for repeating end of game
def repeat_end():
    # Transition to P73
    display_page("P73.png")
    pygame.display.flip()

    # Button on P73
    p73_button1 = pygame.Rect(382, 392, 84, 45) # "Ok"

    # Transition with button to P74
    if click1(p73_button1):
        display_page("P74.png")
        pygame.display.flip()

    # Button on P74
    p74_button1 = pygame.Rect(675, 362, 112, 45) # "Collect"

    # Transition with button to P75
    if click1(p74_button1):
        display_page("P75.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Auto transition from P76 to P82
    page_list6 = ["P76.png", "P77.png", "P78.png", "P79.png", "P80.png",
                "P81.png", "P82.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list6:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(500)

    # Button on P82
    p82_button1 = pygame.Rect(753, 355, 84, 45) # "Ok"

    # Transition with button to P83
    if click1(p82_button1):
        display_page("P83.png")
        pygame.display.flip()

    # Button on P83
    p83_button1 = pygame.Rect(414, 281, 239, 53) # "Play Again"

    # Restart if button is clicked
    if click1(p83_button1):
        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        # Buttons on P1-3
        p1_3_button1_3 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_3 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_3 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_3 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_3 = click4(p1_3_button1_3, p1_3_button2_3, p1_3_button3_3, p1_3_button4_3)

        # Repeating whole game
        if p1_3_click_3 == 1:
            repeat_game5()
        # Repeating level 1 and then level 2
        elif p1_3_click_3 == 2:
            repeat_levels_1_2_3_L_end()
        # Repeating level 2
        elif p1_3_click_3 == 3:
            repeat_levels_2_3_L_end()
        # Repeating
        elif p1_3_click_3 == 4:
            repeat_levels_3_L_end()

# Function for repeating Level 1 and then Level 2
def repeat_levels_1_2():
    # Auto transition from P5 to P9
    # Play Level 1 on P10
    level1()
    pygame.time.delay(150)

    # Auto transition from P11 to P24
    page_list2 = ["P11.png", "P12.png", "P13.png", "P14.png", "P15.png",
                "P16.png", "P17.png", "P18.png", "P19.png", "P20.png",
                "P21.png", "P22.png", "P23.png", "P24.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list2:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P24
    p24_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P25
    if click1(p24_button1):
        display_page("P25.png")
        pygame.display.flip()

    # Buttons on P25
    p25_button1 = pygame.Rect(128, 286, 176, 74) # "Light" - correct
    p25_button2 = pygame.Rect(351, 286, 176, 74) # "Glass" - wrong
    p25_button3 = pygame.Rect(176, 396, 303, 74) # "Rubberband" - wrong
    p25_click = click3(p25_button1, p25_button2, p25_button3)

    # Showing if correct (green) or wrong (red)
    if p25_click == 1:
        display_page("P25-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 2:
        display_page("P25-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 3:
        display_page("P25-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 2 and 3 to P85 then P1-1
    if p25_click == 2 or p25_click == 3:
        # Display P85
        display_page("P85.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-2
        display_page("P1-2.png")
        pygame.display.flip()

        # Buttons on P1-2
        p1_2_button1_1 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_2_button2_1 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_2_button3_1 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_2_click_1 = click3(p1_2_button1_1, p1_2_button2_1, p1_2_button3_1)

        # Repeating whole game
        if p1_2_click_1 == 1:
            repeat_game2()
            return
        # Repeating level 1 and then level 2
        elif p1_2_click_1 == 2:
            repeat_levels_1_2()
            return
        # Repeating level 2
        elif p1_2_click_1 == 3:
            repeat_level2()
            return

    # Transition to P26
    display_page("P26.png")
    pygame.display.flip()

    # Button on P26
    p26_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

    # Transition with button to P27
    if click1(p26_button1):
        display_page("P27.png")
        pygame.display.flip()

    # Repeating level 2
    repeat_level2()

# Function for repeating Level 1, Level 2, and then Level 3
def repeat_levels_1_2_3():
    # Auto transition from P5 to P9
    # Play Level 1 on P10
    level1()
    pygame.time.delay(150)

    # Auto transition from P11 to P24
    page_list2 = ["P11.png", "P12.png", "P13.png", "P14.png", "P15.png",
                "P16.png", "P17.png", "P18.png", "P19.png", "P20.png",
                "P21.png", "P22.png", "P23.png", "P24.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list2:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P24
    p24_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P25
    if click1(p24_button1):
        display_page("P25.png")
        pygame.display.flip()

    # Buttons on P25
    p25_button1 = pygame.Rect(128, 286, 176, 74) # "Light" - correct
    p25_button2 = pygame.Rect(351, 286, 176, 74) # "Glass" - wrong
    p25_button3 = pygame.Rect(176, 396, 303, 74) # "Rubberband" - wrong
    p25_click = click3(p25_button1, p25_button2, p25_button3)

    # Showing if correct (green) or wrong (red)
    if p25_click == 1:
        display_page("P25-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 2:
        display_page("P25-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 3:
        display_page("P25-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 2 and 3 to P85 then P1-1
    if p25_click == 2 or p25_click == 3:
        # Display P85
        display_page("P85.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_1_1 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_1_1 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_1_1 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_1_1 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_1_1 = click4(p1_3_button1_1_1, p1_3_button2_1_1, p1_3_button3_1_1, p1_3_button4_1_1)

        # Repeating whole game
        if p1_3_click_1_1 == 1:
            repeat_game3()
            return
        # Repeating level 1, level 2, and then level 3
        elif p1_3_click_1_1 == 2:
            repeat_levels_1_2_3()
            return
        # Repeating level 2 and then level 3
        elif p1_3_click_1_1 == 3:
            repeat_levels_2_3()
            return
        # Repeating level 3
        elif p1_3_click_1_1 == 4:
            repeat_level3()
            return

    # Transition to P26
    display_page("P26.png")
    pygame.display.flip()

    # Button on P26
    p26_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

    # Transition with button to P27
    if click1(p26_button1):
        display_page("P27.png")
        pygame.display.flip()

    # Repeating level 2 and then level 3
    repeat_levels_2_3()

# Function for repeating Level 2 and then Level 3
def repeat_levels_2_3():
    # Auto transition from P27 to P31
    # Play Level 2 on P32
    level2()
    pygame.time.delay(150)

    # Auto transition from P33 to P46
    page_list4 = ["P33.png", "P34.png", "P35.png", "P36.png", "P37.png",
                "P38.png", "P39.png", "P40.png", "P41.png", "P42.png",
                "P43.png", "P44.png", "P45.png", "P46.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list4:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P46
    p46_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P47
    if click1(p46_button1):
        display_page("P47.png")
        pygame.display.flip()

    # Buttons on P47
    p47_button1 = pygame.Rect(128, 300, 176, 74) # "Food" - wrong
    p47_button2 = pygame.Rect(351, 300, 176, 74) # "Age" - wrong
    p47_button3 = pygame.Rect(176, 410, 303, 74) # "Footsteps" - correct
    p47_click = click3(p47_button1, p47_button2, p47_button3)

    # Showing if correct (green) or wrong (red)
    if p47_click == 1:
        display_page("P47-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p47_click == 2:
        display_page("P47-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p47_click == 3:
        display_page("P47-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 2 to P87 then P1-2
    if p47_click == 1 or p47_click == 2:
        # Display P87
        display_page("P87.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_1_2 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_1_2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_1_2 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_1_2 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_1_2 = click4(p1_3_button1_1_2, p1_3_button2_1_2, p1_3_button3_1_2, p1_3_button4_1_2)

        # Repeating whole game
        if p1_3_click_1_2 == 1:
            repeat_game3()
            return
        # Repeating level 1, level 2, and then level 3
        elif p1_3_click_1_2 == 2:
            repeat_levels_1_2_3()
            return
        # Repeating level 2 and then level 3
        elif p1_3_click_1_2 == 3:
            repeat_levels_2_3()
            return
        # Repeating level 3
        elif p1_3_click_1_2 == 4:
            repeat_level3()
            return

    # Transition to P48
    display_page("P48.png")
    pygame.display.flip()

    # Button on P48
    p48_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

    # Transition with button to P49
    if click1(p48_button1):
        display_page("P49.png")
        pygame.display.flip()
    
    # Repeating level 3
    repeat_level3()

# Function for repeating Level 1, Level 2, Level 3, and then Evil Leprechaun
def repeat_levels_1_2_3_L():
    # Auto transition from P5 to P9
    # Play Level 1 on P10
    level1()
    pygame.time.delay(150)

    # Auto transition from P11 to P24
    page_list2 = ["P11.png", "P12.png", "P13.png", "P14.png", "P15.png",
                "P16.png", "P17.png", "P18.png", "P19.png", "P20.png",
                "P21.png", "P22.png", "P23.png", "P24.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list2:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P24
    p24_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P25
    if click1(p24_button1):
        display_page("P25.png")
        pygame.display.flip()

    # Buttons on P25
    p25_button1 = pygame.Rect(128, 286, 176, 74) # "Light" - correct
    p25_button2 = pygame.Rect(351, 286, 176, 74) # "Glass" - wrong
    p25_button3 = pygame.Rect(176, 396, 303, 74) # "Rubberband" - wrong
    p25_click = click3(p25_button1, p25_button2, p25_button3)

    # Showing if correct (green) or wrong (red)
    if p25_click == 1:
        display_page("P25-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 2:
        display_page("P25-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 3:
        display_page("P25-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 2 and 3 to P85 then P1-1
    if p25_click == 2 or p25_click == 3:
        # Display P85
        display_page("P85.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_2_1 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_2_1 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_2_1 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_2_1 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_2_1 = click4(p1_3_button1_2_1, p1_3_button2_2_1, p1_3_button3_2_1, p1_3_button4_2_1)

        # Repeating whole game
        if p1_3_click_2_1 == 1:
            repeat_game4()
            return
        # Repeating level 1, level 2, level 3, and then evil leprechaun
        elif p1_3_click_2_1 == 2:
            repeat_levels_1_2_3_L()
            return
        # Repeating level 2, level 3, and then evil leprechaun
        elif p1_3_click_2_1 == 3:
            repeat_levels_2_3_L()
            return
        # Repeating level 3 and then evil leprechaun
        elif p1_3_click_2_1 == 4:
            repeat_levels_3_L()
            return

    # Transition to P26
    display_page("P26.png")
    pygame.display.flip()

    # Button on P26
    p26_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

    # Transition with button to P27
    if click1(p26_button1):
        display_page("P27.png")
        pygame.display.flip()

    # Repeating level 2, level 3, and then evil leprechaun
    repeat_levels_2_3_L()

# Function for repeating Level 2, Level 3, and then Evil Leprechaun
def repeat_levels_2_3_L():
    # Auto transition from P27 to P31
    # Play Level 2 on P32
    level2()
    pygame.time.delay(150)

    # Auto transition from P33 to P46
    page_list4 = ["P33.png", "P34.png", "P35.png", "P36.png", "P37.png",
                "P38.png", "P39.png", "P40.png", "P41.png", "P42.png",
                "P43.png", "P44.png", "P45.png", "P46.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list4:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P46
    p46_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P47
    if click1(p46_button1):
        display_page("P47.png")
        pygame.display.flip()

    # Buttons on P47
    p47_button1 = pygame.Rect(128, 300, 176, 74) # "Food" - wrong
    p47_button2 = pygame.Rect(351, 300, 176, 74) # "Age" - wrong
    p47_button3 = pygame.Rect(176, 410, 303, 74) # "Footsteps" - correct
    p47_click = click3(p47_button1, p47_button2, p47_button3)

    # Showing if correct (green) or wrong (red)
    if p47_click == 1:
        display_page("P47-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p47_click == 2:
        display_page("P47-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p47_click == 3:
        display_page("P47-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 2 to P87 then P1-2
    if p47_click == 1 or p47_click == 2:
        # Display P87
        display_page("P87.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_2_2 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_2_2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_2_2 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_2_2 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_2_2 = click4(p1_3_button1_2_2, p1_3_button2_2_2, p1_3_button3_2_2, p1_3_button4_2_2)

        # Repeating whole game
        if p1_3_click_2_2 == 1:
            repeat_game4()
            return
        # Repeating level 1, level 2, level 3, and then evil leprechaun
        elif p1_3_click_2_2 == 2:
            repeat_levels_1_2_3_L()
            return
        # Repeating level 2, level 3, and then evil leprechaun
        elif p1_3_click_2_2 == 3:
            repeat_levels_2_3_L()
            return
        # Repeating level 3 and then evil leprechaun
        elif p1_3_click_2_2 == 4:
            repeat_levels_3_L()
            return

    # Transition to P48
    display_page("P48.png")
    pygame.display.flip()

    # Button on P48
    p48_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

    # Transition with button to P49
    if click1(p48_button1):
        display_page("P49.png")
        pygame.display.flip()
    
    # Repeating level 3 and then evil leprechaun
    repeat_levels_3_L()

# Function for repeating Level 3 and then Evil Leprechaun
def repeat_levels_3_L():
    # Auto transition from P49 to P53
    # Play Level 3 on P54
    level3()
    pygame.time.delay(150)

    # Auto transition from P33 to P46
    page_list5 = ["P55.png", "P56.png", "P57.png", "P58.png", "P59.png",
                "P60.png", "P62.png", "P62.png", "P63.png", "P64.png",
                "P65.png", "P66.png", "P67.png", "P68.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list5:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P68
    p68_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P69
    if click1(p68_button1):
        display_page("P69.png")
        pygame.display.flip()

    # Buttons on P69
    p69_button1 = pygame.Rect(99, 319, 176, 74) # "Rain" - wrong
    p69_button2 = pygame.Rect(298, 319, 258, 74) # "Darkness" - correct
    p69_button3 = pygame.Rect(176, 430, 303, 74) # "Sunlight" - wrong
    p69_click = click3(p69_button1, p69_button2, p69_button3)

    # Showing if correct (green) or wrong (red)
    if p69_click == 1:
        display_page("P69-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p69_click == 2:
        display_page("P69-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p69_click == 3:
        display_page("P69-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 3 to P89 then P1-3
    if p69_click == 1 or p69_click == 3:
        # Display P89
        display_page("P89.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_2_3 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_2_3 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_2_3 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_2_3 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_2_3 = click4(p1_3_button1_2_3, p1_3_button2_2_3, p1_3_button3_2_3, p1_3_button4_2_3)

        # Repeating whole game
        if p1_3_click_2_3 == 1:
            repeat_game4()
            return
        # Repeating level 1, level 2, level 3, and then evil leprechaun
        elif p1_3_click_2_3 == 2:
            repeat_levels_1_2_3_L()
            return
        # Repeating level 2, level 3, and then evil leprechaun
        elif p1_3_click_2_3 == 3:
            repeat_levels_2_3_L()
            return
        # Repeating level 3 and then evil leprechaun
        elif p1_3_click_2_3 == 4:
            repeat_levels_3_L()
            return
    
    # Repeating evil leprechaun
    repeat_leprechaun()

# Function for repeating Level 1, Level 2, Level 3, the Evil Leprechaun, and then end
def repeat_levels_1_2_3_L_end():
    # Auto transition from P5 to P9
    # Play Level 1 on P10
    level1()
    pygame.time.delay(150)

    # Auto transition from P11 to P24
    page_list2 = ["P11.png", "P12.png", "P13.png", "P14.png", "P15.png",
                "P16.png", "P17.png", "P18.png", "P19.png", "P20.png",
                "P21.png", "P22.png", "P23.png", "P24.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list2:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P24
    p24_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P25
    if click1(p24_button1):
        display_page("P25.png")
        pygame.display.flip()

    # Buttons on P25
    p25_button1 = pygame.Rect(128, 286, 176, 74) # "Light" - correct
    p25_button2 = pygame.Rect(351, 286, 176, 74) # "Glass" - wrong
    p25_button3 = pygame.Rect(176, 396, 303, 74) # "Rubberband" - wrong
    p25_click = click3(p25_button1, p25_button2, p25_button3)

    # Showing if correct (green) or wrong (red)
    if p25_click == 1:
        display_page("P25-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 2:
        display_page("P25-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p25_click == 3:
        display_page("P25-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 2 and 3 to P85 then P1-1
    if p25_click == 2 or p25_click == 3:
        # Display P85
        display_page("P85.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_3_1 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_3_1 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_3_1 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_3_1 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_3_1 = click4(p1_3_button1_3_1, p1_3_button2_3_1, p1_3_button3_3_1, p1_3_button4_3_1)

        # Repeating whole game
        if p1_3_click_3_1 == 1:
            repeat_game5()
            return
        # Repeating level 1 and then level 2
        elif p1_3_click_3_1 == 2:
            repeat_levels_1_2_3_L_end()
            return
        # Repeating level 2
        elif p1_3_click_3_1 == 3:
            repeat_levels_2_3_L_end()
            return
        # Repeating
        elif p1_3_click_3_1 == 4:
            repeat_levels_3_L_end()
            return

    # Transition to P26
    display_page("P26.png")
    pygame.display.flip()

    # Button on P26
    p26_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

    # Transition with button to P27
    if click1(p26_button1):
        display_page("P27.png")
        pygame.display.flip()

    # Repeating level 2, level 3, evil leprechaun, and then end
    repeat_levels_2_3_L_end()

# Function for repeating Level 2, Level 3, the Evil Leprechaun, and then end
def repeat_levels_2_3_L_end():
    # Auto transition from P27 to P31
    # Play Level 2 on P32
    level2()
    pygame.time.delay(150)

    # Auto transition from P33 to P46
    page_list4 = ["P33.png", "P34.png", "P35.png", "P36.png", "P37.png",
                "P38.png", "P39.png", "P40.png", "P41.png", "P42.png",
                "P43.png", "P44.png", "P45.png", "P46.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list4:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P46
    p46_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P47
    if click1(p46_button1):
        display_page("P47.png")
        pygame.display.flip()

    # Buttons on P47
    p47_button1 = pygame.Rect(128, 300, 176, 74) # "Food" - wrong
    p47_button2 = pygame.Rect(351, 300, 176, 74) # "Age" - wrong
    p47_button3 = pygame.Rect(176, 410, 303, 74) # "Footsteps" - correct
    p47_click = click3(p47_button1, p47_button2, p47_button3)

    # Showing if correct (green) or wrong (red)
    if p47_click == 1:
        display_page("P47-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p47_click == 2:
        display_page("P47-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p47_click == 3:
        display_page("P47-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 2 to P87 then P1-2
    if p47_click == 1 or p47_click == 2:
        # Display P87
        display_page("P87.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_3_2 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_3_2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_3_2 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_3_2 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_3_2 = click4(p1_3_button1_3_2, p1_3_button2_3_2, p1_3_button3_3_2, p1_3_button4_3_2)

        # Repeating whole game
        if p1_3_click_3_2 == 1:
            repeat_game5()
            return
        # Repeating level 1 and then level 2
        elif p1_3_click_3_2 == 2:
            repeat_levels_1_2_3_L_end()
            return
        # Repeating level 2
        elif p1_3_click_3_2 == 3:
            repeat_levels_2_3_L_end()
            return
        # Repeating
        elif p1_3_click_3_2 == 4:
            repeat_levels_3_L_end()
            return

    # Transition to P48
    display_page("P48.png")
    pygame.display.flip()

    # Button on P48
    p48_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

    # Transition with button to P49
    if click1(p48_button1):
        display_page("P49.png")
        pygame.display.flip()
    
    # Repeating level 3, evil leprechaun, and then end
    repeat_levels_3_L_end()

# Function for repeating Level 3, the Evil Leprechaun, and then end
def repeat_levels_3_L_end():
    # Auto transition from P49 to P53
    # Play Level 3 on P54
    level3()
    pygame.time.delay(150)

    # Auto transition from P33 to P46
    page_list5 = ["P55.png", "P56.png", "P57.png", "P58.png", "P59.png",
                "P60.png", "P62.png", "P62.png", "P63.png", "P64.png",
                "P65.png", "P66.png", "P67.png", "P68.png"]

    # Looping through the list and displing each image with a delay
    for page in page_list5:
        display_page(page)
        pygame.display.flip()
        pygame.time.delay(150)

    # Button on P68
    p68_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

    # Transition with button to P69
    if click1(p68_button1):
        display_page("P69.png")
        pygame.display.flip()

    # Buttons on P69
    p69_button1 = pygame.Rect(99, 319, 176, 74) # "Rain" - wrong
    p69_button2 = pygame.Rect(298, 319, 258, 74) # "Darkness" - correct
    p69_button3 = pygame.Rect(176, 430, 303, 74) # "Sunlight" - wrong
    p69_click = click3(p69_button1, p69_button2, p69_button3)

    # Showing if correct (green) or wrong (red)
    if p69_click == 1:
        display_page("P69-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p69_click == 2:
        display_page("P69-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p69_click == 3:
        display_page("P69-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 3 to P89 then P1-3
    if p69_click == 1 or p69_click == 3:
        # Display P89
        display_page("P89.png")
        pygame.display.flip()
        pygame.time.delay(1500)

        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_3_3 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_3_3 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_3_3 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_3_3 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_3_3 = click4(p1_3_button1_3_3, p1_3_button2_3_3, p1_3_button3_3_3, p1_3_button4_3_3)

        # Repeating whole game
        if p1_3_click_3_3 == 1:
            repeat_game5()
            return
        # Repeating level 1 and then level 2
        elif p1_3_click_3_3 == 2:
            repeat_levels_1_2_3_L_end()
            return
        # Repeating level 2
        elif p1_3_click_3_3 == 3:
            repeat_levels_2_3_L_end()
            return
        # Repeating
        elif p1_3_click_3_3 == 4:
            repeat_levels_3_L_end()
            return
    
    # Repeating evil leprechaun and end
    repeat_levels_L_end()

# Function for repeating the Evil Leprechaun and then end
def repeat_levels_L_end():
    # Transition to P70
    display_page("P70.png")
    pygame.display.flip()

    # Button on P70
    p70_button1 = pygame.Rect(454, 370, 84, 45) # "Go"

    # Transition with button to P71
    if click1(p70_button1):
        display_page("P71.png")
        pygame.display.flip()

    # Button on P71
    p71_button1 = pygame.Rect(382, 392, 84, 45) # "Ok"

    # Transition with button to P50
    if click1(p71_button1):
        display_page("P72.png")
        pygame.display.flip()

    # Buttons on P72
    p72_button1 = pygame.Rect(128, 319, 176, 74) # "Coins" - wrong
    p72_button2 = pygame.Rect(351, 319, 176, 74) # "Time" - wrong
    p72_button3 = pygame.Rect(176, 430, 303, 74) # "Secret" - correct
    p72_click = click3(p72_button1, p72_button2, p72_button3)

    # Showing if correct (green) or wrong (red)
    if p72_click == 1:
        display_page("P72-1.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p72_click == 2:
        display_page("P72-2.png")
        pygame.display.flip()
        pygame.time.delay(500)
    elif p72_click == 3:
        display_page("P72-3.png")
        pygame.display.flip()
        pygame.time.delay(500)

    # Transition with button 1 and 2 to P90
    if p72_click == 1 or p72_click == 2:
        display_page("P90.png")
        pygame.display.flip()

        # Button on P90
        p64_button1 = pygame.Rect(414, 324, 239, 53) # "Restart"

        # Transition with button to P1-3
        if click1(p64_button1):
            # Display P1-3
            display_page("P1-3.png")
            pygame.display.flip()

            # Buttons on P1-3
            p1_3_button1_3_4 = pygame.Rect(414, 281, 239, 53) # "Play"
            p1_3_button2_3_4 = pygame.Rect(472, 352, 122, 35) # "Level 1"
            p1_3_button3_3_4 = pygame.Rect(472, 397, 122, 35) # "Level 2"
            p1_3_button4_3_4 = pygame.Rect(472, 441, 122, 35) # "Level 3"
            p1_3_click_3_4 = click4(p1_3_button1_3_4, p1_3_button2_3_4, p1_3_button3_3_4, p1_3_button4_3_4)

            # Repeating whole game
            if p1_3_click_3_4 == 1:
                repeat_game5()
                return
            # Repeating level 1 and then level 2
            elif p1_3_click_3_4 == 2:
                repeat_levels_1_2_3_L_end()
                return
            # Repeating level 2
            elif p1_3_click_3_4 == 3:
                repeat_levels_2_3_L_end()
                return
            # Repeating
            elif p1_3_click_3_4 == 4:
                repeat_levels_3_L_end()
                return
    
    # Repeating end
    repeat_end()

# Function for repeating everything until Level 1
def repeat_game1():
    # Repeating start
    repeat_start()

    # Repeating level 1
    repeat_level1()

# Function for repeating everything until Level 2
def repeat_game2():
    # Repeating start
    repeat_start()

    # Repeating level 1 and then level 2
    repeat_levels_1_2()

# Function for repeating everything until Level 3
def repeat_game3():
    # Repeating start
    repeat_start()

    # Repeating level 1, level 2, and then level 3
    repeat_levels_1_2_3()

# Function for repeating everything until Evil Leprechaun
def repeat_game4():
    # Repeating start
    repeat_start()

    # Repeating level 1, level 2, level 3, and then evil leprechaun
    repeat_levels_1_2_3_L()

# Function for repeating everything with all levels open
def repeat_game5():
    # Repeating start
    repeat_start()

    # Repeating level 1, level 2, level 3, evil leprechaun, and then end
    repeat_levels_1_2_3_L_end()

# GAME
# Display P1
display_page("P1.png")
pygame.display.flip()

# Button on P1
p1_button1 = pygame.Rect(414, 281, 239, 53) # "Play"

# Transition with button to P2
if click1(p1_button1):
    display_page("P2.png")
    pygame.display.flip()

# Buttons on P2
p2_button1 = pygame.Rect(328, 393, 84, 45) # "Yes"
p2_button2 = pygame.Rect(909, 531, 124, 53) # "Skip"
p2_click = click2(p2_button1, p2_button2)

# Transition with button 1 to P3
if p2_click == 1:
    display_page("P3.png")
    pygame.display.flip()

    # Button on P3
    p3_button1 = pygame.Rect(328, 393, 84, 45) # "Ok"
    
    # Transition with button to P4
    if click1(p3_button1):
        display_page("P4.png")
        pygame.display.flip()

        # Button on P4
        p4_button1 = pygame.Rect(328, 393, 84, 45) # "Start"
        
        # Transition with button to P5
        if click1(p4_button1):
            display_page("P5.png")
            pygame.display.flip()

# Transition with button 2 to P5
elif p2_click == 2:
    display_page("P5.png")
    pygame.display.flip()

# Auto transition from P5 to P9
# Play Level 1 on P10
level1()
pygame.time.delay(150)

# Auto transition from P11 to P24
page_list2 = ["P11.png", "P12.png", "P13.png", "P14.png", "P15.png",
            "P16.png", "P17.png", "P18.png", "P19.png", "P20.png",
            "P21.png", "P22.png", "P23.png", "P24.png"]

# Looping through the list and displing each image with a delay
for page in page_list2:
    display_page(page)
    pygame.display.flip()
    pygame.time.delay(150)

# Button on P24
p24_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

# Transition with button to P25
if click1(p24_button1):
    display_page("P25.png")
    pygame.display.flip()

# Buttons on P25
p25_button1 = pygame.Rect(128, 286, 176, 74) # "Light" - correct
p25_button2 = pygame.Rect(351, 286, 176, 74) # "Glass" - wrong
p25_button3 = pygame.Rect(176, 396, 303, 74) # "Rubberband" - wrong
p25_click = click3(p25_button1, p25_button2, p25_button3)

# Showing if correct (green) or wrong (red)
if p25_click == 1:
    display_page("P25-1.png")
    pygame.display.flip()
    pygame.time.delay(500)
elif p25_click == 2:
    display_page("P25-2.png")
    pygame.display.flip()
    pygame.time.delay(500)
elif p25_click == 3:
    display_page("P25-3.png")
    pygame.display.flip()
    pygame.time.delay(500)

# Transition with button 2 and 3 to P85 then P1-1
if p25_click == 2 or p25_click == 3:
    # Display P85
    display_page("P85.png")
    pygame.display.flip()
    pygame.time.delay(1500)

    # Display P1-1
    display_page("P1-1.png")
    pygame.display.flip()

    # Buttons on P1-1
    p1_1_button1 = pygame.Rect(414, 281, 239, 53) # "Play"
    p1_1_button2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
    p1_1_click = click2(p1_1_button1, p1_1_button2)

    # Repeating whole game
    if p1_1_click == 1:
        repeat_game1()
    # Repeating level 1
    elif p1_1_click == 2:
        repeat_level1()

# Transition to P26
display_page("P26.png")
pygame.display.flip()

# Button on P26
p26_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

# Transition with button to P27
if click1(p26_button1):
    display_page("P27.png")
    pygame.display.flip()

# Auto transition from P27 to P31
# Play Level 2 on P32
level2()
pygame.time.delay(150)

# Auto transition from P33 to P46
page_list4 = ["P33.png", "P34.png", "P35.png", "P36.png", "P37.png",
            "P38.png", "P39.png", "P40.png", "P41.png", "P42.png",
            "P43.png", "P44.png", "P45.png", "P46.png"]

# Looping through the list and displing each image with a delay
for page in page_list4:
    display_page(page)
    pygame.display.flip()
    pygame.time.delay(150)

# Button on P46
p46_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

# Transition with button to P47
if click1(p46_button1):
    display_page("P47.png")
    pygame.display.flip()

# Buttons on P47
p47_button1 = pygame.Rect(128, 300, 176, 74) # "Food" - wrong
p47_button2 = pygame.Rect(351, 300, 176, 74) # "Age" - wrong
p47_button3 = pygame.Rect(176, 410, 303, 74) # "Footsteps" - correct
p47_click = click3(p47_button1, p47_button2, p47_button3)

# Showing if correct (green) or wrong (red)
if p47_click == 1:
    display_page("P47-1.png")
    pygame.display.flip()
    pygame.time.delay(500)
elif p47_click == 2:
    display_page("P47-2.png")
    pygame.display.flip()
    pygame.time.delay(500)
elif p47_click == 3:
    display_page("P47-3.png")
    pygame.display.flip()
    pygame.time.delay(500)

# Transition with button 1 and 2 to P87 then P1-2
if p47_click == 1 or p47_click == 2:
    # Display P87
    display_page("P87.png")
    pygame.display.flip()
    pygame.time.delay(1500)

    # Display P1-2
    display_page("P1-2.png")
    pygame.display.flip()

    # Buttons on P1-2
    p1_2_button1 = pygame.Rect(414, 281, 239, 53) # "Play"
    p1_2_button2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
    p1_2_button3 = pygame.Rect(472, 397, 122, 35) # "Level 2"
    p1_2_click = click3(p1_2_button1, p1_2_button2, p1_2_button3)

    # Repeating whole game
    if p1_2_click == 1:
        repeat_game2()
    # Repeating level 1 and then level 2
    elif p1_2_click == 2:
        repeat_levels_1_2()
    # Repeating level 2
    elif p1_2_click == 3:
        repeat_level2()

# Transition to P48
display_page("P48.png")
pygame.display.flip()

# Button on P48
p48_button1 = pygame.Rect(454, 370, 84, 45) # "Start"

# Transition with button to P49
if click1(p48_button1):
    display_page("P49.png")
    pygame.display.flip()

# Auto transition from P49 to P53
# Play Level 3 on P54
level3()
pygame.time.delay(150)

# Auto transition from P33 to P46
page_list5 = ["P55.png", "P56.png", "P57.png", "P58.png", "P59.png",
            "P60.png", "P62.png", "P62.png", "P63.png", "P64.png",
            "P65.png", "P66.png", "P67.png", "P68.png"]

# Looping through the list and displing each image with a delay
for page in page_list5:
    display_page(page)
    pygame.display.flip()
    pygame.time.delay(150)

# Button on P68
p68_button1 = pygame.Rect(454, 370, 84, 45) # "Ok"

# Transition with button to P69
if click1(p68_button1):
    display_page("P69.png")
    pygame.display.flip()

# Buttons on P69
p69_button1 = pygame.Rect(99, 319, 176, 74) # "Rain" - wrong
p69_button2 = pygame.Rect(298, 319, 258, 74) # "Darkness" - correct
p69_button3 = pygame.Rect(176, 430, 303, 74) # "Sunlight" - wrong
p69_click = click3(p69_button1, p69_button2, p69_button3)

# Showing if correct (green) or wrong (red)
if p69_click == 1:
    display_page("P69-1.png")
    pygame.display.flip()
    pygame.time.delay(500)
elif p69_click == 2:
    display_page("P69-2.png")
    pygame.display.flip()
    pygame.time.delay(500)
elif p69_click == 3:
    display_page("P69-3.png")
    pygame.display.flip()
    pygame.time.delay(500)

# Transition with button 1 and 3 to P89 then P1-3
if p69_click == 1 or p69_click == 3:
    # Display P89
    display_page("P89.png")
    pygame.display.flip()
    pygame.time.delay(1500)

    # Display P1-3
    display_page("P1-3.png")
    pygame.display.flip()

    # Buttons on P1-3
    p1_3_button1_1 = pygame.Rect(414, 281, 239, 53) # "Play"
    p1_3_button2_1 = pygame.Rect(472, 352, 122, 35) # "Level 1"
    p1_3_button3_1 = pygame.Rect(472, 397, 122, 35) # "Level 2"
    p1_3_button4_1 = pygame.Rect(472, 441, 122, 35) # "Level 3"
    p1_3_click_1 = click4(p1_3_button1_1, p1_3_button2_1, p1_3_button3_1, p1_3_button4_1)

    # Repeating whole game
    if p1_3_click_1 == 1:
        repeat_game3()
    # Repeating level 1, level 2, and then level 3
    elif p1_3_click_1 == 2:
        repeat_levels_1_2_3()
    # Repeating level 2 and then level 3
    elif p1_3_click_1 == 3:
        repeat_levels_2_3()
    # Repeating level 3
    elif p1_3_click_1 == 4:
        repeat_level3()

# Transition to P70
display_page("P70.png")
pygame.display.flip()

# Button on P70
p70_button1 = pygame.Rect(454, 370, 84, 45) # "Go"

# Transition with button to P71
if click1(p70_button1):
    display_page("P71.png")
    pygame.display.flip()

# Button on P71
p71_button1 = pygame.Rect(382, 392, 84, 45) # "Ok"

# Transition with button to P50
if click1(p71_button1):
    display_page("P72.png")
    pygame.display.flip()

# Buttons on P72
p72_button1 = pygame.Rect(128, 319, 176, 74) # "Coins" - wrong
p72_button2 = pygame.Rect(351, 319, 176, 74) # "Time" - wrong
p72_button3 = pygame.Rect(176, 430, 303, 74) # "Secret" - correct
p72_click = click3(p72_button1, p72_button2, p72_button3)

# Showing if correct (green) or wrong (red)
if p72_click == 1:
    display_page("P72-1.png")
    pygame.display.flip()
    pygame.time.delay(500)
elif p72_click == 2:
    display_page("P72-2.png")
    pygame.display.flip()
    pygame.time.delay(500)
elif p72_click == 3:
    display_page("P72-3.png")
    pygame.display.flip()
    pygame.time.delay(500)

# Transition with button 1 and 2 to P90
if p72_click == 1 or p72_click == 2:
    display_page("P90.png")
    pygame.display.flip()

    # Button on P90
    p64_button1 = pygame.Rect(414, 324, 239, 53) # "Restart"

    # Transition with button to P1-3
    if click1(p64_button1):
        # Display P1-3
        display_page("P1-3.png")
        pygame.display.flip()

        # Buttons on P1-3
        p1_3_button1_2 = pygame.Rect(414, 281, 239, 53) # "Play"
        p1_3_button2_2 = pygame.Rect(472, 352, 122, 35) # "Level 1"
        p1_3_button3_2 = pygame.Rect(472, 397, 122, 35) # "Level 2"
        p1_3_button4_2 = pygame.Rect(472, 441, 122, 35) # "Level 3"
        p1_3_click_2 = click4(p1_3_button1_2, p1_3_button2_2, p1_3_button3_2, p1_3_button4_2)

        # Repeating whole game
        if p1_3_click_2 == 1:
            repeat_game4()
        # Repeating level 1, level 2, level 3, and then evil leprechaun
        elif p1_3_click_2 == 2:
            repeat_levels_1_2_3_L()
        # Repeating level 2, level 3, and then evil leprechaun
        elif p1_3_click_2 == 3:
            repeat_levels_2_3_L()
        # Repeating level 3 and then evil leprechaun
        elif p1_3_click_2 == 4:
            repeat_levels_3_L()

# Transition to P73
display_page("P73.png")
pygame.display.flip()

# Button on P73
p73_button1 = pygame.Rect(382, 392, 84, 45) # "Ok"

# Transition with button to P74
if click1(p73_button1):
    display_page("P74.png")
    pygame.display.flip()

# Button on P74
p74_button1 = pygame.Rect(675, 362, 112, 45) # "Collect"

# Transition with button to P75
if click1(p74_button1):
    display_page("P75.png")
    pygame.display.flip()
    pygame.time.delay(500)

# Auto transition from P76 to P82
page_list6 = ["P76.png", "P77.png", "P78.png", "P79.png", "P80.png",
            "P81.png", "P82.png"]

# Looping through the list and displing each image with a delay
for page in page_list6:
    display_page(page)
    pygame.display.flip()
    pygame.time.delay(500)

# Button on P82
p82_button1 = pygame.Rect(753, 355, 84, 45) # "Ok"

# Transition with button to P83
if click1(p82_button1):
    display_page("P83.png")
    pygame.display.flip()

# Button on P83
p83_button1 = pygame.Rect(414, 281, 239, 53) # "Play Again"

# Restart if button is clicked
if click1(p83_button1):
    # Display P1-3
    display_page("P1-3.png")
    pygame.display.flip()

    # Buttons on P1-3
    # Buttons on P1-3
    p1_3_button1_3 = pygame.Rect(414, 281, 239, 53) # "Play"
    p1_3_button2_3 = pygame.Rect(472, 352, 122, 35) # "Level 1"
    p1_3_button3_3 = pygame.Rect(472, 397, 122, 35) # "Level 2"
    p1_3_button4_3 = pygame.Rect(472, 441, 122, 35) # "Level 3"
    p1_3_click_3 = click4(p1_3_button1_3, p1_3_button2_3, p1_3_button3_3, p1_3_button4_3)

    # Repeating whole game
    if p1_3_click_3 == 1:
        repeat_game5()
    # Repeating level 1 and then level 2
    elif p1_3_click_3 == 2:
        repeat_levels_1_2_3_L_end()
    # Repeating level 2
    elif p1_3_click_3 == 3:
        repeat_levels_2_3_L_end()
    # Repeating
    elif p1_3_click_3 == 4:
        repeat_levels_3_L_end()

# Looping the game
async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Updating the display
        pygame.display.flip()
        await asyncio.sleep(0)




asyncio.run(main())
# Quitting
pygame.quit()
sys.exit()



