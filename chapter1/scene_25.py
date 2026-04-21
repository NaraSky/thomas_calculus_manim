from manim import *


class Scene25_FunctionSubtraction(Scene):
    INPUT_COLOR = YELLOW
    F_COLOR = TEAL
    G_COLOR = GREEN
    DIFF_COLOR = BLUE
    ZERO_COLOR = GREY_B
    DOMAIN_COLOR = RED

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_draw_original_functions()
        self.step3_choose_same_input()
        self.step4_show_two_heights()
        self.step5_show_signed_difference()
        self.step6_trace_difference_graph()
        self.step7_mark_zero_crossing()
        self.step8_summarize_subtraction()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.sample_x = 0.81

        self.create_axes()
        self.create_formulas()
        self.create_graphs()
        self.create_sample_objects()
        self.create_zero_marker()
        self.create_domain_marker()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-0.2, 1.25, 0.25],
            y_range=[-1.15, 1.45, 0.5],
            x_length=6.4,
            y_length=5.0,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.25, -0.08, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.64)
        self.y_axis_label = MathTex("y", color=WHITE).scale(0.64)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.1)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.1)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_formulas(self):
        self.f_formula = MathTex("f(x)", "=", "\\sqrt{x}", color=WHITE).scale(0.66)
        self.f_formula.set_color_by_tex("f", self.F_COLOR)
        self.f_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.f_formula.move_to([3.35, 2.22, 0])

        self.g_formula = MathTex("g(x)", "=", "\\sqrt{1-x}", color=WHITE).scale(0.66)
        self.g_formula.set_color_by_tex("g", self.G_COLOR)
        self.g_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.g_formula.move_to([3.35, 1.5, 0])

        self.diff_formula = MathTex("(f-g)(x)", "=", "f(x)", "-", "g(x)", color=WHITE).scale(0.62)
        self.diff_formula.set_color_by_tex("f", self.F_COLOR)
        self.diff_formula.set_color_by_tex("g", self.G_COLOR)
        self.diff_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.diff_formula.move_to([3.35, 0.62, 0])

        self.domain_formula = MathTex("D_f", "\\cap", "D_g", "=", "[0,1]", color=WHITE).scale(0.6)
        self.domain_formula.set_color_by_tex("D_f", self.F_COLOR)
        self.domain_formula.set_color_by_tex("D_g", self.G_COLOR)
        self.domain_formula.set_color_by_tex("[0,1]", self.DOMAIN_COLOR)
        self.domain_formula.move_to([3.35, -0.12, 0])

    def create_graphs(self):
        self.f_graph = self.make_graph(self.f_function, 0, 1, self.F_COLOR)
        self.g_graph = self.make_graph(self.g_function, 0, 1, self.G_COLOR)
        self.diff_graph = self.make_graph(self.diff_function, 0, 1, self.DIFF_COLOR, stroke_width=5)

        self.f_label = MathTex("f", color=self.F_COLOR).scale(0.56)
        self.f_label.move_to(self.axes.c2p(0.82, self.f_function(0.82) + 0.13))
        self.g_label = MathTex("g", color=self.G_COLOR).scale(0.56)
        self.g_label.move_to(self.axes.c2p(0.2, self.g_function(0.2) + 0.16))
        self.diff_label = MathTex("f-g", color=self.DIFF_COLOR).scale(0.58)
        self.diff_label.move_to(self.axes.c2p(0.76, self.diff_function(0.76) - 0.18))

    def create_sample_objects(self):
        x = self.sample_x
        f_y = self.f_function(x)
        g_y = self.g_function(x)
        diff_y = self.diff_function(x)

        self.sample_line = DashedLine(
            self.axes.c2p(x, -0.18),
            self.axes.c2p(x, 1.12),
            color=self.INPUT_COLOR,
            stroke_width=3,
            dash_length=0.12,
        )
        self.sample_label = MathTex("a", color=self.INPUT_COLOR).scale(0.58)
        self.sample_label.next_to(self.axes.c2p(x, 0), DOWN, buff=0.12)

        self.f_segment = Line(self.axes.c2p(x, 0), self.axes.c2p(x, f_y), color=self.F_COLOR, stroke_width=7)
        self.g_segment = Line(
            self.axes.c2p(x + 0.055, 0),
            self.axes.c2p(x + 0.055, g_y),
            color=self.G_COLOR,
            stroke_width=7,
        )
        self.f_value_label = MathTex("f(a)", color=self.F_COLOR).scale(0.5)
        self.f_value_label.next_to(self.f_segment, LEFT, buff=0.12)
        self.g_value_label = MathTex("g(a)", color=self.G_COLOR).scale(0.5)
        self.g_value_label.next_to(self.g_segment, RIGHT, buff=0.12)

        self.difference_segment = Line(
            self.axes.c2p(x, g_y),
            self.axes.c2p(x, f_y),
            color=self.DIFF_COLOR,
            stroke_width=8,
        )
        self.difference_dot = Dot(self.axes.c2p(x, diff_y), radius=0.08, color=self.DIFF_COLOR)
        self.difference_value_label = MathTex("f(a)-g(a)", color=self.DIFF_COLOR).scale(0.48)
        self.difference_value_label.next_to(self.difference_segment, RIGHT, buff=0.12)

    def create_zero_marker(self):
        self.zero_line = Line(
            self.axes.c2p(0.5, -0.16),
            self.axes.c2p(0.5, 0.16),
            color=self.ZERO_COLOR,
            stroke_width=4,
        )
        self.zero_dot = Dot(self.axes.c2p(0.5, 0), radius=0.07, color=self.ZERO_COLOR)
        self.zero_label = MathTex("f=g", color=self.ZERO_COLOR).scale(0.5)
        self.zero_label.next_to(self.zero_dot, UP, buff=0.14)

    def create_domain_marker(self):
        self.domain_line = Line(
            self.axes.c2p(0, -0.12),
            self.axes.c2p(1, -0.12),
            color=self.DOMAIN_COLOR,
            stroke_width=5,
        )
        self.domain_label = MathTex("[0,1]", color=self.DOMAIN_COLOR).scale(0.5)
        self.domain_label.next_to(self.domain_line, DOWN, buff=0.08)

    def create_summary(self):
        self.summary_cards = VGroup(
            self.make_card("same x", self.INPUT_COLOR, width=1.2),
            self.make_card("signed gap", self.DIFF_COLOR, width=1.45),
            self.make_card("shared domain", self.DOMAIN_COLOR, width=1.7),
        )
        self.summary_cards.arrange(RIGHT, buff=0.18)
        self.summary_cards.to_edge(DOWN, buff=0.34)

        self.final_statement = MathTex(r"\text{new graph from vertical gaps}", color=WHITE).scale(0.56)
        self.final_statement.move_to([3.35, -0.86, 0])

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_draw_original_functions(self):
        self.play(
            Write(self.f_formula),
            Write(self.g_formula),
            Create(self.f_graph),
            Create(self.g_graph),
            FadeIn(self.f_label),
            FadeIn(self.g_label),
            run_time=3,
        )
        self.wait()

    def step3_choose_same_input(self):
        self.play(Create(self.sample_line), Write(self.sample_label), run_time=2)
        self.wait()

    def step4_show_two_heights(self):
        self.play(
            Create(self.f_segment),
            Create(self.g_segment),
            Write(self.f_value_label),
            Write(self.g_value_label),
            run_time=2,
        )
        self.wait()

    def step5_show_signed_difference(self):
        self.play(
            ReplacementTransform(self.g_value_label, self.difference_value_label),
            Transform(self.f_segment, self.difference_segment),
            FadeOut(self.f_value_label),
            FadeOut(self.g_segment),
            Write(self.diff_formula),
            run_time=2,
        )
        self.wait()

    def step6_trace_difference_graph(self):
        self.play(Create(self.diff_graph), FadeIn(self.diff_label), FadeIn(self.difference_dot), run_time=3)
        self.wait()

    def step7_mark_zero_crossing(self):
        self.play(
            Create(self.zero_line),
            FadeIn(self.zero_dot),
            Write(self.zero_label),
            Create(self.domain_line),
            Write(self.domain_label),
            Write(self.domain_formula),
            run_time=2,
        )
        self.wait()

    def step8_summarize_subtraction(self):
        self.play(
            FadeOut(self.sample_line),
            FadeOut(self.sample_label),
            FadeOut(self.difference_value_label),
            FadeIn(self.summary_cards),
            Write(self.final_statement),
            run_time=2,
        )
        self.wait()

    def f_function(self, x):
        return np.sqrt(x)

    def g_function(self, x):
        return np.sqrt(1 - x)

    def diff_function(self, x):
        return self.f_function(x) - self.g_function(x)

    def make_graph(self, function, x_start, x_end, color, stroke_width=4):
        points = []
        samples = 160
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=stroke_width)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_card(self, label, color, width=1.2):
        box = RoundedRectangle(
            width=width,
            height=0.48,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.3,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(r"\text{" + label + "}", color=color).scale(0.44)
        text.move_to(box)
        return VGroup(box, text)
