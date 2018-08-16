import pygame
from pygame.locals import *
pygame.init()


def startscreen():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Gobbo Hunt')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to Gobbo Hunt", 1, (255, 255, 255))
    textpos = text.get_rect(center=(400, 150))
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

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


if __name__ == '__main__': startscreen()
