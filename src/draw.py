import pygame
from src.widgets.dropdown import ScrollableDropdown
from constants import Colors, Fonts


class Draw:
    def __init__(self, screen):
        self.screen = screen

    def draw_enemy_dropdown(self, enemies):
        enemy_names = [enemy.name for enemy in enemies]
        dropdown = ScrollableDropdown(
            self.screen, 540, 40, 200, 32,
            name="Select Enemy",
            choices=enemy_names,
            font=self.set_font(Fonts.MAIN_FONT, 24),
            max_height=300,
            borderRadius=3,
            borderColour=Colors.PRIMARY_TEXT,
            borderThickness=2,
            textColour=Colors.PRIMARY_TEXT,
            hoverColour=(100, 100, 100),
            pressedColour=(50, 50, 50),
            inactiveColour=Colors.TAN_BG
        )
        return dropdown

    def set_font(self, font_string, size):
        return pygame.font.Font(font_string, size)
