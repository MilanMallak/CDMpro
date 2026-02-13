# exerice de classe 3
#Par Milan Mallak

import cursorbox

import arcade
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800
WINDOW_TITLE = "Drawing"

rouge = (224, 54, 54)
rouge2 = (161, 31, 31)
rouge3 = (211, 66, 81)
blanc = (246, 227, 195)
blanc2 = (199, 175, 141)
noir = (21, 22, 16)
noir2 = (15, 14, 20)
bleu = (163, 196, 211)
bleu2 = (68, 97, 129)
aqua = (33, 75, 73)
aqua2 = (7, 33, 30)
silver = (169, 146, 156)
silver2 = (72, 61, 67)
pinkish = (223, 184, 202)
pinkish2 = (222, 143, 162)
pinkish3 = (79, 40, 59)

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

        arcade.draw.draw_triangle_filled(278, 668, 265, 567, 254, 623, noir2)
        arcade.draw.draw_triangle_filled(258, 568, 265, 567, 254, 623, noir2)
        arcade.draw.draw_triangle_filled(254, 623, 261, 578, 250, 591, noir2)
        arcade.draw.draw_triangle_filled(265, 619, 265, 567, 283, 558, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 283, 558, 292, 569, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 292, 569, 299, 563, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 299, 563, 348, 560, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 348, 560, 387, 587, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 387, 587, 393, 602, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(265, 619, 393, 602, 371, 638, arcade.color.BLACK)
        arcade.draw.draw_triangle_filled(354, 660, 370, 648, 372, 605, noir2)
        arcade.draw.draw_triangle_filled(370, 648, 372, 605, 394, 602, noir2)

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

        arcade.draw.draw_triangle_filled(282, 663, 283, 645, 322, 659, noir2)
        arcade.draw.draw_triangle_filled(282, 663, 340, 676, 322, 659, noir2)
        arcade.draw.draw_triangle_filled(358, 659, 355, 651, 328, 675, noir2)
        arcade.draw.draw_triangle_filled(323,664, 355, 651, 328, 675, noir2)

        arcade.draw.draw_line(283, 593, 294, 585, arcade.color.BLACK, 3)

        arcade.draw.draw_triangle_filled(265, 641, 260, 649, 266, 663, aqua)
        arcade.draw.draw_triangle_filled(265, 641, 266, 663, 302, 664, aqua)
        arcade.draw.draw_triangle_filled(266, 663, 302, 664, 323, 684, aqua)
        arcade.draw.draw_triangle_filled(302, 664, 323, 684, 332, 671, aqua)
        arcade.draw.draw_triangle_filled(323, 684, 332, 671, 351, 667, aqua)
        arcade.draw.draw_arc_outline(306, 655, 87, 18, aqua, 0, 180, 4, -18, 20)


        arcade.draw.draw_triangle_filled(276, 632, 297, 626, 304, 646, noir)
        arcade.draw.draw_triangle_filled(282, 631, 283, 624, 289, 629, noir)
        arcade.draw.draw_triangle_filled(290, 638, 298, 632, 302, 644, arcade.color.WHITE)

        arcade.draw.draw_triangle_filled(319, 641, 335, 655, 353, 643, noir)
        arcade.draw.draw_triangle_filled(321, 643, 335, 653, 351, 644, arcade.color.WHITE)
        arcade.draw.draw_triangle_filled(319, 641, 331, 652, 341, 643, noir)

        arcade.draw.draw_line(324, 609, 310, 602, noir, 3)


        #Left Arm
        arcade.draw.draw_arc_filled(385, 497, 44, 12, pinkish, 0, 360, 142, 10)
        arcade.draw.draw_arc_outline(385, 497, 44, 12, noir2, 0, 180, 1, 142, 10)
        arcade.draw.draw_arc_filled(378, 502, 51, 85, pinkish, 0, 180, -22, 20)
        arcade.draw.draw_arc_outline(378, 502, 51, 85, noir2, 0, 180, 1, -22, 20)
        arcade.draw.draw_triangle_filled(397, 510, 371, 488, 374, 519, pinkish)


        #Torso
        arcade.draw.draw_polygon_filled([(306, 557), (281, 513), (300, 507), (316, 553)], pinkish2)
        arcade.draw.draw_polygon_outline([(306, 557), (281, 513), (300, 507), (316, 553)], noir2, 1)
        arcade.draw.draw_polygon_filled([(281, 513), (300, 507), (309, 435), (298, 442)], pinkish2)
        arcade.draw.draw_polygon_outline([(281, 513), (300, 507), (309, 435), (298, 442)], noir2)

        arcade.draw.draw_polygon_filled([(308, 558), (351, 556), (360, 552), (316, 553)], noir2)
        arcade.draw.draw_polygon_filled([(360, 552), (316, 553), (300, 507), (376, 505)], rouge3)
        arcade.draw.draw_polygon_outline([(360, 552), (316, 553), (300, 507), (376, 505)], noir2, 1)

        arcade.draw.draw_triangle_filled(320, 553, 341, 538, 359, 552, rouge2)

        arcade.draw.draw_polygon_filled([(326, 540), (350, 539), (362, 505), (311, 507)], pinkish)
        arcade.draw.draw_polygon_outline([(326, 540), (350, 539), (362, 505), (311, 507)], noir2, 1)

        arcade.draw.draw_polygon_filled([(319, 554), (312, 547), (333, 530), (339, 540)], pinkish)
        arcade.draw.draw_polygon_outline([(319, 554), (312, 547), (333, 530), (339, 540)], noir2, 1.2)
        arcade.draw.draw_polygon_filled([(342, 540), (347, 528), (364, 540), (360, 551)], pinkish)
        arcade.draw.draw_polygon_outline([(342, 540), (347, 528), (364, 540), (360, 552)], noir2, 1.2)

        arcade.draw.draw_polygon_filled([(300, 507), (376, 505), (357, 432), (309, 435)], rouge3)
        arcade.draw.draw_polygon_outline([(300, 507), (376, 505), (357, 432), (309, 435)], noir2, 1)

        arcade.draw.draw_polygon_filled([(311, 507), (362, 505), (348, 433), (319, 434)], pinkish2)
        arcade.draw.draw_polygon_outline([(311, 507), (362, 505), (348, 433), (319, 434)], noir2, 1)

        #Right Arm
        arcade.draw.draw_polygon_filled([(230, 517), (255, 521), (295, 498), (261, 497)], pinkish3)
        arcade.draw.draw_polygon_outline([(230, 517), (255, 521), (295, 498), (261, 497)], noir2, 1)

        arcade.draw.draw_polygon_filled([(250, 527), (231, 463), (240, 459), (265, 525)], blanc2)
        arcade.draw.draw_polygon_outline([(250, 527), (231, 463), (240, 459), (265, 525)], noir2, 1)
        arcade.draw.draw_polygon_filled([(265, 525), (240, 459), (263, 460), (283, 513)], bleu)
        arcade.draw.draw_polygon_outline([(265, 525), (240, 459), (263, 460), (283, 513)], noir2, 1)
        arcade.draw.draw_polygon_filled([(231, 463), (240, 459), (284, 390), (287, 393)], bleu)
        arcade.draw.draw_polygon_outline([(231, 463), (240, 459), (287, 393), (284, 390)], noir2, 1)
        arcade.draw.draw_polygon_filled([(240, 459), (287, 393), (297, 406), (283, 445), (263, 460)], blanc2)
        arcade.draw.draw_polygon_outline([(240, 459), (287, 393), (297, 406), (283, 445), (263, 460)], noir2, 1)

        arcade.draw.draw_polygon_filled([(294, 549), (295, 498), (255, 521), (276, 560)], pinkish2)
        arcade.draw.draw_polygon_outline([(294, 549), (295, 498), (255, 521), (276, 560)], noir2, 1)
        arcade.draw.draw_polygon_filled([(255, 521), (276, 560), (261, 557), (230, 517)], pinkish2)
        arcade.draw.draw_polygon_outline([(255, 521), (276, 560), (261, 557), (230, 517)], noir2, 1)
        #



        cursorbox.draw_information()

    def on_mouse_motion(self, x: float, y, shit1, shi2):
        cursorbox.mouseX = x
        cursorbox.mouseY = y

def main():
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()