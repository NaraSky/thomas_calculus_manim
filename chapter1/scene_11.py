from manim import *


class Scene11_OddFunctionsOriginSymmetry(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    GRAPH_COLOR = BLUE
    ORIGIN_COLOR = YELLOW
    POINT_COLOR = GREEN
    NEGATIVE_COLOR = RED

    def construct(self):
        self.setup_layout()
        self.step1_create_cubic_graph()
        self.step2_highlight_origin()
        self.step3_place_right_point()
        self.step4_draw_origin_line()
        self.step5_rotate_point_through_origin()
        self.step6_label_opposite_point()
        self.step7_show_opposite_outputs()
        self.step8_write_specific_rule()
        self.step9_generalize_rule()
        self.step10_label_odd_function()
        self.step11_move_point_pair()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.a = 1.25
        self.b = 1.42
        self.create_axes()
        self.create_graph()
        self.create_origin_marker()
        self.create_points()
        self.create_guides()
        self.create_rules()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-2.2, 2.2, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=7.0,
            y_length=5.2,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-0.95, 0, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.72)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.72)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_graph(self):
        points = [self.axes.c2p(x / 50, (x / 50) ** 3) for x in range(-75, 76)]
        self.graph = VMobject(color=self.GRAPH_COLOR, stroke_width=4)
        self.graph.set_points_smoothly(points)

        self.graph_label = MathTex("y=x^3", color=WHITE).scale(0.75)
        self.graph_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.graph_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.graph_label.move_to([0, 3.25, 0])

    def create_origin_marker(self):
        self.origin_dot = Dot(self.axes.c2p(0, 0), radius=0.08, color=self.ORIGIN_COLOR)
        self.origin_label = Text("origin", font_size=26, color=self.ORIGIN_COLOR)
        self.origin_label.next_to(self.origin_dot, DOWN + LEFT, buff=0.18)

    def create_points(self):
        self.right_point = Dot(self.point_at(self.a), radius=0.08, color=self.POINT_COLOR)
        self.right_label = MathTex("(a,f(a))", color=WHITE).scale(0.58)
        self.right_label.next_to(self.right_point, UP + RIGHT, buff=0.1)

        self.left_point = Dot(self.point_at(-self.a), radius=0.08, color=self.POINT_COLOR)
        self.left_label = MathTex("(-a,-f(a))", color=WHITE).scale(0.58)
        self.left_label.next_to(self.left_point, DOWN + LEFT, buff=0.1)

        self.next_right_point = Dot(self.point_at(self.b), radius=0.08, color=self.POINT_COLOR)
        self.next_left_point = Dot(self.point_at(-self.b), radius=0.08, color=self.POINT_COLOR)
        self.next_right_label = MathTex("(b,f(b))", color=WHITE).scale(0.58)
        self.next_left_label = MathTex("(-b,-f(b))", color=WHITE).scale(0.58)
        self.next_right_label.next_to(self.next_right_point, UP + RIGHT, buff=0.1)
        self.next_left_label.next_to(self.next_left_point, DOWN + LEFT, buff=0.1)

    def create_guides(self):
        self.diameter_line = DashedLine(
            self.point_at(-self.a),
            self.point_at(self.a),
            color=self.ORIGIN_COLOR,
            dash_length=0.12,
            stroke_width=3,
        )
        self.rotation_arrow = CurvedArrow(
            self.point_at(self.a) + 0.25 * RIGHT,
            self.point_at(-self.a) + 0.25 * LEFT,
            angle=-TAU / 2,
            color=self.ORIGIN_COLOR,
            stroke_width=4,
        )
        self.output_pair = VGroup(
            MathTex("f(a)", color=self.OUTPUT_COLOR).scale(0.62),
            MathTex("-f(a)", color=self.NEGATIVE_COLOR).scale(0.62),
        )
        self.output_pair.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.output_pair.move_to([3.85, 1.55, 0])

        self.next_diameter_line = DashedLine(
            self.point_at(-self.b),
            self.point_at(self.b),
            color=self.ORIGIN_COLOR,
            dash_length=0.12,
            stroke_width=3,
        )

    def create_rules(self):
        self.specific_rule = MathTex("f(-a)", "=", "-f(a)", color=WHITE).scale(0.75)
        self.specific_rule.set_color_by_tex("-a", self.INPUT_COLOR)
        self.specific_rule.set_color_by_tex("-f(a)", self.NEGATIVE_COLOR)
        self.specific_rule.move_to([3.85, 0.55, 0])

        self.general_rule = MathTex("f(-x)", "=", "-f(x)", color=WHITE).scale(0.82)
        self.general_rule.set_color_by_tex("-x", self.INPUT_COLOR)
        self.general_rule.set_color_by_tex("-f(x)", self.NEGATIVE_COLOR)
        self.general_rule.move_to([3.85, 0.55, 0])

        self.odd_label = Text("odd function", font_size=32, color=self.GRAPH_COLOR)
        self.odd_label.move_to([3.85, -0.2, 0])

    def step1_create_cubic_graph(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()
        self.play(Create(self.graph), Write(self.graph_label), run_time=2)
        self.wait()

    def step2_highlight_origin(self):
        self.play(FadeIn(self.origin_dot), Write(self.origin_label), run_time=2)
        self.wait()

    def step3_place_right_point(self):
        self.play(FadeIn(self.right_point), Write(self.right_label), run_time=2)
        self.wait()

    def step4_draw_origin_line(self):
        self.play(Create(self.diameter_line), run_time=2)
        self.wait()

    def step5_rotate_point_through_origin(self):
        self.play(
            Create(self.rotation_arrow),
            ReplacementTransform(self.right_point.copy(), self.left_point),
            run_time=2,
        )
        self.wait()

    def step6_label_opposite_point(self):
        self.play(Write(self.left_label), run_time=2)
        self.wait()

    def step7_show_opposite_outputs(self):
        self.play(Write(self.output_pair), Indicate(VGroup(self.left_point, self.right_point), color=self.OUTPUT_COLOR), run_time=2)
        self.wait()

    def step8_write_specific_rule(self):
        self.play(Write(self.specific_rule), run_time=2)
        self.wait()

    def step9_generalize_rule(self):
        self.play(ReplacementTransform(self.specific_rule, self.general_rule), run_time=2)
        self.wait()

    def step10_label_odd_function(self):
        self.play(Write(self.odd_label), run_time=2)
        self.wait()

    def step11_move_point_pair(self):
        self.play(
            Transform(self.right_point, self.next_right_point),
            Transform(self.left_point, self.next_left_point),
            Transform(self.right_label, self.next_right_label),
            Transform(self.left_label, self.next_left_label),
            Transform(self.diameter_line, self.next_diameter_line),
            FadeOut(self.rotation_arrow),
            run_time=3,
        )
        self.wait()

    def point_at(self, x_value):
        return self.axes.c2p(x_value, x_value**3)
