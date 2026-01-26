import pygame
from widgets.dropdown import ScrollableDropdown
from data.constants import Colors, Fonts
from widgets.health_bar import HealthBar
from data.player import Player
from data.enemy import Enemy
class Draw:
    def __init__(self, screen):
        self.screen = screen

    def draw_enemy_dropdown(self, enemies):
        enemy_names = [enemy.name for enemy in enemies]
        dropdown = ScrollableDropdown(
            self.screen, 620, 40, 220, 36,
            name="Select Enemy",
            choices=enemy_names,
            font=self.set_font(Fonts.MAIN_FONT, 24),
            max_height=300,
            borderRadius=3,
            borderColour=Colors.PRIMARY_TEXT,
            borderThickness=2,
            textColour=Colors.PRIMARY_TEXT,
            hoverColour=Colors.DROPDOWN_BG,
            selectedColour=Colors.DROPDOWN_BG,
            inactiveColour=Colors.TAN_BG
        )
        return dropdown

    def set_font(self, font_string, size):
        return pygame.font.Font(font_string, size)

    # Draw the entire main battle section
    def draw_battle_section(self, enemy, player):
        self._draw_portraits(enemy.portrait)
        self._draw_health_bars(enemy, player)
        self._draw_battle_names(enemy.name)

    #Draw the portraits of the player and enemy
    def _draw_portraits(self, enemy_portrait):
        # Define enemy portrait
        enemy_portrait_loaded = pygame.image.load(enemy_portrait)
        enemy_portrait = pygame.transform.scale(enemy_portrait_loaded, (120, 120))
        # Define player portrait
        player_portrait = pygame.image.load("../assets/images/placeholder.png")
        player_portrait = pygame.transform.scale(player_portrait, (120, 120))
        # Render to screen
        self.screen.blit(player_portrait, (230, 240))
        self.screen.blit(enemy_portrait, (800, 240))
    
    # Draw health bars for player and enemy
    def _draw_health_bars(self, enemy, player):
        player_healthbar = HealthBar(
            self.screen, 230, 370, 420, 20,
            fill_color=Colors.HEALTH_GREEN
        )
        enemy_healthbar = HealthBar(
            self.screen, 820, 370, 420, 20,
            fill_color=Colors.HEALTH_RED
        )

        player_healthbar.draw(current_health=player.temp_health, max_health=player.health)  
        enemy_healthbar.draw(current_health=enemy.temp_health, max_health=enemy.health)

    def _draw_battle_names(self, enemy_name):
        font = self.set_font(Fonts.MAIN_FONT, 40)
        # Player name
        player_name_surf = font.render("Player", True, Colors.PRIMARY_TEXT)
        self.screen.blit(player_name_surf, (380, 315))
        # Enemy name
        enemy_name_surf = font.render(enemy_name, True, Colors.PRIMARY_TEXT)
        self.screen.blit(enemy_name_surf, (950, 315))

    def draw_placeholder_menu(self):
        placeholder_menu = pygame.Rect(0, 0, 180, 720)
        pygame.draw.rect(self.screen, Colors.DROPDOWN_BG, placeholder_menu)