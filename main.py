import numpy as np
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

        # You can change all parameters from here
        self.looping_colors(iterations=1000,
                            runtime=0.001,
                            text_merry=text_merry,
                            text_christmas=text_christmas,
                            color_map=color_map,
                            image_obj=christmas_tree_img,
                            start_image_loop=500)

    def looping_colors(self, iterations, runtime, text_merry, text_christmas, color_map, image_obj, start_image_loop):

        for iteration in range(iterations):
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
            # Playing this total randomness (you can change the 'run_time' parameter
            # to speed up or slow down the animations)
            self.play(text_merry.animate(run_time=runtime))
            self.play(text_christmas.animate(run_time=runtime))

            if iteration >= start_image_loop:
                self.looping_image(image_obj=image_obj,
                                   iterations=1)

    def looping_image(self, image_obj, iterations):
        
        for iteration in range(iterations):
            self.play(Rotate(image_obj, np.array(0.5*PI), run_time=0.01))
