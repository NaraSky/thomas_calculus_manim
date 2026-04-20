from manim import *


class Scene20_ExponentialFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    BASE_COLOR = BLUE
    CURVE_COLOR = TEAL
    STEEP_COLOR = GREEN
    FAST_COLOR = BLUE
    MIRROR_COLOR = PURPLE
    RANGE_COLOR = RED
    GUIDE_COLOR = GREY_B

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_write_exponential_form()
        self.step3_mark_anchor_point()
        self.step4_draw_base_two_graph()
        self.step5_show_repeated_multiplication()
        self.step6_compare_larger_bases()
        self.step7_mark_positive_range()
        self.step8_show_decreasing_mirror()
        self.step9_summarize_exponential_functions()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_formulas()
        self.create_graphs()
        self.create_anchor_marker()
        self.create_multiplication_markers()
        self.create_range_marker()
        self.create_mirror_marker()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-3.0, 3.0, 1],
            y_range=[-0.6, 5.4, 1],
            x_length=6.8,
            y_length=5.2,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.15, -0.18, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.68)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.68)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_formulas(self):
        self.general_formula = MathTex("f(x)", "=", "a^x", color=WHITE).scale(0.82)
        self.general_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.general_formula.set_color_by_tex("a", self.BASE_COLOR)
        self.general_formula.move_to([3.25, 2.35, 0])

        self.base_rule = MathTex("a", ">", "0", ",", "\\quad", "a", "\\ne", "1", color=WHITE).scale(0.62)
        self.base_rule.set_color_by_tex("a", self.BASE_COLOR)
        self.base_rule.move_to([3.25, 1.6, 0])

        self.example_formula = MathTex("y", "=", "2^x", color=WHITE).scale(0.72)
        self.example_formula.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.example_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.example_formula.move_to([3.25, 0.82, 0])

        self.decreasing_formula = MathTex("y", "=", "2^{-x}", color=WHITE).scale(0.72)
        self.decreasing_formula.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.decreasing_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.decreasing_formula.move_to(self.example_formula)

    def create_graphs(self):
        self.base_two_graph = self.make_graph(lambda x: 2**x, -3.0, 2.35, self.CURVE_COLOR)
        self.base_three_graph = self.make_graph(lambda x: 3**x, -3.0, 1.48, self.STEEP_COLOR)
        self.base_ten_graph = self.make_graph(lambda x: 10**x, -3.0, 0.72, self.FAST_COLOR)
        self.decreasing_graph = self.make_graph(lambda x: 2 ** (-x), -2.35, 3.0, self.MIRROR_COLOR)
        self.final_growth_graph = self.make_graph(lambda x: 2**x, -3.0, 2.35, self.CURVE_COLOR)

        self.base_labels = VGroup(
            self.make_curve_label("2^x", self.CURVE_COLOR, [1.65, 1.9, 0]),
            self.make_curve_label("3^x", self.STEEP_COLOR, [0.78, 2.35, 0]),
            self.make_curve_label("10^x", self.FAST_COLOR, [-0.05, 2.62, 0]),
        )

    def create_anchor_marker(self):
        self.anchor_dot = Dot(self.axes.c2p(0, 1), radius=0.08, color=self.OUTPUT_COLOR)
        self.anchor_label = MathTex("(0,1)", color=WHITE).scale(0.55)
        self.anchor_label.next_to(self.anchor_dot, LEFT, buff=0.16)

    def create_multiplication_markers(self):
        self.step_points = VGroup(
            Dot(self.axes.c2p(0, 1), radius=0.06, color=self.INPUT_COLOR),
            Dot(self.axes.c2p(1, 2), radius=0.06, color=self.INPUT_COLOR),
            Dot(self.axes.c2p(2, 4), radius=0.06, color=self.INPUT_COLOR),
        )
        self.mult_arrows = VGroup(
            Arrow(self.axes.c2p(0, 1), self.axes.c2p(1, 2), color=self.BASE_COLOR, buff=0.12, stroke_width=3),
            Arrow(self.axes.c2p(1, 2), self.axes.c2p(2, 4), color=self.BASE_COLOR, buff=0.12, stroke_width=3),
        )
        self.mult_label = MathTex("\\times", "2", "\\quad", "\\times", "2", color=WHITE).scale(0.58)
        self.mult_label.set_color_by_tex("2", self.BASE_COLOR)
        self.mult_label.move_to([3.25, 0.06, 0])

    def create_range_marker(self):
        self.x_axis_asymptote = DashedLine(
            self.axes.c2p(-2.9, 0),
            self.axes.c2p(2.9, 0),
            color=self.RANGE_COLOR,
            stroke_width=2,
            dash_length=0.16,
        )
        self.x_axis_asymptote.set_opacity(0.75)
        self.range_label = MathTex("y", ">", "0", color=WHITE).scale(0.7)
        self.range_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.range_label.set_color_by_tex("0", self.RANGE_COLOR)
        self.range_label.move_to([3.25, -0.62, 0])

    def create_mirror_marker(self):
        self.mirror_axis = DashedLine(
            self.axes.c2p(0, -0.35),
            self.axes.c2p(0, 5.1),
            color=self.GUIDE_COLOR,
            stroke_width=2,
            dash_length=0.16,
        )
        self.mirror_label = Text("mirror across y-axis", font_size=21, color=self.MIRROR_COLOR)
        self.mirror_label.move_to([3.25, -1.28, 0])

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("a^x", self.BASE_COLOR, width=1.15),
            self.make_summary_card("(0,1)", self.OUTPUT_COLOR, width=1.25),
            self.make_summary_card("y>0", self.RANGE_COLOR, width=1.15),
        )
        self.summary.arrange(RIGHT, buff=0.2)
        self.summary.to_edge(DOWN, buff=0.34)

        self.final_statement = Text("equal x-steps scale y", font_size=24, color=WHITE)
        self.final_statement.move_to([3.25, 1.25, 0])

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_write_exponential_form(self):
        self.play(Write(self.general_formula), Write(self.base_rule), run_time=2)
        self.wait()

    def step3_mark_anchor_point(self):
        self.play(FadeIn(self.anchor_dot), Write(self.anchor_label), Write(self.example_formula), run_time=2)
        self.wait()

    def step4_draw_base_two_graph(self):
        self.play(Create(self.base_two_graph), run_time=3)
        self.wait()

    def step5_show_repeated_multiplication(self):
        self.play(FadeIn(self.step_points), Create(self.mult_arrows), Write(self.mult_label), run_time=2)
        self.wait()

    def step6_compare_larger_bases(self):
        self.play(Create(self.base_three_graph), Create(self.base_ten_graph), FadeIn(self.base_labels), run_time=3)
        self.wait()

    def step7_mark_positive_range(self):
        self.play(Create(self.x_axis_asymptote), Write(self.range_label), run_time=2)
        self.wait()

    def step8_show_decreasing_mirror(self):
        self.play(
            ReplacementTransform(self.base_two_graph, self.decreasing_graph),
            ReplacementTransform(self.example_formula, self.decreasing_formula),
            Create(self.mirror_axis),
            Write(self.mirror_label),
            FadeOut(self.mult_arrows),
            FadeOut(self.mult_label),
            FadeOut(self.step_points),
            FadeOut(self.base_three_graph),
            FadeOut(self.base_ten_graph),
            FadeOut(self.base_labels),
            run_time=3,
        )
        self.wait()

    def step9_summarize_exponential_functions(self):
        self.play(
            FadeOut(self.mirror_label),
            FadeOut(self.decreasing_formula),
            ReplacementTransform(self.decreasing_graph, self.final_growth_graph),
            ReplacementTransform(self.general_formula, self.final_statement),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def make_graph(self, function, x_start, x_end, color):
        points = []
        samples = 180
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            if -0.5 <= y <= 5.15:
                points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=4)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_curve_label(self, label, color, position):
        text = MathTex(label, color=color).scale(0.58)
        text.move_to(position)
        return text

    def make_summary_card(self, label, color, width=1.2):
        box = RoundedRectangle(
            width=width,
            height=0.5,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.4,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(label, color=color).scale(0.5)
        text.move_to(box)
        return VGroup(box, text)
