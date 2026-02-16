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

# exerice de classe 3
#Par Milan Mallak

import arcade
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800
WINDOW_TITLE = "Drawing"

rouge = (224, 54, 54)
rouge2 = (161, 31, 31)
blanc = (246, 227, 195)
blanc2 = (199, 175, 141)
noire = (21, 22, 16)
noire2 = (15, 14, 20)
bleu = (163, 196, 211)
bleu2 = (68, 97, 129)
aqua = (33, 75, 73)
aqua2 = (7, 33, 30)
silver = (169, 146, 156)
silver2 = (72, 61, 67)

class GameView(arcade.Window):
    def __init__(self):

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK_BEAN)

    def on_draw(self):
        self.clear()

        arcade.draw.draw_ellipse_filled(306, 679, 120, 90, aqua2, -18, 15)
        arcade.draw.draw_ellipse_outline(308, 667, 110, 65, arcade.color.BLACK, 7, -18, 20)
        arcade.draw.draw_circle_filled(291, 694, 9, silver, 0, 20)
        arcade.draw.draw_ellipse_filled(289, 695, 18, 14, silver2, -51, 20)

        arcade.draw.draw_triangle_filled(278, 668, 265, 567, 254, 623, noire2)
        arcade.draw.draw_triangle_filled(258, 568, 265, 567, 254, 623, noire2)
        arcade.draw.draw_triangle_filled(254, 623, 261, 578, 250, 591, noire2)
        arcade.draw.draw_triangle_filled(265, 619, 265, 567, 283, 558, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 283, 558, 292, 569, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 292, 569, 299, 563, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 299, 563, 348, 560, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 348, 560, 387, 587, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 387, 587, 393, 602, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 393, 602, 371, 638, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(354, 660, 370, 648, 372, 605, noire2)
        arcade.draw.draw_triangle_filled(370, 648, 372, 605, 394, 602, noire2)

        arcade.draw.draw_triangle_filled(334, 581,323, 611, 362, 605, rouge)
        arcade.draw.draw_triangle_filled(361, 637, 323, 611, 362, 605, rouge)
        arcade.draw.draw_triangle_filled(361, 637, 323, 611, 320, 613, rouge)
        arcade.draw.draw_triangle_filled(361, 637, 321, 616, 320, 613, rouge)

        arcade.draw.draw_arc_filled(340, 628, 45, 7, rouge2, 0, 360, -28, 20)
        arcade.draw.draw_triangle_filled(361, 637, 321, 616, 321, 617, rouge2)
        arcade.draw.draw_triangle_filled(361, 637, 321, 616, 314, 623, rouge2)
        arcade.draw.draw_triangle_filled(353, 651, 314, 623, 361, 637, rouge2)
        arcade.draw.draw_triangle_filled(353, 651, 314, 623, 312, 638, rouge2)
        arcade.draw.draw_triangle_filled(353, 651, 337, 658, 312, 638, rouge2)

        arcade.draw.draw_triangle_filled(309, 655, 337, 658, 312, 638, rouge)
        arcade.draw.draw_triangle_filled(309, 655, 337, 658, 326, 661, rouge)

        arcade.draw.draw_triangle_filled(334, 581, 323, 611, 287, 589, blanc)
        arcade.draw.draw_triangle_filled( 276, 611, 323, 611, 287, 589, blanc)

        arcade.draw.draw_triangle_filled(322, 611, 320, 613, 310, 610, blanc)
        arcade.draw.draw_triangle_filled(320, 611, 320, 619, 307, 610, blanc)

        arcade.draw.draw_triangle_filled(284, 604, 276, 610, 320, 615, blanc2)
        arcade.draw.draw_triangle_filled(320, 620, 276, 610, 320, 615, blanc2)
        arcade.draw.draw_triangle_filled(320, 620, 276, 610, 314, 625, blanc2)
        arcade.draw.draw_triangle_filled(314, 625, 276, 610, 312, 632, blanc2)
        arcade.draw.draw_triangle_filled(276, 610, 287, 616, 273, 616, blanc2)
        arcade.draw.draw_triangle_filled(272, 625, 287, 616, 273, 616, blanc2)

        arcade.draw.draw_triangle_filled(311, 639, 287, 616, 312, 632, bleu2)
        arcade.draw.draw_triangle_filled(311, 639, 287, 616, 281, 618, bleu2)
        arcade.draw.draw_triangle_filled(274, 634, 278, 670, 305, 650, bleu2)

        arcade.draw.draw_triangle_filled(311, 639, 272, 626, 281, 618, bleu)
        arcade.draw.draw_triangle_filled(311, 639, 272, 626, 271, 633, bleu)
        arcade.draw.draw_triangle_filled(311, 639, 308, 654, 271, 633, bleu)

        arcade.draw.draw_triangle_filled(356, 651, 364, 648, 366, 630, rouge2)
        arcade.draw.draw_triangle_filled(362, 640, 366, 630, 363, 621, rouge2)

        arcade.draw.draw_triangle_filled(270, 629, 265, 620, 268, 611, blanc2)
        arcade.draw.draw_triangle_filled(270, 629, 268, 611, 273, 603, blanc2)
        arcade.draw.draw_triangle_filled(270, 615, 273, 603, 280, 598, blanc2)

        arcade.draw.draw_triangle_filled(282, 663, 283, 645, 322, 659, noire2)
        arcade.draw.draw_triangle_filled(282, 663, 340, 676, 322, 659, noire2)
        arcade.draw.draw_triangle_filled(358, 659, 355, 651, 328, 675, noire2)
        arcade.draw.draw_triangle_filled(323,664, 355, 651, 328, 675, noire2)

        arcade.draw.draw_line(283, 593, 294, 585, arcade.color.BLACK, 3)

        arcade.draw.draw_triangle_filled(265, 641, 260, 649, 266, 663, aqua)
        arcade.draw.draw_triangle_filled(265, 641, 266, 663, 302, 664, aqua)
        arcade.draw.draw_triangle_filled(266, 663, 302, 664, 323, 684, aqua)
        arcade.draw.draw_triangle_filled(302, 664, 323, 684, 332, 671, aqua)
        arcade.draw.draw_triangle_filled(323, 684, 332, 671, 351, 667, aqua)
        arcade.draw.draw_arc_outline(306, 655, 87, 18, aqua, 0, 180, 4, -18, 20)


        arcade.draw.draw_triangle_filled(276, 632, 297, 626, 304, 646, noire)
        arcade.draw.draw_triangle_filled(282, 631, 283, 624, 289, 629, noire)
        arcade.draw.draw_triangle_filled(290, 638, 298, 632, 302, 644, arcade.color.WHITE)

        arcade.draw.draw_triangle_filled(319, 641, 335, 655, 353, 643, noire)
        arcade.draw.draw_triangle_filled(321, 643, 335, 653, 351, 644, arcade.color.WHITE)
        arcade.draw.draw_triangle_filled(319, 641, 331, 652, 341, 643, noire)

        arcade.draw.draw_line(324, 609, 310, 602, noire, 3)


def main():
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
