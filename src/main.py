import pygame
from draw import Draw
from data.enemy import Enemy
from data.player import Player
from data.constants import Colors
from logic.battle import Battle

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Onslaught")
clock = pygame.time.Clock()
running = True

# Generate enemies and create enemy dropdown
draw = Draw(screen)
dropdown = draw.draw_enemy_dropdown(Enemy.get_all())
dropdown.set_selected("Mouse")

player_instance = Player(name="Hero")

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

    #draw battle widget

    draw.draw_placeholder_menu()
    # Look up the full Enemy object from the selected name
    selected_enemy = Enemy.get_by_name(dropdown.get_selected())
    if selected_enemy:
        battle = Battle(player_instance, selected_enemy)
        battle.start(screen)
        draw.draw_battle_section(selected_enemy, player_instance)
        battle.draw()

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
