# Import Neccesary Libraries
import pygame
# Initialize required modules
pygame.init()
# Setup window geometry
screen = pygame.display.set_mode((400,500))
# Create a loop to run till the game is quit by the user
done = False
while not done:
        # clear the event queue
        for event in pygame.event.get():
                if event.type== pygame.QUIT:
                        pygame.quit()
        # Make the changes visibe
        pygame.display.flip

