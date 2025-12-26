import arcade

class Resources:
    def __init__(self):
        self.backgrounds = {
            "cyber_room": arcade.load_texture(":assets:images/backgrounds/cyber_room.png")
        }
resources = Resources()