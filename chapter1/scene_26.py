from manim import *


class Scene26_FunctionMultiplication(Scene):
    INPUT_COLOR = YELLOW
    F_COLOR = TEAL
    G_COLOR = GREEN
    PRODUCT_COLOR = BLUE
    DOMAIN_COLOR = RED
    GUIDE_COLOR = GREY_B

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_draw_original_functions()
        self.step3_choose_same_input()
        self.step4_show_height_and_factor()
        self.step5_connect_factor_to_height()
        self.step6_scale_height_to_product()
        self.step7_reveal_product_formula()
        self.step8_trace_product_graph()
        self.step9_mark_shared_domain()
        self.step10_summarize_product()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.sample_x = 0.64

        self.create_axes()
        self.create_formulas()
        self.create_graphs()
        self.create_sample_objects()
        self.create_domain_marker()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-0.2, 1.25, 0.25],
            y_range=[-0.35, 1.45, 0.5],
            x_length=6.4,
            y_length=5.0,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.25, -0.04, 0])

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

        self.product_formula = MathTex("(fg)(x)", "=", "f(x)", "g(x)", color=WHITE).scale(0.62)
        self.product_formula.set_color_by_tex("f", self.F_COLOR)
        self.product_formula.set_color_by_tex("g", self.G_COLOR)
        self.product_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.product_formula.move_to([3.35, 0.62, 0])

        self.domain_formula = MathTex("D_f", "\\cap", "D_g", "=", "[0,1]", color=WHITE).scale(0.6)
        self.domain_formula.set_color_by_tex("D_f", self.F_COLOR)
        self.domain_formula.set_color_by_tex("D_g", self.G_COLOR)
        self.domain_formula.set_color_by_tex("[0,1]", self.DOMAIN_COLOR)
        self.domain_formula.move_to([3.35, -0.12, 0])

    def create_graphs(self):
        self.f_graph = self.make_graph(self.f_function, 0, 1, self.F_COLOR)
        self.g_graph = self.make_graph(self.g_function, 0, 1, self.G_COLOR)
        self.product_graph = self.make_graph(self.product_function, 0, 1, self.PRODUCT_COLOR, stroke_width=5)

        self.f_label = MathTex("f", color=self.F_COLOR).scale(0.56)
        self.f_label.move_to(self.axes.c2p(0.82, self.f_function(0.82) + 0.13))
        self.g_label = MathTex("g", color=self.G_COLOR).scale(0.56)
        self.g_label.move_to(self.axes.c2p(0.2, self.g_function(0.2) + 0.16))
        self.product_label = MathTex("fg", color=self.PRODUCT_COLOR).scale(0.58)
        self.product_label.move_to(self.axes.c2p(0.5, self.product_function(0.5) + 0.14))

    def create_sample_objects(self):
        x = self.sample_x
        f_y = self.f_function(x)
        g_y = self.g_function(x)
        product_y = self.product_function(x)

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
        self.f_value_label = MathTex("f(a)", color=self.F_COLOR).scale(0.5)
        self.f_value_label.next_to(self.f_segment, LEFT, buff=0.12)

        self.factor_track = Line(
            self.axes.c2p(1.08, 0),
            self.axes.c2p(1.08, 1),
            color=self.GUIDE_COLOR,
            stroke_width=2,
        )
        self.factor_bar = Line(
            self.axes.c2p(1.08, 0),
            self.axes.c2p(1.08, g_y),
            color=self.G_COLOR,
            stroke_width=7,
        )
        self.factor_label = MathTex("g(a)", color=self.G_COLOR).scale(0.5)
        self.factor_label.next_to(self.factor_bar, RIGHT, buff=0.12)
        self.unit_label = MathTex("1", color=self.GUIDE_COLOR).scale(0.42)
        self.unit_label.next_to(self.factor_track.get_end(), RIGHT, buff=0.1)

        self.scale_arrow = Arrow(
            self.factor_bar.get_center() + LEFT * 0.08,
            self.f_segment.get_center() + RIGHT * 0.16,
            buff=0.08,
            color=self.G_COLOR,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.14,
        )
        self.scale_label = MathTex("\\times", "g(a)", color=WHITE).scale(0.48)
        self.scale_label.set_color_by_tex("g", self.G_COLOR)
        self.scale_label.next_to(self.scale_arrow, UP, buff=0.05)

        self.product_segment = Line(
            self.axes.c2p(x, 0),
            self.axes.c2p(x, product_y),
            color=self.PRODUCT_COLOR,
            stroke_width=8,
        )
        self.product_dot = Dot(self.axes.c2p(x, product_y), radius=0.08, color=self.PRODUCT_COLOR)
        self.product_value_label = MathTex("f(a)g(a)", color=self.PRODUCT_COLOR).scale(0.48)
        self.product_value_label.next_to(self.product_segment, RIGHT, buff=0.12)

    def create_domain_marker(self):
        self.domain_line = Line(
            self.axes.c2p(0, -0.11),
            self.axes.c2p(1, -0.11),
            color=self.DOMAIN_COLOR,
            stroke_width=5,
        )
        self.domain_label = MathTex("[0,1]", color=self.DOMAIN_COLOR).scale(0.5)
        self.domain_label.next_to(self.domain_line, DOWN, buff=0.08)

    def create_summary(self):
        self.summary_cards = VGroup(
            self.make_card("same x", self.INPUT_COLOR, width=1.2),
            self.make_card("scale height", self.PRODUCT_COLOR, width=1.55),
            self.make_card("shared domain", self.DOMAIN_COLOR, width=1.7),
        )
        self.summary_cards.arrange(RIGHT, buff=0.18)
        self.summary_cards.to_edge(DOWN, buff=0.34)

        self.final_statement = MathTex(r"\text{new graph from scaled heights}", color=WHITE).scale(0.56)
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

    def step4_show_height_and_factor(self):
        self.play(
            Create(self.f_segment),
            Write(self.f_value_label),
            Create(self.factor_track),
            Create(self.factor_bar),
            Write(self.factor_label),
            Write(self.unit_label),
            run_time=2,
        )
        self.wait()

    def step5_connect_factor_to_height(self):
        self.play(Create(self.scale_arrow), Write(self.scale_label), run_time=2)
        self.wait()

    def step6_scale_height_to_product(self):
        self.play(
            Transform(self.f_segment, self.product_segment),
            ReplacementTransform(self.f_value_label, self.product_value_label),
            FadeIn(self.product_dot),
            run_time=2,
        )
        self.wait()

    def step7_reveal_product_formula(self):
        self.play(Write(self.product_formula), run_time=2)
        self.wait()

    def step8_trace_product_graph(self):
        self.play(Create(self.product_graph), FadeIn(self.product_label), run_time=3)
        self.wait()

    def step9_mark_shared_domain(self):
        self.play(Create(self.domain_line), Write(self.domain_label), Write(self.domain_formula), run_time=2)
        self.wait()

    def step10_summarize_product(self):
        self.play(
            FadeOut(self.sample_line),
            FadeOut(self.sample_label),
            FadeOut(self.product_value_label),
            FadeOut(self.factor_track),
            FadeOut(self.factor_bar),
            FadeOut(self.factor_label),
            FadeOut(self.unit_label),
            FadeOut(self.scale_arrow),
            FadeOut(self.scale_label),
            FadeIn(self.summary_cards),
            Write(self.final_statement),
            run_time=2,
        )
        self.wait()

    def f_function(self, x):
        return np.sqrt(x)

    def g_function(self, x):
        return np.sqrt(1 - x)

    def product_function(self, x):
        return self.f_function(x) * self.g_function(x)

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
