import pygame
import argparse
from utils.logger import setup_logger
from draw import Draw
from data.enemy import Enemy
from data.player import Player
from data.constants import Colors, Config
from logic.battle import Battle

# Argument parser for developer mode
if Config.DEV_MODE_AVAILABLE:
    argparser = argparse.ArgumentParser(description="Onslaught Game")
    argparser.add_argument("--dev", action="store_true", help="Enable developer mode with extra features")

# Setup logger
logger = setup_logger(Config.DEV_MODE_AVAILABLE)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Onslaught")
clock = pygame.time.Clock()
running = True

PLAYER_ATTACK = pygame.event.custom_type()
ENEMY_ATTACK = pygame.event.custom_type()
BATTLE_EVENT = pygame.event.custom_type()
pygame.time.set_timer(BATTLE_EVENT, 6000)

# Generate enemies and create enemy dropdown
draw = Draw(screen)
dropdown = draw.draw_enemy_dropdown(Enemy.get_all())
# initialize battle widget
battle_widget = draw.init_battle_widget()

selected_enemy = dropdown.set_selected("Mouse")

# initialize player and enemy
player_instance = Player(name="Hero")
pygame.time.set_timer(PLAYER_ATTACK, int(player_instance.attack_speed * 1000))

pygame.time.set_timer(ENEMY_ATTACK, int(2000))
#Game loop
while running:
    screen.fill(Colors.TAN_BG)
    # poll for events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: #click X to close window
            running = False
        elif event.type == PLAYER_ATTACK:
            battle.player_attack(PLAYER_ATTACK)
            print(f"player attacked for {player_instance.attack}")
        elif event.type == ENEMY_ATTACK:
            battle.enemy_attack(ENEMY_ATTACK)
            print(f"enemy attacked for {selected_enemy.attack}")
        # if event.type == BATTLE_EVENT:
            

    # fill the screen with a color to wipe away anything from last frame

    # Handle dropdown events and draw
    dropdown.handle_events(events)
    dropdown.draw()

    #draw battle widget
    draw.draw_placeholder_menu()
    # Look up the full Enemy object from the selected name
    selected_enemy = Enemy.get_by_name(dropdown.get_selected())
    if selected_enemy:
        battle = Battle(player_instance, selected_enemy)
        battle.battle_sequence()

        draw.draw_battle_section(selected_enemy, player_instance)
        draw.draw_battle_widget_text(battle_widget, selected_enemy, player_instance)

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
