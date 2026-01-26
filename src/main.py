# Example file showing a basic pygame "game loop"
import pygame
from draw import Draw
from data.enemy import Enemy
from data.player import Player
from data.enemy_list import EnemyList
from src.data.constants import Colors

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Onslaught")
clock = pygame.time.Clock()
running = True

# Generate enemies and create enemy dropdown
list_of_enemies = EnemyList.generate_enemies()
draw = Draw(screen)
dropdown = draw.draw_enemy_dropdown(list_of_enemies)
dropdown.set_selected("Mouse")

#Game loop
while running:
    # poll for events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: #click X to close window
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(Colors.TAN_BG)

    # Handle dropdown events and draw
    dropdown.handle_events(events)
    dropdown.draw()

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
