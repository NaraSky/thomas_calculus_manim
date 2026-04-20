from manim import *


class Scene10_EvenFunctionsMirrorSymmetry(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    GRAPH_COLOR = BLUE
    MIRROR_COLOR = YELLOW
    POINT_COLOR = GREEN

    def construct(self):
        self.setup_layout()
        self.step1_create_parabola()
        self.step2_highlight_mirror_axis()
        self.step3_place_right_point()
        self.step4_draw_height_guide()
        self.step5_reflect_point()
        self.step6_label_reflected_point()
        self.step7_show_equal_height()
        self.step8_write_specific_rule()
        self.step9_generalize_rule()
        self.step10_label_even_function()
        self.step11_move_point_pair()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.a = 1.25
        self.b = 1.75
        self.create_axes()
        self.create_graph()
        self.create_mirror_axis()
        self.create_points()
        self.create_guides()
        self.create_rules()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-0.3, 4.2, 1],
            x_length=7.2,
            y_length=4.7,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-0.8, -0.25, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.72)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.72)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_graph(self):
        points = [self.axes.c2p(x / 40, (x / 40) ** 2) for x in range(-88, 89)]
        self.graph = VMobject(color=self.GRAPH_COLOR, stroke_width=4)
        self.graph.set_points_smoothly(points)

        self.graph_label = MathTex("y=x^2", color=WHITE).scale(0.75)
        self.graph_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.graph_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.graph_label.move_to([0, 3.2, 0])

    def create_mirror_axis(self):
        self.mirror_axis = DashedLine(
            self.axes.c2p(0, -0.2),
            self.axes.c2p(0, 4.0),
            color=self.MIRROR_COLOR,
            dash_length=0.12,
            stroke_width=4,
        )
        self.mirror_label = Text("mirror", font_size=26, color=self.MIRROR_COLOR)
        self.mirror_label.next_to(self.mirror_axis, UP, buff=0.12)

    def create_points(self):
        self.right_point = Dot(self.point_at(self.a), radius=0.08, color=self.POINT_COLOR)
        self.right_label = MathTex("(a,f(a))", color=WHITE).scale(0.6)
        self.right_label.next_to(self.right_point, UP + RIGHT, buff=0.1)

        self.left_point = Dot(self.point_at(-self.a), radius=0.08, color=self.POINT_COLOR)
        self.left_label = MathTex("(-a,f(a))", color=WHITE).scale(0.6)
        self.left_label.next_to(self.left_point, UP + LEFT, buff=0.1)

        self.next_right_point = Dot(self.point_at(self.b), radius=0.08, color=self.POINT_COLOR)
        self.next_left_point = Dot(self.point_at(-self.b), radius=0.08, color=self.POINT_COLOR)
        self.next_right_label = MathTex("(b,f(b))", color=WHITE).scale(0.6)
        self.next_left_label = MathTex("(-b,f(b))", color=WHITE).scale(0.6)
        self.next_right_label.next_to(self.next_right_point, UP + RIGHT, buff=0.1)
        self.next_left_label.next_to(self.next_left_point, UP + LEFT, buff=0.1)

    def create_guides(self):
        self.height_guide = DashedLine(
            self.point_at(-self.a),
            self.point_at(self.a),
            color=self.OUTPUT_COLOR,
            dash_length=0.12,
            stroke_width=3,
        )
        self.height_label = MathTex(r"\text{same height}", color=self.OUTPUT_COLOR).scale(0.55)
        self.height_label.next_to(self.height_guide, UP, buff=0.12)

        self.reflection_arrow = CurvedArrow(
            self.point_at(self.a) + 0.25 * UP,
            self.point_at(-self.a) + 0.25 * UP,
            color=self.MIRROR_COLOR,
            stroke_width=4,
        )

        self.next_height_guide = DashedLine(
            self.point_at(-self.b),
            self.point_at(self.b),
            color=self.OUTPUT_COLOR,
            dash_length=0.12,
            stroke_width=3,
        )

    def create_rules(self):
        self.specific_rule = MathTex("f(-a)", "=", "f(a)", color=WHITE).scale(0.75)
        self.specific_rule.set_color_by_tex("-a", self.INPUT_COLOR)
        self.specific_rule.set_color_by_tex("a", self.INPUT_COLOR)
        self.specific_rule.move_to([3.9, 0.8, 0])

        self.general_rule = MathTex("f(-x)", "=", "f(x)", color=WHITE).scale(0.82)
        self.general_rule.set_color_by_tex("-x", self.INPUT_COLOR)
        self.general_rule.set_color_by_tex("x", self.INPUT_COLOR)
        self.general_rule.move_to([3.9, 0.8, 0])

        self.even_label = Text("even function", font_size=32, color=self.GRAPH_COLOR)
        self.even_label.move_to([3.9, 0.05, 0])

    def step1_create_parabola(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()
        self.play(Create(self.graph), Write(self.graph_label), run_time=2)
        self.wait()

    def step2_highlight_mirror_axis(self):
        self.play(Create(self.mirror_axis), Write(self.mirror_label), run_time=2)
        self.wait()

    def step3_place_right_point(self):
        self.play(FadeIn(self.right_point), Write(self.right_label), run_time=2)
        self.wait()

    def step4_draw_height_guide(self):
        self.play(Create(self.height_guide), Write(self.height_label), run_time=2)
        self.wait()

    def step5_reflect_point(self):
        self.play(
            Create(self.reflection_arrow),
            ReplacementTransform(self.right_point.copy(), self.left_point),
            run_time=2,
        )
        self.wait()

    def step6_label_reflected_point(self):
        self.play(Write(self.left_label), run_time=2)
        self.wait()

    def step7_show_equal_height(self):
        self.play(Indicate(VGroup(self.left_point, self.right_point, self.height_guide), color=self.OUTPUT_COLOR), run_time=2)
        self.wait()

    def step8_write_specific_rule(self):
        self.play(Write(self.specific_rule), run_time=2)
        self.wait()

    def step9_generalize_rule(self):
        self.play(ReplacementTransform(self.specific_rule, self.general_rule), run_time=2)
        self.wait()

    def step10_label_even_function(self):
        self.play(Write(self.even_label), run_time=2)
        self.wait()

    def step11_move_point_pair(self):
        self.play(
            Transform(self.right_point, self.next_right_point),
            Transform(self.left_point, self.next_left_point),
            Transform(self.right_label, self.next_right_label),
            Transform(self.left_label, self.next_left_label),
            Transform(self.height_guide, self.next_height_guide),
            FadeOut(self.reflection_arrow),
            run_time=3,
        )
        self.wait()

    def point_at(self, x_value):
        return self.axes.c2p(x_value, x_value**2)
