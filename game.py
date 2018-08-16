import pygame

pygame.init()

# height and width of game window for now
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Gobbo Hunt')  # game title

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

dead = False

MonsterImg = pygame.image.load('goblin.jpg')


def monster(x,y):
    gameDisplay.blit(MonsterImg, (x,y))  #draws image on screen


x = (display_width * 0.45)
y = (display_height * 0.8)

while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    gameDisplay.fill(white)
    monster(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
