from manim import *


class Scene14_NegativePowerFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    RECIPROCAL_COLOR = BLUE
    SQUARE_RECIPROCAL_COLOR = GREEN
    ASYMPTOTE_COLOR = GREY_B
    EXCLUDED_COLOR = RED
    HIGHLIGHT_COLOR = YELLOW

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_show_negative_power_form()
        self.step3_mark_excluded_input()
        self.step4_show_asymptotes()
        self.step5_draw_reciprocal_graph()
        self.step6_mark_origin_symmetry()
        self.step7_transform_to_square_reciprocal()
        self.step8_mark_y_axis_symmetry()
        self.step9_show_positive_outputs()
        self.step10_summarize_negative_powers()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_formulas()
        self.create_excluded_input_marker()
        self.create_asymptotes()
        self.create_graphs()
        self.create_symmetry_markers()
        self.create_output_marker()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-3.0, 3.0, 1],
            x_length=7.0,
            y_length=5.2,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-0.9, -0.1, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.7)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.7)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_formulas(self):
        self.negative_power_form = MathTex("x^{-n}", "=", "\\frac{1}{x^n}", color=WHITE)
        self.negative_power_form.set_color_by_tex("x", self.INPUT_COLOR)
        self.negative_power_form.set_color_by_tex("n", self.HIGHLIGHT_COLOR)
        self.negative_power_form.move_to([4.05, 2.35, 0])

        self.reciprocal_label = MathTex("y", "=", "\\frac{1}{x}", color=WHITE).scale(0.68)
        self.reciprocal_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.reciprocal_label.set_color_by_tex("x", self.RECIPROCAL_COLOR)
        self.reciprocal_label.move_to([4.05, 1.45, 0])

        self.square_reciprocal_label = MathTex("y", "=", "\\frac{1}{x^2}", color=WHITE).scale(0.68)
        self.square_reciprocal_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.square_reciprocal_label.set_color_by_tex("x", self.SQUARE_RECIPROCAL_COLOR)
        self.square_reciprocal_label.move_to(self.reciprocal_label)

    def create_excluded_input_marker(self):
        self.forbidden_line = DashedLine(
            self.axes.c2p(0, -2.75),
            self.axes.c2p(0, 2.75),
            color=self.EXCLUDED_COLOR,
            stroke_width=3,
            dash_length=0.18,
        )
        self.forbidden_dot = Dot(self.axes.c2p(0, 0), radius=0.09, color=self.EXCLUDED_COLOR)
        self.forbidden_cross = Cross(
            Circle(radius=0.18, color=self.EXCLUDED_COLOR).move_to(self.axes.c2p(0, 0)),
            stroke_color=self.EXCLUDED_COLOR,
            stroke_width=4,
        )
        self.domain_rule = MathTex("x", "\\ne", "0", color=WHITE).scale(0.75)
        self.domain_rule.set_color_by_tex("x", self.INPUT_COLOR)
        self.domain_rule.set_color_by_tex("0", self.EXCLUDED_COLOR)
        self.domain_rule.move_to([4.05, 0.75, 0])
        self.excluded_input = VGroup(self.forbidden_line, self.forbidden_dot, self.forbidden_cross)

    def create_asymptotes(self):
        self.horizontal_asymptote = DashedLine(
            self.axes.c2p(-3.05, 0),
            self.axes.c2p(3.05, 0),
            color=self.ASYMPTOTE_COLOR,
            stroke_width=2.5,
            dash_length=0.16,
        )
        self.vertical_asymptote = DashedLine(
            self.axes.c2p(0, -2.75),
            self.axes.c2p(0, 2.75),
            color=self.ASYMPTOTE_COLOR,
            stroke_width=2.5,
            dash_length=0.16,
        )
        self.asymptotes = VGroup(self.horizontal_asymptote, self.vertical_asymptote)
        self.asymptote_label = Text("approaches axes", font_size=23, color=self.ASYMPTOTE_COLOR)
        self.asymptote_label.move_to([4.25, -0.72, 0])

    def create_graphs(self):
        self.reciprocal_graph = VGroup(
            self.make_graph_branch(lambda x: 1 / x, -3.0, -0.36, self.RECIPROCAL_COLOR),
            self.make_graph_branch(lambda x: 1 / x, 0.36, 3.0, self.RECIPROCAL_COLOR),
        )

        self.square_reciprocal_graph = VGroup(
            self.make_graph_branch(lambda x: 1 / (x * x), -3.0, -0.6, self.SQUARE_RECIPROCAL_COLOR),
            self.make_graph_branch(lambda x: 1 / (x * x), 0.6, 3.0, self.SQUARE_RECIPROCAL_COLOR),
        )

    def create_symmetry_markers(self):
        self.origin_point_a = Dot(
            self.axes.c2p(1.0, 1.0),
            radius=0.08,
            color=self.RECIPROCAL_COLOR,
        )
        self.origin_point_b = Dot(
            self.axes.c2p(-1.0, -1.0),
            radius=0.08,
            color=self.RECIPROCAL_COLOR,
        )
        self.origin_symmetry_arrow = CurvedArrow(
            self.axes.c2p(1.0, 1.0),
            self.axes.c2p(-1.0, -1.0),
            angle=TAU / 3,
            color=self.RECIPROCAL_COLOR,
            stroke_width=3,
        )
        self.origin_symmetry_marker = VGroup(
            self.origin_point_a,
            self.origin_point_b,
            self.origin_symmetry_arrow,
        )
        self.origin_symmetry_label = Text("origin symmetry", font_size=25, color=self.RECIPROCAL_COLOR)
        self.origin_symmetry_label.move_to([4.25, -1.2, 0])

        self.y_axis_symmetry_line = Line(
            self.axes.c2p(0, 0),
            self.axes.c2p(0, 2.65),
            color=self.SQUARE_RECIPROCAL_COLOR,
            stroke_width=4,
        )
        self.y_axis_symmetry_label = Text("y-axis symmetry", font_size=25, color=self.SQUARE_RECIPROCAL_COLOR)
        self.y_axis_symmetry_label.move_to(self.origin_symmetry_label)

    def create_output_marker(self):
        self.positive_output_region = Polygon(
            self.axes.c2p(-3.05, 0.02),
            self.axes.c2p(3.05, 0.02),
            self.axes.c2p(3.05, 2.85),
            self.axes.c2p(-3.05, 2.85),
            stroke_width=0,
            fill_color=self.OUTPUT_COLOR,
            fill_opacity=0.1,
        )
        self.positive_output_arrow = Arrow(
            self.axes.c2p(-2.85, 0.35),
            self.axes.c2p(-2.85, 1.4),
            color=self.OUTPUT_COLOR,
            stroke_width=4,
            buff=0,
            max_tip_length_to_length_ratio=0.18,
        )
        self.positive_output_label = MathTex("y", ">", "0", color=WHITE).scale(0.75)
        self.positive_output_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.positive_output_label.set_color_by_tex("0", self.OUTPUT_COLOR)
        self.positive_output_label.move_to([4.22, -1.7, 0])
        self.positive_outputs = VGroup(
            self.positive_output_region,
            self.positive_output_arrow,
            self.positive_output_label,
        )

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("x != 0", self.EXCLUDED_COLOR, width=1.3),
            self.make_summary_card("axes are limits", self.ASYMPTOTE_COLOR, width=1.9),
            self.make_summary_card("symmetry differs", self.HIGHLIGHT_COLOR, width=2.25),
        )
        self.summary.arrange(RIGHT, buff=0.22)
        self.summary.to_edge(DOWN, buff=0.28)

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_show_negative_power_form(self):
        self.play(Write(self.negative_power_form), run_time=2)
        self.wait()

    def step3_mark_excluded_input(self):
        self.play(FadeIn(self.excluded_input), Write(self.domain_rule), run_time=2)
        self.wait()

    def step4_show_asymptotes(self):
        self.play(
            ReplacementTransform(self.excluded_input, self.vertical_asymptote),
            Create(self.horizontal_asymptote),
            run_time=2,
        )
        self.wait()

    def step5_draw_reciprocal_graph(self):
        self.play(Create(self.reciprocal_graph), Write(self.reciprocal_label), run_time=3)
        self.wait()

    def step6_mark_origin_symmetry(self):
        self.play(Write(self.asymptote_label), run_time=2)
        self.wait()
        self.play(FadeIn(self.origin_symmetry_marker), Write(self.origin_symmetry_label), run_time=2)
        self.wait()

    def step7_transform_to_square_reciprocal(self):
        self.play(
            ReplacementTransform(self.reciprocal_graph, self.square_reciprocal_graph),
            ReplacementTransform(self.reciprocal_label, self.square_reciprocal_label),
            FadeOut(self.origin_symmetry_marker),
            run_time=3,
        )
        self.wait()

    def step8_mark_y_axis_symmetry(self):
        self.play(
            Create(self.y_axis_symmetry_line),
            ReplacementTransform(self.origin_symmetry_label, self.y_axis_symmetry_label),
            run_time=2,
        )
        self.wait()

    def step9_show_positive_outputs(self):
        self.play(FadeIn(self.positive_outputs), run_time=2)
        self.wait()

    def step10_summarize_negative_powers(self):
        self.play(
            FadeOut(self.y_axis_symmetry_line),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def make_graph_branch(self, function, x_start, x_end, color):
        points = []
        samples = 120
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            if -2.85 <= y <= 2.85:
                points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=4)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_summary_card(self, label, color, width=1.7):
        box = RoundedRectangle(
            width=width,
            height=0.48,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.5,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = Text(label, font_size=19, color=color)
        text.move_to(box)
        return VGroup(box, text)
