from manim import *


class Scene18_AlgebraicFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    OPERATION_COLOR = BLUE
    ROOT_COLOR = YELLOW
    DOMAIN_COLOR = RED
    CURVE_COLOR = TEAL
    SECOND_CURVE_COLOR = GREEN
    HIGHLIGHT_COLOR = RED

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_show_operation_building_blocks()
        self.step3_write_root_example()
        self.step4_draw_root_graph()
        self.step5_mark_domain_boundary()
        self.step6_transform_to_cusp_example()
        self.step7_highlight_cusps()
        self.step8_show_implicit_example()
        self.step9_summarize_algebraic_functions()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_operation_cards()
        self.create_formulas()
        self.create_graphs()
        self.create_domain_marker()
        self.create_cusp_markers()
        self.create_implicit_note()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-3.0, 3.0, 1],
            y_range=[-1.4, 3.4, 1],
            x_length=6.9,
            y_length=5.2,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.1, -0.15, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.7)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.7)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_operation_cards(self):
        self.operation_cards = VGroup(
            self.make_operation_card("+", self.OPERATION_COLOR),
            self.make_operation_card("-", self.OPERATION_COLOR),
            self.make_operation_card(r"\times", self.OPERATION_COLOR),
            self.make_operation_card(r"\div", self.OPERATION_COLOR),
            self.make_operation_card(r"\sqrt{\phantom{x}}", self.ROOT_COLOR, width=0.72),
        )
        self.operation_cards.arrange(RIGHT, buff=0.14)
        self.operation_cards.move_to([3.25, 2.35, 0])

        self.operation_label = Text("finite algebraic operations", font_size=21, color=WHITE)
        self.operation_label.next_to(self.operation_cards, DOWN, buff=0.16)

    def create_formulas(self):
        self.root_formula = MathTex("f(x)", "=", "\\sqrt{1-x}", color=WHITE).scale(0.74)
        self.root_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.root_formula.set_color_by_tex("\\sqrt", self.ROOT_COLOR)
        self.root_formula.move_to([3.25, 1.35, 0])

        self.root_domain = MathTex("x", "\\le", "1", color=WHITE).scale(0.7)
        self.root_domain.set_color_by_tex("x", self.INPUT_COLOR)
        self.root_domain.set_color_by_tex("1", self.DOMAIN_COLOR)
        self.root_domain.move_to([3.25, 0.6, 0])

        self.cusp_formula = MathTex("g(x)", "=", "(x^2-1)^{2/3}", color=WHITE).scale(0.68)
        self.cusp_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.cusp_formula.set_color_by_tex("2/3", self.ROOT_COLOR)
        self.cusp_formula.move_to(self.root_formula)

        self.cusp_note = Text("roots can create sharp points", font_size=22, color=self.HIGHLIGHT_COLOR)
        self.cusp_note.move_to([3.25, 0.6, 0])

    def create_graphs(self):
        self.root_graph = self.make_graph(self.root_function, -2.6, 1.0, self.CURVE_COLOR)
        self.cusp_graph = self.make_graph(self.cusp_function, -2.4, 2.4, self.SECOND_CURVE_COLOR)

    def create_domain_marker(self):
        self.domain_boundary = DashedLine(
            self.axes.c2p(1, -1.2),
            self.axes.c2p(1, 3.15),
            color=self.DOMAIN_COLOR,
            stroke_width=3,
            dash_length=0.16,
        )
        self.boundary_label = MathTex("x", "=", "1", color=WHITE).scale(0.58)
        self.boundary_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.boundary_label.set_color_by_tex("1", self.DOMAIN_COLOR)
        self.boundary_label.next_to(self.domain_boundary, UP, buff=0.08)

        self.domain_ray = Line(
            self.axes.c2p(-2.6, -0.18),
            self.axes.c2p(1, -0.18),
            color=self.DOMAIN_COLOR,
            stroke_width=4,
        )
        self.endpoint = Dot(self.axes.c2p(1, 0), radius=0.08, color=self.DOMAIN_COLOR)

    def create_cusp_markers(self):
        self.cusp_dots = VGroup(
            Dot(self.axes.c2p(-1, 0), radius=0.09, color=self.HIGHLIGHT_COLOR),
            Dot(self.axes.c2p(1, 0), radius=0.09, color=self.HIGHLIGHT_COLOR),
        )
        self.cusp_labels = VGroup(
            MathTex("x=-1", color=self.HIGHLIGHT_COLOR).scale(0.48),
            MathTex("x=1", color=self.HIGHLIGHT_COLOR).scale(0.48),
        )
        self.cusp_labels[0].next_to(self.cusp_dots[0], DOWN, buff=0.14)
        self.cusp_labels[1].next_to(self.cusp_dots[1], DOWN, buff=0.14)

    def create_implicit_note(self):
        self.implicit_equation = MathTex("y^3", "-", "9xy", "+", "x^3", "=", "0", color=WHITE).scale(0.66)
        self.implicit_equation.set_color_by_tex("x", self.INPUT_COLOR)
        self.implicit_equation.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.implicit_equation.move_to([3.25, 0.08, 0])

        self.implicit_label = Text("can also be implicit", font_size=21, color=self.OPERATION_COLOR)
        self.implicit_label.next_to(self.implicit_equation, DOWN, buff=0.12)

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("poly base", self.OPERATION_COLOR, width=1.45),
            self.make_summary_card("root operations", self.ROOT_COLOR, width=1.8),
            self.make_summary_card("domain matters", self.DOMAIN_COLOR, width=1.8),
        )
        self.summary.arrange(RIGHT, buff=0.18)
        self.summary.to_edge(DOWN, buff=0.36)

        self.final_statement = Text("algebraic = operations + roots", font_size=23, color=WHITE)
        self.final_statement.move_to([3.25, 0.45, 0])

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_show_operation_building_blocks(self):
        self.play(FadeIn(self.operation_cards), Write(self.operation_label), run_time=2)
        self.wait()

    def step3_write_root_example(self):
        self.play(Write(self.root_formula), run_time=2)
        self.wait()

    def step4_draw_root_graph(self):
        self.play(Create(self.root_graph), run_time=3)
        self.wait()

    def step5_mark_domain_boundary(self):
        self.play(
            Create(self.domain_boundary),
            Write(self.boundary_label),
            Create(self.domain_ray),
            FadeIn(self.endpoint),
            Write(self.root_domain),
            run_time=2,
        )
        self.wait()

    def step6_transform_to_cusp_example(self):
        self.play(
            ReplacementTransform(self.root_formula, self.cusp_formula),
            ReplacementTransform(self.root_graph, self.cusp_graph),
            FadeOut(self.domain_boundary),
            FadeOut(self.boundary_label),
            FadeOut(self.domain_ray),
            FadeOut(self.endpoint),
            ReplacementTransform(self.root_domain, self.cusp_note),
            run_time=3,
        )
        self.wait()

    def step7_highlight_cusps(self):
        self.play(FadeIn(self.cusp_dots), Write(self.cusp_labels), run_time=2)
        self.wait()

    def step8_show_implicit_example(self):
        self.play(
            FadeOut(self.operation_cards),
            FadeOut(self.operation_label),
            FadeOut(self.cusp_note),
            Write(self.implicit_equation),
            Write(self.implicit_label),
            run_time=2,
        )
        self.wait()

    def step9_summarize_algebraic_functions(self):
        self.play(
            FadeOut(self.cusp_dots),
            FadeOut(self.cusp_labels),
            FadeOut(self.implicit_equation),
            FadeOut(self.implicit_label),
            FadeIn(self.summary),
            FadeIn(self.final_statement),
            run_time=2,
        )
        self.wait()

    def root_function(self, x):
        return (1 - x) ** 0.5

    def cusp_function(self, x):
        return abs(x**2 - 1) ** (2 / 3)

    def make_graph(self, function, x_start, x_end, color):
        points = []
        samples = 180
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            if -1.25 <= y <= 3.25:
                points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=4)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_operation_card(self, symbol, color, width=0.58):
        box = RoundedRectangle(
            width=width,
            height=0.48,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.2,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(symbol, color=color).scale(0.58)
        text.move_to(box)
        return VGroup(box, text)

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
