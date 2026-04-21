from manim import *


class Scene28_ConstantMultiple(Scene):
    INPUT_COLOR = YELLOW
    F_COLOR = TEAL
    SCALED_COLOR = BLUE
    GUIDE_COLOR = GREY_B
    FACTOR_COLOR = GREEN

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_draw_original_function()
        self.step3_choose_input()
        self.step4_show_original_height()
        self.step5_show_scale_factor()
        self.step6_stretch_height()
        self.step7_trace_scaled_graph()
        self.step8_summarize_constant_multiple()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.sample_x = 0.49
        self.scale_factor = 2

        self.create_axes()
        self.create_formulas()
        self.create_graphs()
        self.create_sample_objects()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-0.2, 1.25, 0.25],
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
        self.axes.move_to([-1.25, -0.08, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.64)
        self.y_axis_label = MathTex("y", color=WHITE).scale(0.64)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.1)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.1)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_formulas(self):
        self.f_formula = MathTex("f(x)", "=", "\\sqrt{x}", color=WHITE).scale(0.68)
        self.f_formula.set_color_by_tex("f", self.F_COLOR)
        self.f_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.f_formula.move_to([3.35, 2.08, 0])

        self.scaled_formula = MathTex("(cf)(x)", "=", "c", "f(x)", color=WHITE).scale(0.64)
        self.scaled_formula.set_color_by_tex("c", self.FACTOR_COLOR)
        self.scaled_formula.set_color_by_tex("f", self.F_COLOR)
        self.scaled_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.scaled_formula.move_to([3.35, 1.1, 0])

        self.example_formula = MathTex("c", "=", "2", color=WHITE).scale(0.62)
        self.example_formula.set_color_by_tex("c", self.FACTOR_COLOR)
        self.example_formula.set_color_by_tex("2", self.FACTOR_COLOR)
        self.example_formula.move_to([3.35, 0.36, 0])

        self.result_formula = MathTex("y", "=", "2\\sqrt{x}", color=WHITE).scale(0.62)
        self.result_formula.set_color_by_tex("2", self.FACTOR_COLOR)
        self.result_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.result_formula.move_to([3.35, -0.38, 0])

    def create_graphs(self):
        self.f_graph = self.make_graph(self.f_function, 0, 1, self.F_COLOR)
        self.scaled_graph = self.make_graph(self.scaled_function, 0, 1, self.SCALED_COLOR, stroke_width=5)

        self.f_label = MathTex("f", color=self.F_COLOR).scale(0.56)
        self.f_label.move_to(self.axes.c2p(0.82, self.f_function(0.82) + 0.12))
        self.scaled_label = MathTex("2f", color=self.SCALED_COLOR).scale(0.58)
        self.scaled_label.move_to(self.axes.c2p(0.78, self.scaled_function(0.78) + 0.16))

    def create_sample_objects(self):
        x = self.sample_x
        f_y = self.f_function(x)
        scaled_y = self.scaled_function(x)

        self.sample_line = DashedLine(
            self.axes.c2p(x, -0.15),
            self.axes.c2p(x, scaled_y + 0.24),
            color=self.INPUT_COLOR,
            stroke_width=3,
            dash_length=0.12,
        )
        self.sample_label = MathTex("a", color=self.INPUT_COLOR).scale(0.58)
        self.sample_label.next_to(self.axes.c2p(x, 0), DOWN, buff=0.12)

        self.f_segment = Line(self.axes.c2p(x, 0), self.axes.c2p(x, f_y), color=self.F_COLOR, stroke_width=7)
        self.f_value_label = MathTex("f(a)", color=self.F_COLOR).scale(0.5)
        self.f_value_label.next_to(self.f_segment, LEFT, buff=0.12)

        self.factor_brace = Brace(self.f_segment.copy(), RIGHT, color=self.FACTOR_COLOR, buff=0.14)
        self.factor_label = MathTex("\\times 2", color=self.FACTOR_COLOR).scale(0.52)
        self.factor_label.next_to(self.factor_brace, RIGHT, buff=0.08)

        self.scaled_segment = Line(
            self.axes.c2p(x, 0),
            self.axes.c2p(x, scaled_y),
            color=self.SCALED_COLOR,
            stroke_width=8,
        )
        self.scaled_dot = Dot(self.axes.c2p(x, scaled_y), radius=0.08, color=self.SCALED_COLOR)
        self.scaled_value_label = MathTex("2f(a)", color=self.SCALED_COLOR).scale(0.5)
        self.scaled_value_label.next_to(self.scaled_dot, UP, buff=0.12)

    def create_summary(self):
        self.summary_cards = VGroup(
            self.make_card("same x", self.INPUT_COLOR, width=1.2),
            self.make_card("scale height", self.SCALED_COLOR, width=1.55),
            self.make_card("constant c", self.FACTOR_COLOR, width=1.35),
        )
        self.summary_cards.arrange(RIGHT, buff=0.18)
        self.summary_cards.to_edge(DOWN, buff=0.34)

        self.final_statement = MathTex(r"\text{constant multiples rescale every height}", color=WHITE).scale(0.54)
        self.final_statement.move_to([3.35, -1.16, 0])

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_draw_original_function(self):
        self.play(Write(self.f_formula), Create(self.f_graph), FadeIn(self.f_label), run_time=3)
        self.wait()

    def step3_choose_input(self):
        self.play(Create(self.sample_line), Write(self.sample_label), run_time=2)
        self.wait()

    def step4_show_original_height(self):
        self.play(Create(self.f_segment), Write(self.f_value_label), run_time=2)
        self.wait()

    def step5_show_scale_factor(self):
        self.play(FadeIn(self.factor_brace), Write(self.factor_label), Write(self.example_formula), run_time=2)
        self.wait()

    def step6_stretch_height(self):
        self.play(
            Transform(self.f_segment, self.scaled_segment),
            ReplacementTransform(self.f_value_label, self.scaled_value_label),
            FadeOut(self.factor_brace),
            FadeOut(self.factor_label),
            FadeIn(self.scaled_dot),
            Write(self.scaled_formula),
            run_time=2,
        )
        self.wait()

    def step7_trace_scaled_graph(self):
        self.play(Create(self.scaled_graph), FadeIn(self.scaled_label), Write(self.result_formula), run_time=3)
        self.wait()

    def step8_summarize_constant_multiple(self):
        self.play(
            FadeOut(self.sample_line),
            FadeOut(self.sample_label),
            FadeOut(self.scaled_value_label),
            FadeIn(self.summary_cards),
            Write(self.final_statement),
            run_time=2,
        )
        self.wait()

    def f_function(self, x):
        return np.sqrt(x)

    def scaled_function(self, x):
        return self.scale_factor * self.f_function(x)

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
