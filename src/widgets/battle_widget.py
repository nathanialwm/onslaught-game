import pygame
from data.constants import Fonts, Colors


class BattleWidget:
    """
    Widget for displaying battle information including player stats, enemy stats, and battle summary.

    Layout:
    - Left section: Player stats (left-aligned)
    - Center section: Battle summary (center-aligned)
    - Right section: Enemy stats (right-aligned)
    """

    def __init__(self, screen, player_x, enemy_x, y, player_width, enemy_width, summary_width, **kwargs):
        """
        Initialize the BattleWidget.

        Args:
            screen: Pygame screen surface
            player_x: X position for player stats section (left edge)
            enemy_x: X position for enemy stats section (left edge)
            y: Y position for the top of the widget
            player_width: Width of player stats section
            enemy_width: Width of enemy stats section
            summary_width: Width of battle summary section
            **kwargs: Optional styling parameters:
                - font: Font to use (default: SyneMono size 24)
                - text_color: Color for text (default: PRIMARY_TEXT)
                - line_spacing: Space between lines in pixels (default: 25)
        """
        self.screen = screen
        self.player_x = player_x
        self.enemy_x = enemy_x
        self.y = y
        self.player_width = player_width
        self.enemy_width = enemy_width
        self.summary_width = summary_width

        # Styling parameters
        self.font = kwargs.get("font", pygame.font.Font(Fonts.MAIN_FONT, 26))
        self.summary_font = kwargs.get("font", pygame.font.Font(Fonts.MAIN_FONT, 20))
        self.text_color = kwargs.get("text_color", Colors.PRIMARY_TEXT)
        self.line_spacing = kwargs.get("line_spacing", 28)
        self.summary_line_spacing = kwargs.get("line_spacing", 24)

        # Calculate center X for summary (midpoint between player and enemy sections)
        self.summary_x = player_x + player_width + (enemy_x - (player_x + player_width)) // 2

    def draw(self, player_stats=None, enemy_stats=None, battle_summary=None):
        """
        Draw the battle widget with dynamic content.

        Args:
            player_stats: List of strings to display as player stats (e.g., ["Attack: 10", "Defense: 5"])
            enemy_stats: List of strings to display as enemy stats
            battle_summary: List of strings to display as battle summary (e.g., ["Victory!", "EXP: +50", "Gold: +20"])
        """
        if player_stats is None:
            player_stats = []
        if enemy_stats is None:
            enemy_stats = []
        if battle_summary is None:
            battle_summary = []

        # Draw player stats (left-aligned)
        self._draw_player_stats(player_stats)

        # Draw enemy stats (right-aligned)
        self._draw_enemy_stats(enemy_stats)

        # Draw battle summary (center-aligned)
        self._draw_battle_summary(battle_summary)

    def _draw_player_stats(self, stats):
        """Draw player stats left-aligned."""
        current_y = self.y

        for stat in stats:
            text_surface = self.font.render(stat, True, self.text_color)
            self.screen.blit(text_surface, (self.player_x, current_y))
            current_y += self.line_spacing

    def _draw_enemy_stats(self, stats):
        """Draw enemy stats right-aligned."""
        current_y = self.y

        for stat in stats:
            text_surface = self.font.render(stat, True, self.text_color)
            text_rect = text_surface.get_rect()
            # Right-align within the enemy section
            text_x = self.enemy_x + self.enemy_width - text_rect.width
            self.screen.blit(text_surface, (text_x, current_y))
            current_y += self.line_spacing

    def _draw_battle_summary(self, summary):
        """Draw battle summary center-aligned."""
        current_y = self.y

        for line in summary:
            text_surface = self.summary_font.render(line, True, self.text_color)
            text_rect = text_surface.get_rect()
            # Center-align the text
            text_x = self.summary_x - text_rect.width // 2
            self.screen.blit(text_surface, (text_x, current_y))
            current_y += self.summary_line_spacing
