from manim import *


class Scene7_VerticalLineTest(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    GRAPH_COLOR = BLUE
    TEST_COLOR = YELLOW
    VALID_COLOR = GREEN
    ERROR_COLOR = RED

    def construct(self):
        self.setup_layout()
        self.step1_create_valid_graph()
        self.step2_place_vertical_test_line()
        self.step3_show_single_intersection()
        self.step4_mark_valid_graph()
        self.step5_scan_valid_graph()
        self.step6_transform_to_circle()
        self.step7_place_line_through_circle()
        self.step8_show_two_intersections()
        self.step9_mark_circle_invalid()
        self.step10_split_into_semicircles()
        self.step11_test_upper_semicircle()
        self.step12_state_rule()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_valid_graph()
        self.create_circle_graph()
        self.create_semicircles()
        self.create_test_objects()
        self.create_labels()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1.7, 1.7, 1],
            x_length=6.8,
            y_length=4.8,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([0, -0.25, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.75)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.75)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_valid_graph(self):
        points = [self.axes.c2p(x / 40, self.valid_func(x / 40)) for x in range(-60, 61)]
        self.valid_graph = VMobject(color=self.GRAPH_COLOR, stroke_width=4)
        self.valid_graph.set_points_smoothly(points)
        self.valid_label = MathTex("y=f(x)", color=WHITE).scale(0.75)
        self.valid_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.valid_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.valid_label.move_to([0, 3.1, 0])

    def create_circle_graph(self):
        self.circle = Circle(radius=self.axes.x_axis.unit_size, color=self.GRAPH_COLOR, stroke_width=4)
        self.circle.move_to(self.axes.c2p(0, 0))
        self.circle_label = MathTex("x^2+y^2=1", color=WHITE).scale(0.72)
        self.circle_label.move_to([0, 3.1, 0])

    def create_semicircles(self):
        upper_points = [self.axes.c2p(x / 50, self.upper_circle(x / 50)) for x in range(-50, 51)]
        lower_points = [self.axes.c2p(x / 50, -self.upper_circle(x / 50)) for x in range(-50, 51)]

        self.upper_semicircle = VMobject(color=self.VALID_COLOR, stroke_width=5)
        self.upper_semicircle.set_points_smoothly(upper_points)
        self.lower_semicircle = VMobject(color=GREY_B, stroke_width=4)
        self.lower_semicircle.set_points_smoothly(lower_points)

        self.upper_label = MathTex(r"y=\sqrt{1-x^2}", color=self.VALID_COLOR).scale(0.62)
        self.upper_label.next_to(self.upper_semicircle, UP, buff=0.3)

    def create_test_objects(self):
        self.test_x = 0.45
        self.scan_x = 1.15

        self.test_line = self.make_test_line(self.test_x)
        self.scanned_test_line = self.make_test_line(self.scan_x)
        self.circle_test_line = self.make_test_line(self.test_x)

        self.input_marker = Dot(self.axes.c2p(self.test_x, 0), radius=0.07, color=self.INPUT_COLOR)
        self.input_label = MathTex("x=a", color=self.INPUT_COLOR).scale(0.7)
        self.input_label.next_to(self.input_marker, DOWN, buff=0.18)

        self.valid_point = Dot(
            self.axes.c2p(self.test_x, self.valid_func(self.test_x)),
            radius=0.08,
            color=self.VALID_COLOR,
        )
        self.valid_point_label = MathTex("(a,f(a))", color=WHITE).scale(0.6)
        self.valid_point_label.next_to(self.valid_point, RIGHT, buff=0.15)

        self.scan_point = Dot(
            self.axes.c2p(self.scan_x, self.valid_func(self.scan_x)),
            radius=0.08,
            color=self.VALID_COLOR,
        )
        self.scan_point_label = MathTex(r"\text{still one}", color=self.VALID_COLOR).scale(0.55)
        self.scan_point_label.next_to(self.scan_point, RIGHT, buff=0.15)

        self.circle_top_point = Dot(
            self.axes.c2p(self.test_x, self.upper_circle(self.test_x)),
            radius=0.08,
            color=self.ERROR_COLOR,
        )
        self.circle_bottom_point = Dot(
            self.axes.c2p(self.test_x, -self.upper_circle(self.test_x)),
            radius=0.08,
            color=self.ERROR_COLOR,
        )
        self.two_points = VGroup(self.circle_top_point, self.circle_bottom_point)

        self.upper_test_point = Dot(
            self.axes.c2p(self.test_x, self.upper_circle(self.test_x)),
            radius=0.08,
            color=self.VALID_COLOR,
        )

    def create_labels(self):
        self.check_mark = MathTex(r"\checkmark", color=self.VALID_COLOR).scale(1.4)
        self.check_text = Text("one input, one output", font_size=28, color=self.VALID_COLOR)
        self.valid_badge = VGroup(self.check_mark, self.check_text).arrange(RIGHT, buff=0.25)
        self.valid_badge.to_corner(UR, buff=0.45)

        self.cross_mark = MathTex(r"\times", color=self.ERROR_COLOR).scale(1.6)
        self.cross_text = Text("one input, two outputs", font_size=28, color=self.ERROR_COLOR)
        self.invalid_badge = VGroup(self.cross_mark, self.cross_text).arrange(RIGHT, buff=0.25)
        self.invalid_badge.to_corner(UR, buff=0.45)

        self.rule = MathTex(
            r"\text{vertical line hits}",
            r"\leq",
            r"\text{one point}",
            color=WHITE,
        )
        self.rule.set_color_by_tex("one point", self.VALID_COLOR)
        self.rule.scale(0.72)
        self.rule.to_edge(DOWN, buff=0.35)

    def step1_create_valid_graph(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()
        self.play(Create(self.valid_graph), Write(self.valid_label), run_time=2)
        self.wait()

    def step2_place_vertical_test_line(self):
        self.play(Create(self.test_line), FadeIn(VGroup(self.input_marker, self.input_label)), run_time=2)
        self.wait()

    def step3_show_single_intersection(self):
        self.play(FadeIn(self.valid_point), Write(self.valid_point_label), run_time=2)
        self.wait()

    def step4_mark_valid_graph(self):
        self.play(FadeIn(self.valid_badge), Indicate(self.valid_point, color=self.VALID_COLOR), run_time=2)
        self.wait()

    def step5_scan_valid_graph(self):
        self.play(
            Transform(self.test_line, self.scanned_test_line),
            Transform(self.input_marker, Dot(self.axes.c2p(self.scan_x, 0), radius=0.07, color=self.INPUT_COLOR)),
            Transform(self.input_label, MathTex("x=b", color=self.INPUT_COLOR).scale(0.7).next_to(self.axes.c2p(self.scan_x, 0), DOWN, buff=0.18)),
            Transform(self.valid_point, self.scan_point),
            ReplacementTransform(self.valid_point_label, self.scan_point_label),
            run_time=3,
        )
        self.wait()

    def step6_transform_to_circle(self):
        self.play(
            ReplacementTransform(self.valid_graph, self.circle),
            ReplacementTransform(self.valid_label, self.circle_label),
            FadeOut(VGroup(self.valid_badge, self.valid_point, self.scan_point_label)),
            run_time=3,
        )
        self.wait()

    def step7_place_line_through_circle(self):
        self.play(
            Transform(self.test_line, self.circle_test_line),
            Transform(self.input_marker, Dot(self.axes.c2p(self.test_x, 0), radius=0.07, color=self.INPUT_COLOR)),
            Transform(self.input_label, MathTex("x=a", color=self.INPUT_COLOR).scale(0.7).next_to(self.axes.c2p(self.test_x, 0), DOWN, buff=0.18)),
            run_time=2,
        )
        self.wait()

    def step8_show_two_intersections(self):
        self.play(FadeIn(self.two_points), run_time=2)
        self.wait()

    def step9_mark_circle_invalid(self):
        self.play(FadeIn(self.invalid_badge), Indicate(self.two_points, color=self.ERROR_COLOR), run_time=2)
        self.wait()

    def step10_split_into_semicircles(self):
        self.play(
            ReplacementTransform(self.circle, VGroup(self.upper_semicircle, self.lower_semicircle)),
            ReplacementTransform(self.circle_label, self.upper_label),
            FadeOut(VGroup(self.invalid_badge, self.two_points)),
            run_time=3,
        )
        self.wait()

    def step11_test_upper_semicircle(self):
        self.play(
            FadeOut(self.lower_semicircle),
            FadeIn(self.upper_test_point),
            FadeIn(self.valid_badge),
            run_time=2,
        )
        self.wait()

    def step12_state_rule(self):
        self.play(Write(self.rule), Indicate(self.test_line, color=self.TEST_COLOR), run_time=2)
        self.wait()

    def valid_func(self, x):
        return 0.28 * x**2 + 0.35 * x + 0.15

    def upper_circle(self, x):
        return (1 - x**2) ** 0.5

    def make_test_line(self, x_value):
        return DashedLine(
            self.axes.c2p(x_value, -1.35),
            self.axes.c2p(x_value, 1.35),
            color=self.TEST_COLOR,
            dash_length=0.12,
            stroke_width=4,
        )
