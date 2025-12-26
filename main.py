from pathlib import Path
import arcade
from src.game_view import GameView

ASSETS_PATH = Path(__file__).parent / "assets"

arcade.resources.add_resource_handle("assets", ASSETS_PATH)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Turing Test")
        self.show_view(GameView(self))

if __name__ == "__main__":
    window = MyGame()
    arcade.run()