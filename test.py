import pygame
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')


# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value
# for white, green,
# blue, black, red
# colour respectively.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

# assigning values to X and Y variable
X = 600
Y = 600

# create the display surface object
# of specific dimension..e(X,Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Window')

# completely fill the surface object
# with white colour
display_surface.fill(white)

# draw a circle using draw.circle()
# method of pygame.
# pygame.draw.circle(surface, color,
# center point, radius, thickness)
for i in range(6):
    pygame.draw.circle(display_surface,
                       black, (30, 50), 30, 0)


# infinite loop
while True:

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        pygame.display.update()
