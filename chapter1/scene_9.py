from manim import *


class Scene9_IncreasingDecreasingConstant(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    LEFT_COLOR = BLUE
    MID_COLOR = GREEN
    RIGHT_COLOR = TEAL
    DECREASE_COLOR = RED
    INCREASE_COLOR = GREEN
    CONSTANT_COLOR = TEAL

    def construct(self):
        self.setup_layout()
        self.step1_show_piecewise_graph()
        self.step2_show_left_to_right_direction()
        self.step3_highlight_decreasing_interval()
        self.step4_compare_decreasing_points()
        self.step5_label_decreasing()
        self.step6_highlight_increasing_interval()
        self.step7_compare_increasing_points()
        self.step8_label_increasing()
        self.step9_highlight_constant_interval()
        self.step10_compare_constant_points()
        self.step11_label_constant()
        self.step12_summarize_behaviors()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_graph()
        self.create_intervals()
        self.create_direction_arrow()
        self.create_comparison_objects()
        self.create_behavior_labels()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-2.5, 2.8, 1],
            y_range=[-0.5, 2.6, 1],
            x_length=7.0,
            y_length=4.3,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([0, -0.2, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.72)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.72)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_graph(self):
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
        self.graph = VGroup(self.left_piece, self.middle_piece, self.right_piece)

        self.closed_at_zero = Dot(self.axes.c2p(0, 0), radius=0.075, color=self.MID_COLOR)
        self.closed_at_one = Dot(self.axes.c2p(1, 1), radius=0.075, color=self.MID_COLOR)
        self.endpoints = VGroup(self.closed_at_zero, self.closed_at_one)

    def create_intervals(self):
        self.left_interval = self.make_interval(-2.25, 0, self.LEFT_COLOR, "(-\\infty,0]")
        self.middle_interval = self.make_interval(0, 1, self.MID_COLOR, "[0,1]")
        self.right_interval = self.make_interval(1, 2.55, self.RIGHT_COLOR, "[1,\\infty)")
        self.intervals = VGroup(self.left_interval, self.middle_interval, self.right_interval)

    def create_direction_arrow(self):
        self.direction_arrow = Arrow(
            self.axes.c2p(-2.15, -0.36),
            self.axes.c2p(2.35, -0.36),
            color=self.INPUT_COLOR,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.04,
        )
        self.direction_label = MathTex("x_1<x_2", color=self.INPUT_COLOR).scale(0.62)
        self.direction_label.next_to(self.direction_arrow, DOWN, buff=0.12)
        self.direction = VGroup(self.direction_arrow, self.direction_label)

    def create_comparison_objects(self):
        self.decreasing_pair = self.make_pair(-1.75, -0.7, self.DECREASE_COLOR)
        self.increasing_pair = self.make_pair(0.25, 0.8, self.INCREASE_COLOR)
        self.constant_pair = self.make_pair(1.35, 2.15, self.CONSTANT_COLOR)

        self.decreasing_statement = MathTex(
            "f(x_2)", "<", "f(x_1)",
            color=WHITE,
        ).scale(0.68)
        self.decreasing_statement.set_color_by_tex("f(x_2)", self.OUTPUT_COLOR)
        self.decreasing_statement.set_color_by_tex("f(x_1)", self.OUTPUT_COLOR)

        self.increasing_statement = MathTex(
            "f(x_2)", ">", "f(x_1)",
            color=WHITE,
        ).scale(0.68)
        self.increasing_statement.set_color_by_tex("f(x_2)", self.OUTPUT_COLOR)
        self.increasing_statement.set_color_by_tex("f(x_1)", self.OUTPUT_COLOR)

        self.constant_statement = MathTex(
            "f(x_2)", "=", "f(x_1)",
            color=WHITE,
        ).scale(0.68)
        self.constant_statement.set_color_by_tex("f(x_2)", self.OUTPUT_COLOR)
        self.constant_statement.set_color_by_tex("f(x_1)", self.OUTPUT_COLOR)

        self.statements = VGroup(
            self.decreasing_statement,
            self.increasing_statement,
            self.constant_statement,
        )
        self.statements.move_to([4.2, 1.8, 0])

    def create_behavior_labels(self):
        self.decreasing_label = Text("decreasing", font_size=30, color=self.DECREASE_COLOR)
        self.increasing_label = Text("increasing", font_size=30, color=self.INCREASE_COLOR)
        self.constant_label = Text("constant", font_size=30, color=self.CONSTANT_COLOR)

        self.decreasing_label.move_to([4.25, 0.6, 0])
        self.increasing_label.move_to([4.25, 0.6, 0])
        self.constant_label.move_to([4.25, 0.6, 0])

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("decreasing", self.DECREASE_COLOR),
            self.make_summary_card("increasing", self.INCREASE_COLOR),
            self.make_summary_card("constant", self.CONSTANT_COLOR),
        )
        self.summary.arrange(RIGHT, buff=0.35)
        self.summary.to_edge(DOWN, buff=0.32)

    def step1_show_piecewise_graph(self):
        self.play(
            Create(self.axes),
            FadeIn(self.axis_labels),
            Create(self.graph),
            FadeIn(self.endpoints),
            run_time=3,
        )
        self.wait()

    def step2_show_left_to_right_direction(self):
        self.play(Create(self.direction), run_time=2)
        self.wait()

    def step3_highlight_decreasing_interval(self):
        self.play(Create(self.left_interval), Indicate(self.left_piece, color=self.DECREASE_COLOR), run_time=2)
        self.wait()

    def step4_compare_decreasing_points(self):
        self.play(FadeIn(self.decreasing_pair), Write(self.decreasing_statement), run_time=2)
        self.wait()

    def step5_label_decreasing(self):
        self.play(Write(self.decreasing_label), run_time=2)
        self.wait()

    def step6_highlight_increasing_interval(self):
        self.play(
            FadeOut(VGroup(self.decreasing_pair, self.decreasing_statement, self.decreasing_label)),
            Create(self.middle_interval),
            Indicate(self.middle_piece, color=self.INCREASE_COLOR),
            run_time=2,
        )
        self.wait()

    def step7_compare_increasing_points(self):
        self.play(FadeIn(self.increasing_pair), Write(self.increasing_statement), run_time=2)
        self.wait()

    def step8_label_increasing(self):
        self.play(Write(self.increasing_label), run_time=2)
        self.wait()

    def step9_highlight_constant_interval(self):
        self.play(
            FadeOut(VGroup(self.increasing_pair, self.increasing_statement, self.increasing_label)),
            Create(self.right_interval),
            Indicate(self.right_piece, color=self.CONSTANT_COLOR),
            run_time=2,
        )
        self.wait()

    def step10_compare_constant_points(self):
        self.play(FadeIn(self.constant_pair), Write(self.constant_statement), run_time=2)
        self.wait()

    def step11_label_constant(self):
        self.play(Write(self.constant_label), run_time=2)
        self.wait()

    def step12_summarize_behaviors(self):
        self.play(
            FadeOut(VGroup(self.constant_pair, self.constant_statement, self.constant_label)),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def make_curve(self, x_values, func, color):
        points = [self.axes.c2p(x, func(x)) for x in x_values]
        curve = VMobject(color=color, stroke_width=5)
        curve.set_points_smoothly(points)
        return curve

    def make_interval(self, x_start, x_end, color, label_text):
        line = Line(
            self.axes.c2p(x_start, -0.2),
            self.axes.c2p(x_end, -0.2),
            color=color,
            stroke_width=8,
        )
        label = MathTex(label_text, color=color).scale(0.48)
        label.next_to(line, DOWN, buff=0.12)
        return VGroup(line, label)

    def make_pair(self, x1, x2, color):
        point1 = Dot(self.axes.c2p(x1, self.piecewise_value(x1)), radius=0.075, color=color)
        point2 = Dot(self.axes.c2p(x2, self.piecewise_value(x2)), radius=0.075, color=color)
        guide1 = DashedLine(
            self.axes.c2p(x1, 0),
            point1.get_center(),
            color=GREY_B,
            dash_length=0.1,
            stroke_width=3,
        )
        guide2 = DashedLine(
            self.axes.c2p(x2, 0),
            point2.get_center(),
            color=GREY_B,
            dash_length=0.1,
            stroke_width=3,
        )
        arrow = Arrow(
            point1.get_center(),
            point2.get_center(),
            color=color,
            stroke_width=4,
            buff=0.1,
            max_tip_length_to_length_ratio=0.08,
        )
        return VGroup(guide1, guide2, point1, point2, arrow)

    def make_summary_card(self, label, color):
        box = RoundedRectangle(
            width=2.05,
            height=0.48,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.5,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = Text(label, font_size=22, color=color)
        text.move_to(box)
        return VGroup(box, text)

    def piecewise_value(self, x_value):
        if x_value < 0:
            return -x_value
        if x_value <= 1:
            return x_value**2
        return 1
