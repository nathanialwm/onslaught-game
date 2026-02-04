import logging
import pygame

logger = logging.getLogger("onslaught_logs")
class HealthBar:
    def __init__(self, screen, x, y, width, height, fill_color, background_color=(50, 50, 50)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill_color = fill_color
        self.background_color = background_color

    def draw(self, current_health, max_health):
        """Draw the health bar based on current vs max health."""
        # Calculate fill width based on health percentage
        if max_health <= 0:
            fill_ratio = 0
        else:
            fill_ratio = max(0, min(1, current_health / max_health))

        fill_width = int(self.width * fill_ratio)

        # Draw background (empty portion)
        background_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.background_color, background_rect)

        # Draw fill (current health)
        if fill_width > 0:
            fill_rect = pygame.Rect(self.x, self.y, fill_width, self.height)
            pygame.draw.rect(self.screen, self.fill_color, fill_rect)
