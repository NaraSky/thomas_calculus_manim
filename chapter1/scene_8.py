from manim import *


class Scene8_PiecewiseFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    LEFT_COLOR = BLUE
    MID_COLOR = GREEN
    RIGHT_COLOR = TEAL
    TEST_COLOR = YELLOW

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_highlight_left_interval()
        self.step3_draw_left_piece()
        self.step4_highlight_middle_interval()
        self.step5_draw_middle_piece()
        self.step6_highlight_right_interval()
        self.step7_draw_right_piece()
        self.step8_add_endpoint_dots()
        self.step9_write_piecewise_formula()
        self.step10_scan_combined_graph()
        self.step11_emphasize_one_piece_per_input()
        self.step12_state_rule()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_intervals()
        self.create_graph_pieces()
        self.create_endpoint_dots()
        self.create_formula()
        self.create_test_objects()
        self.create_rule()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-2.5, 2.8, 1],
            y_range=[-0.5, 2.6, 1],
            x_length=6.5,
            y_length=4.2,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.15, -0.15, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.72)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.72)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_intervals(self):
        self.left_interval = self.make_interval(-2.25, 0, self.LEFT_COLOR, "x<0")
        self.middle_interval = self.make_interval(0, 1, self.MID_COLOR, "0\\le x\\le 1")
        self.right_interval = self.make_interval(1, 2.55, self.RIGHT_COLOR, "x>1")
        self.intervals = VGroup(self.left_interval, self.middle_interval, self.right_interval)

    def create_graph_pieces(self):
        self.left_piece = self.make_curve(
            [-2.2 + i * 0.04 for i in range(56)],
            lambda x: -x,
            self.LEFT_COLOR,
        )
        self.middle_piece = self.make_curve(
            [i * 0.025 for i in range(41)],
            lambda x: x**2,
            self.MID_COLOR,
        )
        self.right_piece = Line(
            self.axes.c2p(1.02, 1),
            self.axes.c2p(2.55, 1),
            color=self.RIGHT_COLOR,
            stroke_width=5,
        )
        self.graph_pieces = VGroup(self.left_piece, self.middle_piece, self.right_piece)

    def create_endpoint_dots(self):
        self.open_at_zero = Circle(radius=0.09, color=self.LEFT_COLOR, stroke_width=3)
        self.open_at_zero.move_to(self.axes.c2p(0, 0))

        self.closed_at_zero = Dot(self.axes.c2p(0, 0), radius=0.075, color=self.MID_COLOR)
        self.closed_at_one = Dot(self.axes.c2p(1, 1), radius=0.075, color=self.MID_COLOR)

        self.open_at_one = Circle(radius=0.09, color=self.RIGHT_COLOR, stroke_width=3)
        self.open_at_one.move_to(self.axes.c2p(1, 1))

        self.endpoints = VGroup(
            self.open_at_zero,
            self.closed_at_zero,
            self.closed_at_one,
            self.open_at_one,
        )

    def create_formula(self):
        self.formula = MathTex(
            r"f(x)=",
            r"\begin{cases}",
            r"-x, & x<0\\",
            r"x^2, & 0\le x\le 1\\",
            r"1, & x>1",
            r"\end{cases}",
            color=WHITE,
        )
        self.formula.scale(0.62)
        self.formula.move_to([4.25, 0.55, 0])
        self.formula.set_color_by_tex("-x", self.LEFT_COLOR)
        self.formula.set_color_by_tex("x^2", self.MID_COLOR)
        self.formula.set_color_by_tex("1,", self.RIGHT_COLOR)

    def create_test_objects(self):
        self.test_positions = [-1.25, 0.55, 1.75]
        self.test_line = self.make_test_line(self.test_positions[0])
        self.test_lines = [self.make_test_line(x) for x in self.test_positions]
        self.test_points = VGroup(*[
            Dot(self.axes.c2p(x, self.piecewise_value(x)), radius=0.075, color=self.OUTPUT_COLOR)
            for x in self.test_positions
        ])
        self.test_labels = VGroup(*[
            MathTex(r"\text{one piece}", color=self.OUTPUT_COLOR).scale(0.5)
            for _ in self.test_positions
        ])
        for point, label in zip(self.test_points, self.test_labels):
            label.next_to(point, UP + RIGHT, buff=0.1)

    def create_rule(self):
        self.rule = MathTex(
            r"\text{different formulas}",
            r"\longrightarrow",
            r"\text{one output per input}",
            color=WHITE,
        )
        self.rule.set_color_by_tex("one output", self.OUTPUT_COLOR)
        self.rule.set_color_by_tex("input", self.INPUT_COLOR)
        self.rule.scale(0.66)
        self.rule.to_edge(DOWN, buff=0.35)

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_highlight_left_interval(self):
        self.play(Create(self.left_interval), run_time=2)
        self.wait()

    def step3_draw_left_piece(self):
        self.play(Create(self.left_piece), run_time=2)
        self.wait()

    def step4_highlight_middle_interval(self):
        self.play(Create(self.middle_interval), run_time=2)
        self.wait()

    def step5_draw_middle_piece(self):
        self.play(Create(self.middle_piece), run_time=2)
        self.wait()

    def step6_highlight_right_interval(self):
        self.play(Create(self.right_interval), run_time=2)
        self.wait()

    def step7_draw_right_piece(self):
        self.play(Create(self.right_piece), run_time=2)
        self.wait()

    def step8_add_endpoint_dots(self):
        self.play(FadeIn(self.endpoints), run_time=2)
        self.wait()

    def step9_write_piecewise_formula(self):
        self.play(Write(self.formula), run_time=3)
        self.wait()

    def step10_scan_combined_graph(self):
        self.play(Create(self.test_line), FadeIn(self.test_points[0]), Write(self.test_labels[0]), run_time=2)
        self.wait()
        self.play(
            Transform(self.test_line, self.test_lines[1]),
            Transform(self.test_points[0], self.test_points[1]),
            Transform(self.test_labels[0], self.test_labels[1]),
            run_time=2,
        )
        self.wait()
        self.play(
            Transform(self.test_line, self.test_lines[2]),
            Transform(self.test_points[0], self.test_points[2]),
            Transform(self.test_labels[0], self.test_labels[2]),
            run_time=2,
        )
        self.wait()

    def step11_emphasize_one_piece_per_input(self):
        self.play(
            Indicate(self.graph_pieces, color=self.OUTPUT_COLOR),
            Indicate(VGroup(self.test_line, self.test_points[0]), color=self.TEST_COLOR),
            run_time=2,
        )
        self.wait()

    def step12_state_rule(self):
        self.play(Write(self.rule), run_time=2)
        self.wait()

    def make_interval(self, x_start, x_end, color, label_text):
        line = Line(
            self.axes.c2p(x_start, -0.18),
            self.axes.c2p(x_end, -0.18),
            color=color,
            stroke_width=8,
        )
        label = MathTex(label_text, color=color).scale(0.48)
        label.next_to(line, DOWN, buff=0.14)
        return VGroup(line, label)

    def make_curve(self, x_values, func, color):
        points = [self.axes.c2p(x, func(x)) for x in x_values]
        curve = VMobject(color=color, stroke_width=5)
        curve.set_points_smoothly(points)
        return curve

    def make_test_line(self, x_value):
        return DashedLine(
            self.axes.c2p(x_value, -0.28),
            self.axes.c2p(x_value, self.piecewise_value(x_value)),
            color=self.TEST_COLOR,
            dash_length=0.12,
            stroke_width=4,
        )

    def piecewise_value(self, x_value):
        if x_value < 0:
            return -x_value
        if x_value <= 1:
            return x_value**2
        return 1
