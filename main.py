import random
from manim import *


class ChristmasMessage(Scene):
    def construct(self):
        # TODO: add Christmas images and animate them
        text_merry = Text('Merry', color=RED, font_size=84).move_to(2.6 * LEFT)
        text_christmas = Text('Christmas', color=GREEN, font_size=84).next_to(text_merry, RIGHT)

        self.play(FadeIn(text_merry))
        self.play(FadeIn(text_christmas))

        color_map = ['#165B33', '#146B3A', '#F8B229', '#EA4630', '#BB2528']
        for _ in range(100):
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
            # TODO: Make the animation faster (hopefully it can go lower than 0.1)
            self.play(text_merry.animate(run_time=0.1))
            self.play(text_christmas.animate(run_time=0.1))
