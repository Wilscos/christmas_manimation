import random
from manim import *


class ChristmasMessage(Scene):
    def construct(self):
        christmas_tree_img = ImageMobject('images/christmas_tree.png')
        christmas_tree_img.height = 2

        text_merry = Text('Merry', color=RED, font_size=84).move_to(2.6 * LEFT)
        text_christmas = Text('Christmas', color=GREEN, font_size=84).next_to(text_merry, RIGHT)
        christmas_tree_img.next_to(text_christmas, RIGHT)

        self.play(FadeIn(text_merry))
        self.play(FadeIn(text_christmas))
        self.play(FadeIn(christmas_tree_img))

        color_map = ['#165B33', '#146B3A', '#F8B229', '#EA4630', '#BB2528',
                     '#FAFAFA', '#C43A47', '#843145', '#E7D6BA', '#3E6C67',
                     '#90B594']
        for _ in range(10):
            # Getting random index for letter in word 'Merry'
            random_merry_letter_idx = random.choice(range(len(text_merry)))
            # Getting random index for letter in word 'Christmas'
            random_christmas_letter_idx = random.choice(range(len(text_christmas)))
            # Getting random letter for word 'Merry' from index
            random_merry_letter = text_merry[random_merry_letter_idx]
            # Getting random letter for word 'Christmas' from index
            random_christmas_letter = text_christmas[random_christmas_letter_idx]
            # Setting random color to random letter in word 'Merry'
            random_merry_letter.set_color(random.choice(color_map))
            # Setting random color to random letter in word 'Christmas'
            random_christmas_letter.set_color(random.choice(color_map))
            # Playing this total randomness
            self.play(text_merry.animate(run_time=0.05))
            self.play(text_christmas.animate(run_time=0.05))
