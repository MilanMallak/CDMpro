# exerice de classe 3
#Par Milan Mallak

import arcade
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800
WINDOW_TITLE = "Drawing"

class GameView(arcade.Window):
    def __init__(self):

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK_BEAN)

    def on_draw(self):
        self.clear()
        arcade.draw.draw_triangle_filled(328, 226,325, 203, 354, 178)


def main():
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

