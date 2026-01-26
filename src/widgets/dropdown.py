import pygame

class ScrollableDropdown:
    def __init__(self, screen, x, y, width, height, name, choices, **kwargs):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.item_height = height
        self.name = name
        self.choices = choices
        self.max_dropdown_height = kwargs.get('max_height', 300)

        # State
        self.dropped = False
        self.selected = None
        self.selected_index = -1
        self.scroll_offset = 0
        self.hovered_index = -1

        # Drag scrolling state
        self.dragging = False
        self.drag_start_y = 0
        self.drag_start_scroll = 0

        # Styling
        self.font = kwargs.get('font', pygame.font.SysFont('sans-serif', 20))
        self.text_color = kwargs.get('textColour', (0, 0, 0))
        self.bg_color = kwargs.get('inactiveColour', (150, 150, 150))
        self.hover_color = kwargs.get('hoverColour', (125, 125, 125))
        self.pressed_color = kwargs.get('pressedColour', (100, 100, 100))
        self.selected_color = kwargs.get('selectedColour', (80, 80, 80))
        self.border_color = kwargs.get('borderColour', (0, 0, 0))
        self.border_width = kwargs.get('borderThickness', 2)
        self.border_radius = kwargs.get('borderRadius', 0)

    def get_total_list_height(self):
        """Total height of all choices"""
        return len(self.choices) * self.item_height

    def get_visible_height(self):
        """Height of visible dropdown area (capped at max)"""
        return min(self.get_total_list_height(), self.max_dropdown_height)

    def get_scroll_range(self):
        """Get min and max scroll offsets - allows scrolling entire list through view"""
        if self.selected_index < 0:
            # No selection - standard scrolling
            return 0, max(0, self.get_total_list_height() - self.get_visible_height())

        # With selection, allow scrolling so any part of list can be centered
        items_above = self.selected_index
        items_below = len(self.choices) - self.selected_index - 1

        # Min scroll: selected item at bottom of visible area (show items above)
        min_scroll = -(items_below * self.item_height)

        # Max scroll: selected item at top of visible area (show items below)
        max_scroll = items_above * self.item_height

        return min_scroll, max_scroll

    def handle_events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        for event in events:
            # ESC key closes dropdown
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.dropped:
                    self.dropped = False
                    self.dragging = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    header_rect = pygame.Rect(self.x, self.y, self.width, self.item_height)

                    if self.dropped:
                        # When dropdown is open, prioritize item clicks over header
                        if self._is_over_dropdown(mouse_pos):
                            self.dragging = True
                            self.drag_start_y = mouse_pos[1]
                            self.drag_start_scroll = self.scroll_offset
                        elif header_rect.collidepoint(mouse_pos):
                            # Click on header area but not on an item - close dropdown
                            self.dropped = False
                            self.scroll_offset = 0
                            self.dragging = False
                        else:
                            # Clicked outside - close dropdown
                            self.dropped = False
                            self.dragging = False
                    else:
                        # Dropdown is closed - header click opens it
                        if header_rect.collidepoint(mouse_pos):
                            self.dropped = True
                            self.scroll_offset = 0
                            self.dragging = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.dropped:
                    if self.dragging:
                        # Check if it was a click (minimal movement) vs drag
                        drag_distance = abs(mouse_pos[1] - self.drag_start_y)
                        if drag_distance < 5:  # Threshold for click vs drag
                            # It was a click - select item
                            clicked_item = self._get_item_at_pos(mouse_pos)
                            if clicked_item is not None:
                                self.selected = self.choices[clicked_item]
                                self.selected_index = clicked_item
                                self.dropped = False
                                self.scroll_offset = 0
                    self.dragging = False

            # Mouse wheel scrolling - works anywhere when dropdown is open
            elif event.type == pygame.MOUSEWHEEL and self.dropped:
                min_scroll, max_scroll = self.get_scroll_range()
                # Reversed: scroll up (positive event.y) moves list up (increases offset)
                self.scroll_offset += event.y * self.item_height
                self.scroll_offset = max(min_scroll, min(max_scroll, self.scroll_offset))

        # Handle drag scrolling - works anywhere when dropdown is open
        if self.dragging and mouse_buttons[0]:
            # Reversed: drag up moves list up
            drag_delta = mouse_pos[1] - self.drag_start_y
            min_scroll, max_scroll = self.get_scroll_range()
            self.scroll_offset = self.drag_start_scroll + drag_delta
            self.scroll_offset = max(min_scroll, min(max_scroll, self.scroll_offset))

        # Update hover state (only when not dragging)
        self.hovered_index = -1
        if self.dropped and not self.dragging:
            hovered = self._get_item_at_pos(mouse_pos)
            if hovered is not None:
                self.hovered_index = hovered

    def _is_over_header(self, pos):
        """Check if position is over the header"""
        header_rect = pygame.Rect(self.x, self.y, self.width, self.item_height)
        return header_rect.collidepoint(pos)

    def _is_over_dropdown(self, pos):
        """Check if position is over the dropdown area"""
        if not self.dropped:
            return False

        # Get the current clip bounds
        clip_top, clip_bottom = self._get_clip_bounds()

        return (self.x <= pos[0] <= self.x + self.width and
                clip_top <= pos[1] <= clip_bottom)

    def _get_clip_bounds(self):
        """Calculate the visible clip area bounds"""
        visible_height = self.get_visible_height()

        if self.selected_index >= 0:
            # Calculate base_y (where item 0 starts)
            base_y = self.y - (self.selected_index * self.item_height) + self.scroll_offset

            # Clip bounds based on where items actually are
            list_top = base_y
            list_bottom = base_y + self.get_total_list_height()

            # Center visible area around header, but constrain to actual list
            half_visible = visible_height // 2
            clip_top = max(list_top, self.y - half_visible)
            clip_bottom = min(list_bottom, self.y + self.item_height + half_visible)

            # Ensure we show full visible_height when possible
            if clip_bottom - clip_top < visible_height:
                if clip_top == list_top:
                    clip_bottom = min(list_bottom, clip_top + visible_height)
                else:
                    clip_top = max(list_top, clip_bottom - visible_height)
        else:
            clip_top = self.y
            clip_bottom = self.y + visible_height

        return clip_top, clip_bottom

    def _get_item_at_pos(self, pos):
        """Get the index of the item at the given position"""
        if not self.dropped:
            return None

        # Calculate base Y for the list (where index 0 starts)
        if self.selected_index >= 0:
            base_y = self.y - (self.selected_index * self.item_height) + self.scroll_offset
        else:
            base_y = self.y + self.scroll_offset

        # Check if x is within dropdown
        if not (self.x <= pos[0] <= self.x + self.width):
            return None

        # Check if within clip bounds
        clip_top, clip_bottom = self._get_clip_bounds()
        if not (clip_top <= pos[1] <= clip_bottom):
            return None

        # Calculate which item
        relative_y = pos[1] - base_y
        index = int(relative_y // self.item_height)

        if 0 <= index < len(self.choices):
            return index
        return None

    def draw(self):
        if self.dropped:
            self._draw_dropped()
        else:
            self._draw_collapsed()

    def _draw_collapsed(self):
        """Draw just the header when collapsed"""
        header_rect = pygame.Rect(self.x, self.y, self.width, self.item_height)
        pygame.draw.rect(self.screen, self.bg_color, header_rect, border_radius=self.border_radius)
        pygame.draw.rect(self.screen, self.border_color, header_rect, self.border_width, border_radius=self.border_radius)

        header_text = self.selected if self.selected else self.name
        text_surface = self.font.render(header_text, True, self.text_color)
        text_rect = text_surface.get_rect(center=header_rect.center)
        self.screen.blit(text_surface, text_rect)

    def _draw_dropped(self):
        """Draw the full dropdown when expanded"""
        # Calculate where the list starts (base_y is where item 0 would be)
        if self.selected_index >= 0:
            base_y = self.y - (self.selected_index * self.item_height) + self.scroll_offset
        else:
            base_y = self.y + self.scroll_offset

        # Get clip bounds
        clip_top, clip_bottom = self._get_clip_bounds()
        clip_rect = pygame.Rect(self.x, clip_top, self.width, clip_bottom - clip_top)

        # Draw background for entire visible area
        pygame.draw.rect(self.screen, self.bg_color, clip_rect)

        # Set clipping
        self.screen.set_clip(clip_rect)

        # Draw each item
        for i, choice in enumerate(self.choices):
            item_y = base_y + (i * self.item_height)
            item_rect = pygame.Rect(self.x, item_y, self.width, self.item_height)

            # Only process if potentially visible
            if item_y + self.item_height >= clip_top and item_y <= clip_bottom:
                # Determine color
                if i == self.selected_index:
                    color = self.selected_color
                elif i == self.hovered_index:
                    color = self.hover_color
                else:
                    color = self.bg_color

                pygame.draw.rect(self.screen, color, item_rect)

                # Divider line (except for first item)
                if i > 0:
                    pygame.draw.line(self.screen, self.border_color,
                                     (self.x, item_y), (self.x + self.width, item_y), 1)

                # Text
                text_surface = self.font.render(choice, True, self.text_color)
                text_rect = text_surface.get_rect(center=item_rect.center)
                self.screen.blit(text_surface, text_rect)

        # Remove clipping
        self.screen.set_clip(None)

        # Draw border around visible area
        border_rect = pygame.Rect(
            self.x - self.border_width // 2,
            clip_top - self.border_width // 2,
            self.width + self.border_width,
            (clip_bottom - clip_top) + self.border_width
        )
        pygame.draw.rect(self.screen, self.border_color, border_rect, self.border_width, border_radius=self.border_radius)

    def get_selected(self):
        return self.selected

    def set_selected(self, value):
        if value in self.choices:
            self.selected = value
            self.selected_index = self.choices.index(value)
            return True
        return False
