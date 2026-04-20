from manim import *


class Scene15_FractionalPowerFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    SQRT_COLOR = BLUE
    CUBE_ROOT_COLOR = TEAL
    THREE_HALVES_COLOR = GREEN
    TWO_THIRDS_COLOR = YELLOW
    DOMAIN_COLOR = YELLOW
    RANGE_COLOR = GREEN

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_show_fractional_power_form()
        self.step3_draw_square_root()
        self.step4_mark_half_domain()
        self.step5_transform_to_cube_root()
        self.step6_mark_full_domain()
        self.step7_transform_to_three_halves()
        self.step8_restore_half_domain()
        self.step9_transform_to_two_thirds()
        self.step10_mark_nonnegative_range()
        self.step11_summarize_fractional_powers()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.domain_marker_y = -0.18

        self.create_axes()
        self.create_formulas()
        self.create_domain_markers()
        self.create_denominator_cues()
        self.create_range_marker()
        self.create_graphs()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-2.2, 3.0, 1],
            x_length=7.0,
            y_length=5.2,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-0.95, -0.1, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.7)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.7)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_formulas(self):
        self.power_form = MathTex("f(x)", "=", "x^a", color=WHITE)
        self.power_form.set_color_by_tex("x", self.INPUT_COLOR)
        self.power_form.set_color_by_tex("a", self.DOMAIN_COLOR)
        self.power_form.move_to([3.95, 2.35, 0])

        self.sqrt_label = self.make_formula_label("\\sqrt{x}", self.SQRT_COLOR)
        self.cube_root_label = self.make_formula_label("\\sqrt[3]{x}", self.CUBE_ROOT_COLOR)
        self.three_halves_label = self.make_formula_label("x^{3/2}", self.THREE_HALVES_COLOR)
        self.two_thirds_label = self.make_formula_label("x^{2/3}", self.TWO_THIRDS_COLOR)

    def create_domain_markers(self):
        self.half_domain = VGroup(
            Line(
                self.axes.c2p(0, self.domain_marker_y),
                self.axes.c2p(3.05, self.domain_marker_y),
                color=self.DOMAIN_COLOR,
                stroke_width=5,
            ),
            Dot(self.axes.c2p(0, self.domain_marker_y), radius=0.07, color=self.DOMAIN_COLOR),
        )
        self.full_domain = Line(
            self.axes.c2p(-3.05, self.domain_marker_y),
            self.axes.c2p(3.05, self.domain_marker_y),
            color=self.DOMAIN_COLOR,
            stroke_width=5,
        )

        self.half_domain_label = MathTex("x", "\\ge", "0", color=WHITE).scale(0.7)
        self.half_domain_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.half_domain_label.set_color_by_tex("0", self.DOMAIN_COLOR)
        self.half_domain_label.move_to([3.95, 0.75, 0])

        self.full_domain_label = MathTex("x", "\\in", "\\mathbb{R}", color=WHITE).scale(0.7)
        self.full_domain_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.full_domain_label.move_to(self.half_domain_label)

    def create_denominator_cues(self):
        self.even_denominator_label = Text("even denominator", font_size=23, color=self.DOMAIN_COLOR)
        self.odd_denominator_label = Text("odd denominator", font_size=23, color=self.CUBE_ROOT_COLOR)
        self.even_denominator_label.move_to([3.95, 0.08, 0])
        self.odd_denominator_label.move_to(self.even_denominator_label)

    def create_range_marker(self):
        self.nonnegative_region = Polygon(
            self.axes.c2p(-3.05, 0.02),
            self.axes.c2p(3.05, 0.02),
            self.axes.c2p(3.05, 2.75),
            self.axes.c2p(-3.05, 2.75),
            stroke_width=0,
            fill_color=self.RANGE_COLOR,
            fill_opacity=0.09,
        )
        self.range_arrow = Arrow(
            self.axes.c2p(-2.9, 0.25),
            self.axes.c2p(-2.9, 1.25),
            color=self.RANGE_COLOR,
            stroke_width=4,
            buff=0,
            max_tip_length_to_length_ratio=0.18,
        )
        self.range_label = MathTex("y", "\\ge", "0", color=WHITE).scale(0.7)
        self.range_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.range_label.set_color_by_tex("0", self.RANGE_COLOR)
        self.range_label.move_to([3.95, -0.5, 0])
        self.range_marker = VGroup(self.nonnegative_region, self.range_arrow, self.range_label)

    def create_graphs(self):
        self.sqrt_graph = self.make_graph(lambda x: x**0.5, 0, 3.0, self.SQRT_COLOR)
        self.cube_root_graph = self.make_graph(self.real_cube_root, -3.0, 3.0, self.CUBE_ROOT_COLOR)
        self.three_halves_graph = self.make_graph(lambda x: x**1.5, 0, 2.0, self.THREE_HALVES_COLOR)
        self.two_thirds_graph = self.make_graph(lambda x: abs(x) ** (2 / 3), -3.0, 3.0, self.TWO_THIRDS_COLOR)
        self.root_origin_dot = Dot(self.axes.c2p(0, 0), radius=0.07, color=self.CUBE_ROOT_COLOR)

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("even denom\nx >= 0", self.DOMAIN_COLOR, width=1.65),
            self.make_summary_card("odd denom\nall real x", self.CUBE_ROOT_COLOR, width=1.8),
            self.make_summary_card("even power\ny >= 0", self.RANGE_COLOR, width=1.65),
        )
        self.summary.arrange(RIGHT, buff=0.25)
        self.summary.to_edge(DOWN, buff=0.28)

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_show_fractional_power_form(self):
        self.play(Write(self.power_form), run_time=2)
        self.wait()

    def step3_draw_square_root(self):
        self.play(Create(self.sqrt_graph), Write(self.sqrt_label), run_time=2)
        self.wait()

    def step4_mark_half_domain(self):
        self.play(
            FadeIn(self.half_domain),
            Write(self.half_domain_label),
            Write(self.even_denominator_label),
            run_time=2,
        )
        self.wait()

    def step5_transform_to_cube_root(self):
        self.play(
            ReplacementTransform(self.sqrt_graph, self.cube_root_graph),
            ReplacementTransform(self.sqrt_label, self.cube_root_label),
            run_time=3,
        )
        self.wait()

    def step6_mark_full_domain(self):
        self.play(
            ReplacementTransform(self.half_domain, self.full_domain),
            ReplacementTransform(self.half_domain_label, self.full_domain_label),
            ReplacementTransform(self.even_denominator_label, self.odd_denominator_label),
            FadeIn(self.root_origin_dot),
            run_time=2,
        )
        self.wait()

    def step7_transform_to_three_halves(self):
        self.play(
            ReplacementTransform(self.cube_root_graph, self.three_halves_graph),
            ReplacementTransform(self.cube_root_label, self.three_halves_label),
            ReplacementTransform(self.full_domain, self.half_domain),
            ReplacementTransform(self.full_domain_label, self.half_domain_label),
            ReplacementTransform(self.odd_denominator_label, self.even_denominator_label),
            FadeOut(self.root_origin_dot),
            run_time=3,
        )
        self.wait()

    def step8_restore_half_domain(self):
        self.play(Indicate(self.half_domain), Indicate(self.half_domain_label), run_time=2)
        self.wait()

    def step9_transform_to_two_thirds(self):
        self.play(
            ReplacementTransform(self.three_halves_graph, self.two_thirds_graph),
            ReplacementTransform(self.three_halves_label, self.two_thirds_label),
            ReplacementTransform(self.half_domain, self.full_domain),
            ReplacementTransform(self.half_domain_label, self.full_domain_label),
            ReplacementTransform(self.even_denominator_label, self.odd_denominator_label),
            run_time=3,
        )
        self.wait()

    def step10_mark_nonnegative_range(self):
        self.play(FadeIn(self.range_marker), run_time=2)
        self.wait()

    def step11_summarize_fractional_powers(self):
        self.play(FadeIn(self.summary), run_time=2)
        self.wait()

    def make_formula_label(self, formula, color):
        label = MathTex("y", "=", formula, color=WHITE).scale(0.68)
        label.set_color_by_tex("y", self.OUTPUT_COLOR)
        label.set_color_by_tex("x", color)
        label.move_to([3.95, 1.45, 0])
        return label

    def make_graph(self, function, x_start, x_end, color):
        points = []
        samples = 140
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            if -2.1 <= y <= 2.85:
                points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=4)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def real_cube_root(self, x):
        if x == 0:
            return 0
        return abs(x) ** (1 / 3) * (1 if x > 0 else -1)

    def make_summary_card(self, label, color, width=1.7):
        box = RoundedRectangle(
            width=width,
            height=0.62,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.5,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = Text(label, font_size=14, color=color, line_spacing=0.85)
        text.move_to(box)
        return VGroup(box, text)
