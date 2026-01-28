import os.path
class Colors:
    TAN_BG = "#f0edd3"
    PRIMARY_TEXT = "#45454b"
    DROPDOWN_BG = "#d3cdab"
    HEALTH_GREEN = "#63e141"
    HEALTH_RED = "#ec3c55"

class Fonts:
    MAIN_FONT = os.path.join(
        os.path.dirname(__file__), "..", "..", "assets", "fonts", "SyneMono-Regular.ttf")

class Images:
    PLAYER_PORTRAIT = os.path.join(
        os.path.dirname(__file__), "..", "..", "assets", "images", "placeholder.png")
    MOUSE_PORTRAIT = os.path.join(
        os.path.dirname(__file__), "..", "..", "assets", "images", "mouse.png")
    GOBLIN_PORTRAIT = os.path.join(
        os.path.dirname(__file__), "..", "..", "assets", "images", "goblin.png")