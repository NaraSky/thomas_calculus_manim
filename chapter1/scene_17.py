from manim import *


class Scene17_RationalFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    NUMERATOR_COLOR = BLUE
    DENOMINATOR_COLOR = RED
    CURVE_COLOR = TEAL
    ASYMPTOTE_COLOR = GREY_B
    HIGHLIGHT_COLOR = YELLOW

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_write_rational_form()
        self.step3_show_example_quotient()
        self.step4_highlight_denominator()
        self.step5_mark_excluded_input()
        self.step6_show_vertical_asymptote()
        self.step7_draw_rational_graph()
        self.step8_show_horizontal_asymptote()
        self.step9_show_approach_behavior()
        self.step10_summarize_rational_functions()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_formulas()
        self.create_denominator_marker()
        self.create_asymptotes()
        self.create_graph()
        self.create_approach_markers()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-3.0, 4.0, 1],
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
        self.axes.move_to([-1.05, -0.08, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.7)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.7)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_formulas(self):
        self.rational_form = MathTex("f(x)", "=", "\\frac{p(x)}{q(x)}", color=WHITE)
        self.rational_form.set_color_by_tex("x", self.INPUT_COLOR)
        self.rational_form.move_to([3.65, 2.25, 0])

        self.example_formula = MathTex(
            "f(x)",
            "=",
            "\\frac{x}{x-1}",
            color=WHITE,
            substrings_to_isolate=["x-1"],
        ).scale(0.72)
        self.example_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.example_formula.move_to([3.65, 1.35, 0])

        self.domain_rule = MathTex("q(x)", "\\ne", "0", color=WHITE).scale(0.72)
        self.domain_rule.set_color_by_tex("x", self.INPUT_COLOR)
        self.domain_rule.set_color_by_tex("0", self.DENOMINATOR_COLOR)
        self.domain_rule.move_to([3.65, 0.55, 0])

        self.excluded_rule = MathTex("\\text{domain: }", "x", "\\ne", "1", color=WHITE).scale(0.72)
        self.excluded_rule.set_color_by_tex("x", self.INPUT_COLOR)
        self.excluded_rule.set_color_by_tex("1", self.DENOMINATOR_COLOR)
        self.excluded_rule.move_to(self.domain_rule)

    def create_denominator_marker(self):
        self.denominator_box = SurroundingRectangle(
            self.example_formula[2],
            color=self.DENOMINATOR_COLOR,
            buff=0.08,
        )
        self.denominator_label = VGroup(
            Text("denominator", font_size=18, color=self.DENOMINATOR_COLOR),
            Text("controls domain", font_size=18, color=self.DENOMINATOR_COLOR),
        )
        self.denominator_label.arrange(DOWN, buff=0.04, aligned_edge=LEFT)
        self.denominator_label.next_to(self.denominator_box, RIGHT, buff=0.18)

    def create_asymptotes(self):
        self.vertical_asymptote = DashedLine(
            self.axes.c2p(1, -2.75),
            self.axes.c2p(1, 2.75),
            color=self.DENOMINATOR_COLOR,
            stroke_width=3,
            dash_length=0.18,
        )
        self.horizontal_asymptote = DashedLine(
            self.axes.c2p(-2.85, 1),
            self.axes.c2p(3.85, 1),
            color=self.ASYMPTOTE_COLOR,
            stroke_width=3,
            dash_length=0.18,
        )

        self.vertical_label = MathTex("x", "=", "1", color=WHITE).scale(0.58)
        self.vertical_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.vertical_label.set_color_by_tex("1", self.DENOMINATOR_COLOR)
        self.vertical_label.next_to(self.vertical_asymptote, UP, buff=0.08)

        self.horizontal_label = MathTex("y", "=", "1", color=WHITE).scale(0.58)
        self.horizontal_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.horizontal_label.next_to(self.horizontal_asymptote, RIGHT, buff=0.12)

    def create_graph(self):
        self.rational_graph = VGroup(
            self.make_graph_branch(self.rational_function, -2.8, 0.82, self.CURVE_COLOR),
            self.make_graph_branch(self.rational_function, 1.18, 3.8, self.CURVE_COLOR),
        )

    def create_approach_markers(self):
        self.approach_arrows = VGroup(
            Arrow(
                self.axes.c2p(2.5, 1.35),
                self.axes.c2p(3.4, 1.12),
                color=self.HIGHLIGHT_COLOR,
                stroke_width=4,
                buff=0,
                max_tip_length_to_length_ratio=0.18,
            ),
            Arrow(
                self.axes.c2p(-1.9, 0.72),
                self.axes.c2p(-2.65, 0.92),
                color=self.HIGHLIGHT_COLOR,
                stroke_width=4,
                buff=0,
                max_tip_length_to_length_ratio=0.18,
            ),
        )
        self.approach_label = Text("approaches, never becomes", font_size=22, color=self.HIGHLIGHT_COLOR)
        self.approach_label.move_to([3.65, -0.92, 0])

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("quotient", self.NUMERATOR_COLOR, width=1.3),
            self.make_summary_card("q(x) != 0", self.DENOMINATOR_COLOR, width=1.55),
            self.make_summary_card("asymptotes", self.HIGHLIGHT_COLOR, width=1.55),
        )
        self.summary.arrange(RIGHT, buff=0.2)
        self.summary.to_edge(DOWN, buff=0.36)

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_write_rational_form(self):
        self.play(Write(self.rational_form), run_time=2)
        self.wait()

    def step3_show_example_quotient(self):
        self.play(Write(self.example_formula), run_time=2)
        self.wait()

    def step4_highlight_denominator(self):
        self.play(Create(self.denominator_box), Write(self.denominator_label), run_time=2)
        self.wait()

    def step5_mark_excluded_input(self):
        self.play(Write(self.domain_rule), run_time=2)
        self.wait()
        self.play(ReplacementTransform(self.domain_rule, self.excluded_rule), run_time=2)
        self.wait()

    def step6_show_vertical_asymptote(self):
        self.play(Create(self.vertical_asymptote), Write(self.vertical_label), run_time=2)
        self.wait()

    def step7_draw_rational_graph(self):
        self.play(Create(self.rational_graph), run_time=3)
        self.wait()

    def step8_show_horizontal_asymptote(self):
        self.play(Create(self.horizontal_asymptote), Write(self.horizontal_label), run_time=2)
        self.wait()

    def step9_show_approach_behavior(self):
        self.play(FadeIn(self.approach_arrows), Write(self.approach_label), run_time=2)
        self.wait()

    def step10_summarize_rational_functions(self):
        self.play(
            FadeOut(self.denominator_box),
            FadeOut(self.denominator_label),
            FadeOut(self.approach_arrows),
            FadeOut(self.approach_label),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def rational_function(self, x):
        return x / (x - 1)

    def make_graph_branch(self, function, x_start, x_end, color):
        points = []
        samples = 140
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
            height=0.5,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.4,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = Text(label, font_size=17, color=color)
        text.move_to(box)
        return VGroup(box, text)
