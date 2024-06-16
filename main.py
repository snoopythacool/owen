import pygame
from scenes import game, menu

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = SCREEN_WIDTH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Owen")

scenes = {}
scenes[game.SCENE_ID] = game.loop
scenes[menu.SCENE_ID] = menu.loop
currentscene = "menu"

run = True
while run:

    currentscene = scenes[currentscene]()

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False

pygame.quit()