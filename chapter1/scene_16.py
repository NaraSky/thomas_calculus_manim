from manim import *


class Scene16_PolynomialFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    TERM_COLOR = BLUE
    DEGREE_COLOR = YELLOW
    DOMAIN_COLOR = GREEN
    CURVE_COLOR = TEAL
    HIGHLIGHT_COLOR = RED

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_write_general_polynomial()
        self.step3_create_power_terms()
        self.step4_build_cubic_example()
        self.step5_highlight_degree()
        self.step6_mark_all_real_domain()
        self.step7_show_family_names()
        self.step8_transform_to_higher_degree()
        self.step9_mark_turning_behavior()
        self.step10_summarize_polynomials()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.domain_marker_y = -0.22

        self.create_axes()
        self.create_formulas()
        self.create_term_cards()
        self.create_graphs()
        self.create_degree_marker()
        self.create_domain_marker()
        self.create_family_labels()
        self.create_turning_markers()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-2.6, 2.6, 1],
            y_range=[-3.0, 3.0, 1],
            x_length=6.6,
            y_length=5.2,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.15, -0.05, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.7)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.7)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_formulas(self):
        self.general_formula = MathTex(
            "p(x)",
            "=",
            "a_nx^n",
            "+",
            "a_{n-1}x^{n-1}",
            "+",
            "\\cdots",
            "+",
            "a_0",
            color=WHITE,
        ).scale(0.62)
        self.general_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.general_formula.set_color_by_tex("n", self.DEGREE_COLOR)
        self.general_formula.move_to([3.15, 2.35, 0])

        self.cubic_formula = MathTex(
            "p(x)",
            "=",
            "x^3",
            "-",
            "\\frac{1}{2}x^2",
            "-",
            "2x",
            "+",
            "\\frac{1}{3}",
            color=WHITE,
        ).scale(0.55)
        self.cubic_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.cubic_formula.move_to([3.2, 1.55, 0])

        self.quartic_formula = MathTex("p(x)", "=", "0.35x^4", "-", "x^2", "+", "0.2x", color=WHITE).scale(0.56)
        self.quartic_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.quartic_formula.move_to(self.cubic_formula)

    def create_term_cards(self):
        self.term_cards = VGroup(
            self.make_term_card("leading term", self.DEGREE_COLOR, width=1.65),
            self.make_term_card("lower powers", self.TERM_COLOR, width=1.65),
            self.make_term_card("constant", self.OUTPUT_COLOR, width=1.35),
        )
        self.term_cards.arrange(DOWN, buff=0.16)
        self.term_cards.move_to([3.25, 0.55, 0])

    def create_graphs(self):
        self.cubic_graph = self.make_graph(self.cubic_function, -1.9, 1.9, self.CURVE_COLOR)
        self.quartic_graph = self.make_graph(self.quartic_function, -1.95, 1.95, self.HIGHLIGHT_COLOR)

    def create_degree_marker(self):
        self.degree_box = SurroundingRectangle(self.general_formula[2], color=self.DEGREE_COLOR, buff=0.08)
        self.degree_label = Text("degree = highest power", font_size=23, color=self.DEGREE_COLOR)
        self.degree_label.move_to([3.25, -0.75, 0])

    def create_domain_marker(self):
        self.full_domain = Line(
            self.axes.c2p(-2.45, self.domain_marker_y),
            self.axes.c2p(2.45, self.domain_marker_y),
            color=self.DOMAIN_COLOR,
            stroke_width=5,
        )
        self.domain_label = MathTex("x", "\\in", "\\mathbb{R}", color=WHITE).scale(0.68)
        self.domain_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.domain_label.move_to([3.25, -1.35, 0])

    def create_family_labels(self):
        self.family_labels = VGroup(
            self.make_family_label("linear", "1"),
            self.make_family_label("quadratic", "2"),
            self.make_family_label("cubic", "3"),
        )
        self.family_labels.arrange(RIGHT, buff=0.18)
        self.family_labels.to_edge(DOWN, buff=0.32)

    def create_turning_markers(self):
        self.turning_points = VGroup(
            Dot(self.axes.c2p(-1.25, self.quartic_function(-1.25)), radius=0.1, color=self.HIGHLIGHT_COLOR),
            Dot(self.axes.c2p(0.1, self.quartic_function(0.1)), radius=0.1, color=self.HIGHLIGHT_COLOR),
            Dot(self.axes.c2p(1.25, self.quartic_function(1.25)), radius=0.1, color=self.HIGHLIGHT_COLOR),
        )
        self.turning_label = Text("higher degree: more bends", font_size=23, color=self.HIGHLIGHT_COLOR)
        self.turning_label.move_to([3.25, -0.75, 0])

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("finite sum", self.TERM_COLOR, width=1.55),
            self.make_summary_card("degree = top power", self.DEGREE_COLOR, width=2.1),
            self.make_summary_card("domain: all real x", self.DOMAIN_COLOR, width=2.05),
        )
        self.summary.arrange(RIGHT, buff=0.2)
        self.summary.to_edge(DOWN, buff=0.42)

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_write_general_polynomial(self):
        self.play(Write(self.general_formula), run_time=2)
        self.wait()

    def step3_create_power_terms(self):
        self.play(FadeIn(self.term_cards), run_time=2)
        self.wait()

    def step4_build_cubic_example(self):
        self.play(Create(self.cubic_graph), Write(self.cubic_formula), run_time=3)
        self.wait()

    def step5_highlight_degree(self):
        self.play(Create(self.degree_box), Write(self.degree_label), run_time=2)
        self.wait()

    def step6_mark_all_real_domain(self):
        self.play(Create(self.full_domain), Write(self.domain_label), run_time=2)
        self.wait()

    def step7_show_family_names(self):
        self.play(FadeIn(self.family_labels), run_time=2)
        self.wait()

    def step8_transform_to_higher_degree(self):
        self.play(
            ReplacementTransform(self.cubic_graph, self.quartic_graph),
            ReplacementTransform(self.cubic_formula, self.quartic_formula),
            FadeOut(self.degree_box),
            ReplacementTransform(self.degree_label, self.turning_label),
            run_time=3,
        )
        self.wait()

    def step9_mark_turning_behavior(self):
        self.play(FadeIn(self.turning_points), run_time=2)
        self.wait()

    def step10_summarize_polynomials(self):
        self.play(
            FadeOut(self.turning_points),
            FadeOut(self.turning_label),
            FadeOut(self.family_labels),
            FadeOut(self.term_cards),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def cubic_function(self, x):
        return x**3 - 0.5 * x**2 - 2 * x + 1 / 3

    def quartic_function(self, x):
        return 0.35 * x**4 - x**2 + 0.2 * x + 0.35

    def make_graph(self, function, x_start, x_end, color):
        points = []
        samples = 160
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

    def make_term_card(self, label, color, width=1.6):
        box = RoundedRectangle(
            width=width,
            height=0.42,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.2,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = Text(label, font_size=17, color=color)
        text.move_to(box)
        return VGroup(box, text)

    def make_family_label(self, name, degree):
        box = RoundedRectangle(
            width=1.45,
            height=0.52,
            corner_radius=0.08,
            stroke_color=self.TERM_COLOR,
            stroke_width=2,
            fill_color=self.TERM_COLOR,
            fill_opacity=0.1,
        )
        label = VGroup(
            Text(name, font_size=16, color=self.TERM_COLOR),
            MathTex("n", "=", degree, color=WHITE).scale(0.45),
        )
        label[1].set_color_by_tex("n", self.DEGREE_COLOR)
        label.arrange(DOWN, buff=0.02)
        label.move_to(box)
        return VGroup(box, label)

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
