from manim import *


class Scene27_FunctionQuotient(Scene):
    INPUT_COLOR = YELLOW
    F_COLOR = TEAL
    G_COLOR = GREEN
    QUOTIENT_COLOR = BLUE
    DOMAIN_COLOR = RED
    GUIDE_COLOR = GREY_B
    WARNING_COLOR = RED

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_draw_original_functions()
        self.step3_choose_valid_input()
        self.step4_show_numerator_and_denominator()
        self.step5_mark_denominator_as_unit()
        self.step6_clear_denominator_cue()
        self.step7_form_ratio_height()
        self.step8_reveal_quotient_formula()
        self.step9_trace_quotient_graph()
        self.step10_show_forbidden_endpoint()
        self.step11_summarize_quotient()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.sample_x = 0.64

        self.create_axes()
        self.create_formulas()
        self.create_graphs()
        self.create_sample_objects()
        self.create_domain_objects()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-0.2, 1.12, 0.25],
            y_range=[-0.35, 2.3, 0.5],
            x_length=6.4,
            y_length=5.0,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.25, -0.05, 0])

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

        self.quotient_formula = MathTex(
            "\\left({f\\over g}\\right)(x)", "=", "{f(x)\\over g(x)}",
            color=WHITE,
        ).scale(0.62)
        self.quotient_formula.set_color_by_tex("f", self.F_COLOR)
        self.quotient_formula.set_color_by_tex("g", self.G_COLOR)
        self.quotient_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.quotient_formula.move_to([3.35, 0.58, 0])

        self.domain_formula = MathTex("D", "=", "[0,1)", color=WHITE).scale(0.62)
        self.domain_formula.set_color_by_tex("[0,1)", self.DOMAIN_COLOR)
        self.domain_formula.move_to([3.35, -0.16, 0])

        self.warning_formula = MathTex("g(1)=0", color=self.WARNING_COLOR).scale(0.58)
        self.warning_formula.move_to([3.35, -0.82, 0])

    def create_graphs(self):
        self.f_graph = self.make_graph(self.f_function, 0, 1, self.F_COLOR)
        self.g_graph = self.make_graph(self.g_function, 0, 1, self.G_COLOR)
        self.quotient_graph = self.make_graph(self.quotient_function, 0, 0.84, self.QUOTIENT_COLOR, stroke_width=5)

        self.f_label = MathTex("f", color=self.F_COLOR).scale(0.56)
        self.f_label.move_to(self.axes.c2p(0.82, self.f_function(0.82) + 0.13))
        self.g_label = MathTex("g", color=self.G_COLOR).scale(0.56)
        self.g_label.move_to(self.axes.c2p(0.2, self.g_function(0.2) + 0.16))
        self.quotient_label = MathTex("{f\\over g}", color=self.QUOTIENT_COLOR).scale(0.58)
        self.quotient_label.move_to(self.axes.c2p(0.77, self.quotient_function(0.77) + 0.18))

    def create_sample_objects(self):
        x = self.sample_x
        f_y = self.f_function(x)
        g_y = self.g_function(x)
        quotient_y = self.quotient_function(x)

        self.sample_line = DashedLine(
            self.axes.c2p(x, -0.16),
            self.axes.c2p(x, min(quotient_y + 0.3, 2.1)),
            color=self.INPUT_COLOR,
            stroke_width=3,
            dash_length=0.12,
        )
        self.sample_label = MathTex("a", color=self.INPUT_COLOR).scale(0.58)
        self.sample_label.next_to(self.axes.c2p(x, 0), DOWN, buff=0.12)

        self.f_segment = Line(self.axes.c2p(x, 0), self.axes.c2p(x, f_y), color=self.F_COLOR, stroke_width=7)
        self.g_segment = Line(
            self.axes.c2p(x + 0.06, 0),
            self.axes.c2p(x + 0.06, g_y),
            color=self.G_COLOR,
            stroke_width=7,
        )
        self.f_value_label = MathTex("f(a)", color=self.F_COLOR).scale(0.5)
        self.f_value_label.next_to(self.f_segment, LEFT, buff=0.12)
        self.g_value_label = MathTex("g(a)", color=self.G_COLOR).scale(0.5)
        self.g_value_label.next_to(self.g_segment, RIGHT, buff=0.12)

        self.unit_label = MathTex(r"\text{unit}", "=", "g(a)", color=WHITE).scale(0.44)
        self.unit_label.set_color_by_tex("g", self.G_COLOR)
        self.unit_label.next_to(self.g_segment, RIGHT, buff=0.12)
        self.divide_arrow = Arrow(
            self.g_segment.get_center() + LEFT * 0.08,
            self.f_segment.get_center() + RIGHT * 0.16,
            buff=0.08,
            color=self.G_COLOR,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.14,
        )
        self.divide_label = MathTex("\\div", "g(a)", color=WHITE).scale(0.48)
        self.divide_label.set_color_by_tex("g", self.G_COLOR)
        self.divide_label.next_to(self.divide_arrow, UP, buff=0.05)

        self.quotient_segment = Line(
            self.axes.c2p(x, 0),
            self.axes.c2p(x, quotient_y),
            color=self.QUOTIENT_COLOR,
            stroke_width=8,
        )
        self.quotient_dot = Dot(self.axes.c2p(x, quotient_y), radius=0.08, color=self.QUOTIENT_COLOR)
        self.quotient_value_label = MathTex("{f(a)\\over g(a)}", color=self.QUOTIENT_COLOR).scale(0.48)
        self.quotient_value_label.next_to(self.quotient_dot, UP, buff=0.12)

    def create_domain_objects(self):
        self.domain_line = Line(
            self.axes.c2p(0, -0.11),
            self.axes.c2p(1, -0.11),
            color=self.DOMAIN_COLOR,
            stroke_width=5,
        )
        self.open_endpoint = Circle(radius=0.075, color=self.DOMAIN_COLOR, stroke_width=3)
        self.open_endpoint.move_to(self.axes.c2p(1, -0.11))
        self.domain_label = MathTex("[0,1)", color=self.DOMAIN_COLOR).scale(0.5)
        self.domain_label.next_to(self.domain_line, DOWN, buff=0.08)

        self.forbidden_line = DashedLine(
            self.axes.c2p(1, -0.18),
            self.axes.c2p(1, 1.05),
            color=self.WARNING_COLOR,
            stroke_width=3,
            dash_length=0.1,
        )
        cross_center = self.axes.c2p(1, 0)
        self.forbidden_cross = VGroup(
            Line(cross_center + 0.11 * UL, cross_center + 0.11 * DR, color=self.WARNING_COLOR, stroke_width=5),
            Line(cross_center + 0.11 * UR, cross_center + 0.11 * DL, color=self.WARNING_COLOR, stroke_width=5),
        )

    def create_summary(self):
        self.summary_cards = VGroup(
            self.make_card("same x", self.INPUT_COLOR, width=1.2),
            self.make_card("ratio", self.QUOTIENT_COLOR, width=1.05),
            self.make_card("denominator nonzero", self.DOMAIN_COLOR, width=2.15),
        )
        self.summary_cards.arrange(RIGHT, buff=0.18)
        self.summary_cards.to_edge(DOWN, buff=0.34)

        self.final_statement = MathTex(r"\text{new graph from height ratios}", color=WHITE).scale(0.56)
        self.final_statement.move_to([3.45, -1.16, 0])

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

    def step3_choose_valid_input(self):
        self.play(Create(self.sample_line), Write(self.sample_label), run_time=2)
        self.wait()

    def step4_show_numerator_and_denominator(self):
        self.play(
            Create(self.f_segment),
            Create(self.g_segment),
            Write(self.f_value_label),
            Write(self.g_value_label),
            run_time=2,
        )
        self.wait()

    def step5_mark_denominator_as_unit(self):
        self.play(
            ReplacementTransform(self.g_value_label, self.unit_label),
            Create(self.divide_arrow),
            Write(self.divide_label),
            run_time=2,
        )
        self.wait()

    def step6_clear_denominator_cue(self):
        self.play(
            FadeOut(self.g_segment),
            FadeOut(self.unit_label),
            FadeOut(self.divide_arrow),
            FadeOut(self.divide_label),
            run_time=2,
        )
        self.wait()

    def step7_form_ratio_height(self):
        self.play(
            Transform(self.f_segment, self.quotient_segment),
            ReplacementTransform(self.f_value_label, self.quotient_value_label),
            FadeIn(self.quotient_dot),
            run_time=2,
        )
        self.wait()

    def step8_reveal_quotient_formula(self):
        self.play(Write(self.quotient_formula), run_time=2)
        self.wait()

    def step9_trace_quotient_graph(self):
        self.play(Create(self.quotient_graph), FadeIn(self.quotient_label), run_time=3)
        self.wait()

    def step10_show_forbidden_endpoint(self):
        self.play(
            Create(self.domain_line),
            FadeIn(self.open_endpoint),
            Write(self.domain_label),
            Create(self.forbidden_line),
            FadeIn(self.forbidden_cross),
            Write(self.domain_formula),
            Write(self.warning_formula),
            run_time=2,
        )
        self.wait()

    def step11_summarize_quotient(self):
        self.play(
            FadeOut(self.sample_line),
            FadeOut(self.sample_label),
            FadeOut(self.quotient_value_label),
            FadeIn(self.summary_cards),
            Write(self.final_statement),
            run_time=2,
        )
        self.wait()

    def f_function(self, x):
        return np.sqrt(x)

    def g_function(self, x):
        return np.sqrt(1 - x)

    def quotient_function(self, x):
        return self.f_function(x) / self.g_function(x)

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
