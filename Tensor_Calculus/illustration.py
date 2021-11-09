from manim import *

config.background_color = WHITE


class Basis(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        vec_e1 = Vector([1, 0]).set_color(BLUE)
        vec_e2 = Vector([0, 1]).set_color(BLUE)
        label_vec_e1 = Tex("$\overrightarrow{e_1}$").set_color(
            BLUE).next_to(vec_e1.get_right(), RIGHT)
        label_vec_e2 = Tex("$\overrightarrow{e_2}$").set_color(
            BLUE).next_to(vec_e2.get_top(), UP)

        vec_tilde_e1 = Vector([2, 1]).set_color(RED)
        vec_tilde_e2 = Vector([-0.5, 0.25]).set_color(RED)
        label_vec_tilde_e1 = Tex("$\widetilde{\overrightarrow{e_1}}$").set_color(
            RED).next_to(vec_tilde_e1.get_corner(UR), RIGHT)
        label_vec_tilde_e2 = Tex("$\widetilde{\overrightarrow{e_2}}$").set_color(
            RED).next_to(vec_tilde_e2.get_tip(), UL*0.5)

        vec = Vector([1, 2]).set_color(YELLOW_E)
        label_vec = Tex(r"$\vec{v}$").set_color(
            YELLOW_E).next_to(vec.get_corner(UR), UR*0.5)

        vectors = VGroup(vec_e1, vec_e2, vec_tilde_e1, vec_tilde_e2, vec,
                         label_vec_e1, label_vec_e2, label_vec_tilde_e1, label_vec_tilde_e2, label_vec)
        self.add(vectors)


class CoordinateTransform(LinearTransformationScene):
    CONFIG = {
        "show_basis_vectors": True,
        "foreground_plane_kwargs": {
            "x_max": 10,
            "x_min": -10,
            "y_max": 10,
            "y_min": -10,
            "faded_line_ratio": 0
        },
    }

    def construct(self):
        self.setup()
        self.wait()

        vec = Vector([3, 2]).set_color(ORANGE)
        self.add_vector(vec)

        labelVec = vec.coordinate_label().set_color(ORANGE)
        self.add_moving_mobject(labelVec)

        self.apply_matrix([[2, -1], [0, 1]])

        self.wait()
