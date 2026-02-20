#TP5
#Par Milan Mallak

from turtledemo.nim import SCREENWIDTH

import cursorbox

import arcade
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 800
WINDOW_TITLE = "Drawing"

#Color Palette
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
jaune = (245, 204, 86)
jaune2 = (190, 170, 55)


class GameView(arcade.Window):
    def __init__(self):

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        ena_font = arcade.load_font("assets/gomarice_no_continue.ttf")

    def setup(self):
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        self.clear()

        arcade.draw.draw_lrbt_rectangle_filled(0, SCREENWIDTH, 0, 90, arcade.color.DARK_GRAY)

        # Text
        e_sprite = arcade.create_text_sprite("e", arcade.color.WHITE, 30, None, "left", "No Continue")
        e_sprite.scale_x = -1
        e_sprite.position = (80, 766)
        arcade.draw.draw_sprite(e_sprite)

        arcade.draw_text("n", 90, 750, arcade.color.GREEN, 30, None, "left", "No Continue")
        arcade.draw_text("a", 110, 750, rouge, 30, None, "left", "No Continue")

        arcade.draw_text("dream", 10, 690, arcade.color.BABY_BLUE, 50, None, "left", "No Continue")

        arcade.draw_text("bbq", 57, 643, arcade.color.BUD_GREEN, 40, None, "left", "No Continue")

        arcade.draw.draw_point(5, 710, arcade.color.WHITE, 8)
        arcade.draw.draw_point(196, 710, arcade.color.WHITE, 8)


        #Head and Hat

        arcade.draw.draw_ellipse_filled(306, 679, 120, 90, aqua2, -18, 15)
        arcade.draw.draw_ellipse_outline(308, 667, 110, 65, arcade.color.BLACK, 7, -18, 20)
        arcade.draw.draw_circle_filled(291, 694, 9, silver, 0, 20)
        arcade.draw.draw_ellipse_filled(289, 695, 18, 14, silver2, -51, 20)

        arcade.draw.draw_triangle_filled(351, 661, 367, 649, 340, 611, noir)
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
        arcade.draw.draw_polygon_filled([(379, 450), (399, 429), (366, 413), (333, 419)], rouge2)
        arcade.draw.draw_polygon_filled([(391, 504), (397, 476), (404, 451), (407, 442), (399, 429), (368, 415), (368, 424), (372, 432), (378, 439), (384, 445), (378, 452), (364, 487)], rouge)
        arcade.draw.draw_polygon_outline([(391, 504), (397, 476), (404, 451), (407, 442), (399, 429), (366, 413), (333, 419), (350, 432), (379, 450), (364, 487)], noir2, 1)
        arcade.draw.draw_line(378, 452, 384, 445, noir2, 1)

        arcade.draw.draw_arc_filled(385, 497, 44, 12, pinkish, 0, 360, 142, 10)
        arcade.draw.draw_arc_outline(385, 497, 44, 12, noir2, 0, 180, 2, 142, 10)
        arcade.draw.draw_arc_filled(378, 502, 51, 85, pinkish, 0, 180, -22, 20)
        arcade.draw.draw_arc_outline(378, 502, 51, 85, noir2, 0, 180, 2, -22, 20)
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
        arcade.draw.draw_polygon_filled([(231, 463), (240, 459), (287, 393), (284, 390)], bleu)
        arcade.draw.draw_polygon_outline([(231, 463), (240, 459), (287, 393), (284, 390)], noir2, 1)
        arcade.draw.draw_polygon_filled([(240, 459), (287, 393), (297, 406), (283, 445), (263, 460)], blanc2)
        arcade.draw.draw_polygon_outline([(240, 459), (287, 393), (297, 406), (283, 445), (263, 460)], noir2, 1)

        arcade.draw.draw_polygon_filled([(294, 549), (295, 498), (255, 521), (276, 560)], pinkish2)
        arcade.draw.draw_polygon_outline([(294, 549), (295, 498), (255, 521), (276, 560)], noir2, 1)
        arcade.draw.draw_polygon_filled([(255, 521), (276, 560), (261, 557), (230, 517)], pinkish2)
        arcade.draw.draw_polygon_outline([(255, 521), (276, 560), (261, 557), (230, 517)], noir2, 1)


        #Left Leg
        arcade.draw.draw_polygon_filled([(364, 303), (360, 297), (359, 291), (358, 280), (358, 265),
                                         (350, 259), (341, 259), (333, 261), (328, 263), (326, 269), (327, 286),(331, 299), (332, 320), (334, 327), (350, 339)], noir2)
        arcade.draw.draw_polygon_outline([(364, 303), (360, 297), (359, 291), (358, 280), (358, 265),
                                          (350, 259), (341, 259), (333, 261), (328, 263), (326, 269), (327, 286),(331, 299), (332, 320), (334, 327), (350, 339)], arcade.color.BLACK, 1)
        arcade.draw.draw_polygon_filled([(364, 303), (360, 297), (359, 291), (358, 280), (358, 265), (250, 262), (341, 262), (335, 265), (339, 300), (341, 307), (345, 309), (356, 313)], noir)

        arcade.draw.draw_polygon_filled([(334, 341), (342, 327), (364, 320), (388, 318),
                                         (372, 323), (367, 329), (366, 344), (370, 358), (379, 366), (387, 368),
                                         (400, 359), (397, 369), (390, 374), (355, 374)], aqua)
        arcade.draw.draw_polygon_outline([(334, 341), (342, 327), (364, 320), (388, 318),
                                         (372, 323), (367, 329), (366, 344), (370, 358), (379, 366), (387, 368),
                                         (400, 359), (397, 369), (390, 374), (355, 374)], noir2, 1)
        arcade.draw.draw_line_strip([(363, 321), (359, 326), (358, 333), (358, 343), (361, 353), (365, 361), (371, 367), (375, 371), (383, 374)], noir2, 1)
        arcade.draw.draw_polygon_filled([(372, 378), (362, 362), (355, 348), (341, 341), (350, 390)], aqua2)

        arcade.draw.draw_polygon_filled([(387, 368), (399, 363), (404, 359), (409, 352), (412, 345), (414, 335), (412, 324), (410, 313), (405, 304), (398, 298), (388, 296), (370, 296), (361, 300),
                                         (353, 305), (348, 312), (348, 317), (351, 323), (361, 323), (368, 322)], rouge)
        arcade.draw.draw_polygon_outline([(387, 368), (399, 363), (404, 359), (409, 352), (412, 345), (414, 335), (412, 324), (410, 313), (405, 304),(398, 298), (388, 296), (370, 296), (361, 300),
             (353, 305), (348, 312), (348, 317), (351, 323), (361, 323), (368, 322)], noir2, 1)
        arcade.draw.draw_ellipse_filled(384, 343, 37, 51, rouge, 17, 20)
        arcade.draw.draw_arc_outline(384, 343, 37, 51, noir2, 73, 280,3, 17, 20)
        arcade.draw.draw_arc_outline(390, 327, 6, 24, noir2, 90, 270, 2, 0, 10)


        #Megaphone
        arcade.draw.draw_polygon_filled([(194, 364) ,(233, 291), (318, 380), (304, 394)], jaune2)
        arcade.draw.draw_polygon_filled([(194, 364), (304, 394), (300, 388), (200, 361)], jaune)
        arcade.draw.draw_polygon_outline([(194, 364), (233, 291), (318, 380), (304, 394)], noir2, 1)
        arcade.draw.draw_ellipse_filled(213, 328, 81, 30, jaune2, 60, 30)
        arcade.draw.draw_ellipse_outline(213, 328, 81, 30, noir2, 1, 60, 30)


        # Waist
        arcade.draw.draw_polygon_filled(
            [(293, 430), (303, 429), (301, 408), (296, 404), (291, 399), (290, 395), (288, 387), (277, 389), (278, 398), (280, 403), (284, 406), (290, 410)], aqua2)
        arcade.draw.draw_polygon_outline([(293, 430), (303, 429), (301, 408), (296, 404), (291, 399), (290, 395), (288, 387), (277, 389), (278, 398), (280, 403), (284, 406), (290, 410)], noir2, 1)

        arcade.draw.draw_polygon_filled([(300, 388), (305, 363), (307, 343), (312, 338), (330, 384)], aqua2)
        arcade.draw.draw_polygon_outline([(300, 388), (305, 363), (307, 343), (312, 338), (330, 384)], noir2, 1)

        arcade.draw.draw_polygon_filled([(303, 429), (357, 420), (369, 416), (368, 401), (377, 392), (375, 375), (362, 371), (356, 366), (352, 359), (344, 337), (312, 338), (313, 358), (311, 369),
                                         (304, 376), (295, 382), (288, 387), (290, 395), (291, 399), (296, 404), (301, 408)], aqua)
        arcade.draw.draw_polygon_outline([(303, 429), (357, 420), (369, 416), (368, 401), (377, 392), (375, 375), (362, 371), (356, 366), (352, 359), (344, 337), (312, 338), (313, 358), (311, 369),
                                         (304, 376), (295, 382), (288, 387), (290, 395), (291, 399), (296, 404), (301, 408)], noir2, 1)
        arcade.draw.draw_line(346, 421, 330, 337, noir2, 2)


        #Right Leg
        arcade.draw.draw_polygon_filled([(306, 302), (312, 255), (300, 242), (295, 290)], blanc)
        arcade.draw.draw_polygon_outline([(306, 302), (312, 255), (300, 242), (295, 290)], noir2, 1)
        arcade.draw.draw_polygon_filled([(300, 242), (295, 290), (269, 294), (277, 248), (300, 242)], bleu)
        arcade.draw.draw_polygon_outline([(300, 242), (295, 290), (269, 294), (277, 248), (300, 242)], noir2, 1)

        arcade.draw.draw_polygon_filled([(278, 373), (294, 295), (308, 310), (297, 359)], aqua)
        arcade.draw.draw_polygon_outline([(278, 373), (294, 295), (308, 310), (297, 359)], noir2, 1)
        arcade.draw.draw_polygon_filled([(278, 373), (294, 295), (265, 301), (257, 339), (267, 346)], aqua2)
        arcade.draw.draw_polygon_outline([(278, 373), (294, 295), (265, 301), (257, 339), (267, 346)], noir2, 1)

        arcade.draw.draw_polygon_filled([(308, 310), (311, 311), (313, 301), (295, 282), (294, 295)], aqua)
        arcade.draw.draw_polygon_outline([(308, 310), (311, 311), (313, 301), (295, 282), (294, 295)], noir2, 1)
        arcade.draw.draw_polygon_filled([(294, 295), (295, 282), (263, 289), (260, 298), (265, 301)], aqua2)
        arcade.draw.draw_polygon_outline([(294, 295), (295, 282), (263, 289), (260, 298), (265, 301)], noir2, 1)

        arcade.draw.draw_polygon_filled([(300, 242), (312, 255), (303, 211)], noir)
        arcade.draw.draw_polygon_outline([(300, 242), (312, 255), (303, 211)], arcade.color.BLACK)
        arcade.draw.draw_polygon_filled([(312, 255), (323, 222), (336, 83), (330, 91), (303, 211)], noir2)
        arcade.draw.draw_polygon_outline([(312, 255), (323, 222), (336, 83), (330, 91), (303, 211)], arcade.color.BLACK, 1)
        arcade.draw.draw_line(323, 222, 303, 211, arcade.color.BLACK, 1)
        arcade.draw.draw_polygon_filled([(300, 242), (303, 211), (277, 248)], noir2)
        arcade.draw.draw_polygon_outline([(300, 242), (303, 211), (277, 248)], arcade.color.BLACK, 1)
        arcade.draw.draw_polygon_filled([(277, 248), (303, 211), (330, 91), (338, 83), (371, 58), (322, 75), (305, 61), (314, 91), (275, 210)], noir)
        arcade.draw.draw_polygon_outline([(277, 248), (303, 211), (330, 91), (338, 83), (371, 58), (322, 75), (305, 61), (314, 91), (275, 210)], arcade.color.BLACK, 1)
        arcade.draw.draw_line(303, 211, 275, 210, arcade.color.BLACK, 1)
        arcade.draw.draw_line(330, 91, 314, 91, arcade.color.BLACK, 1)
        arcade.draw.draw_line(330, 91, 322, 75, arcade.color.BLACK, 1)
        arcade.draw.draw_polygon_filled([(305, 61), (322, 75), (371, 58), (373, 45), (333, 46)], noir2)
        arcade.draw.draw_polygon_outline([(305, 61), (322, 75), (371, 58), (373, 45), (333, 46)], arcade.color.BLACK, 1)
        arcade.draw.draw_line(322, 75, 337, 60, arcade.color.BLACK, 1)
        arcade.draw.draw_line(337, 60, 349, 65, arcade.color.BLACK, 1)
        arcade.draw.draw_line(337, 60, 333, 46, arcade.color.BLACK, 1)
        arcade.draw.draw_line(337, 60, 372, 51, arcade.color.BLACK, 1)


        cursorbox.draw_information()


    def on_mouse_motion(self, x: float, y, var1, var2):
        cursorbox.mouseX = x
        cursorbox.mouseY = y

def main():
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
