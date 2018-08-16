# Third Party Modules
import pygame
from pygame.locals import *

# Our Modules
import constants

pygame.init()


def startscreen():
    screen = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
    pygame.display.set_caption(constants.GAME_TITLE)

    background = pygame.image.load('Data/Images/gobbo_base.png')
    text_title = pygame.image.load('Data/Images/game_title.png')

    spacebar_font = pygame.font.Font(None, 25)

    text_spacebar = spacebar_font.render("Press Spacebar to enter the land of Gobbos!", 1, constants.STARTSCREEN_SPACEBAR_COLOR)
    text_spacebarpos = text_spacebar.get_rect(center=(constants.DISPLAY_WIDTH/2, constants.DISPLAY_HEIGHT/1.2))

    background.blit(text_spacebar, text_spacebarpos)

    screen.blit(background, (0, 0))
    screen.blit(text_title, (200, 100))
    pygame.display.flip()

    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main()


def main():
    screen = pygame.display.set_mode((800, 600))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Main Game", 1, (255, 255, 255))
    textpos = text.get_rect(center=(400, 150))
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    startscreen()
    main()
