from manim import *


class Scene22_TranscendentalFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    CATENARY_COLOR = TEAL
    PARABOLA_COLOR = GREY_B
    EXP_COLOR = BLUE
    WARNING_COLOR = RED
    HIGHLIGHT_COLOR = YELLOW

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_show_hanging_chain()
        self.step3_write_catenary_formula()
        self.step4_graph_catenary()
        self.step5_compare_with_parabola()
        self.step6_mark_not_polynomial()
        self.step7_show_transcendental_family()
        self.step8_summarize_transcendentals()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_chain_metaphor()
        self.create_formulas()
        self.create_graphs()
        self.create_comparison_notes()
        self.create_family_cards()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-3.0, 3.0, 1],
            y_range=[-0.4, 4.6, 1],
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

    def create_chain_metaphor(self):
        self.chain_points = [
            self.axes.c2p(x, self.catenary_function(x))
            for x in np.linspace(-2.15, 2.15, 17)
        ]
        self.chain_links = VMobject(color=self.CATENARY_COLOR, stroke_width=5)
        self.chain_links.set_points_smoothly(self.chain_points)
        self.chain_beads = VGroup(
            *[Dot(point, radius=0.045, color=self.HIGHLIGHT_COLOR) for point in self.chain_points]
        )
        self.supports = VGroup(
            Dot(self.chain_points[0], radius=0.09, color=self.WARNING_COLOR),
            Dot(self.chain_points[-1], radius=0.09, color=self.WARNING_COLOR),
        )
        self.chain_label = MathTex(r"\text{hanging chain}", color=self.CATENARY_COLOR).scale(0.58)
        self.chain_label.move_to([3.25, 2.35, 0])

    def create_formulas(self):
        self.catenary_formula = MathTex("y", "=", "\\cosh", "x", color=WHITE).scale(0.78)
        self.catenary_formula.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.catenary_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.catenary_formula.set_color_by_tex("\\cosh", self.CATENARY_COLOR)
        self.catenary_formula.move_to([3.25, 1.55, 0])

        self.exp_definition = MathTex("\\cosh", "x", "=", "\\frac{e^x+e^{-x}}{2}", color=WHITE).scale(0.58)
        self.exp_definition.set_color_by_tex("x", self.INPUT_COLOR)
        self.exp_definition.set_color_by_tex("e", self.EXP_COLOR)
        self.exp_definition.move_to([3.25, 0.82, 0])

        self.final_statement = MathTex(r"\text{transcendental: beyond algebraic}", color=WHITE).scale(0.5)
        self.final_statement.move_to([3.25, 1.68, 0])

    def create_graphs(self):
        self.catenary_graph = self.make_graph(self.catenary_function, -2.2, 2.2, self.CATENARY_COLOR, stroke_width=4)
        self.parabola_graph = self.make_graph(lambda x: 1 + 0.5 * x**2, -2.2, 2.2, self.PARABOLA_COLOR, stroke_width=3)
        self.parabola_graph.set_stroke(opacity=0.7)

        self.vertex_dot = Dot(self.axes.c2p(0, 1), radius=0.08, color=self.OUTPUT_COLOR)
        self.vertex_label = MathTex("(0,1)", color=WHITE).scale(0.54)
        self.vertex_label.next_to(self.vertex_dot, DOWN + RIGHT, buff=0.12)

        self.symmetry_axis = DashedLine(
            self.axes.c2p(0, -0.15),
            self.axes.c2p(0, 4.35),
            color=GREY_B,
            stroke_width=2,
            dash_length=0.16,
        )
        self.symmetry_axis.set_opacity(0.65)

    def create_comparison_notes(self):
        self.parabola_label = MathTex(r"1+\frac{x^2}{2}", color=self.PARABOLA_COLOR).scale(0.52)
        self.parabola_label.move_to(self.axes.c2p(1.7, 2.7))

        self.catenary_label = MathTex(r"\cosh x", color=self.CATENARY_COLOR).scale(0.56)
        self.catenary_label.move_to(self.axes.c2p(2.05, 3.95))

        self.not_polynomial = MathTex(r"\text{not a polynomial}", color=self.WARNING_COLOR).scale(0.58)
        self.not_polynomial.move_to([3.25, 0.08, 0])

    def create_family_cards(self):
        self.family_cards = VGroup(
            self.make_card(r"\sin x", self.CATENARY_COLOR, width=1.1),
            self.make_card(r"e^x", self.EXP_COLOR, width=1.0),
            self.make_card(r"\log x", self.OUTPUT_COLOR, width=1.15),
            self.make_card(r"\cosh x", self.HIGHLIGHT_COLOR, width=1.25),
        )
        self.family_cards.arrange(RIGHT, buff=0.15)
        self.family_cards.move_to([3.25, -0.82, 0])

    def create_summary(self):
        self.summary = VGroup(
            self.make_card(r"\text{not algebraic}", self.WARNING_COLOR, width=1.75),
            self.make_card(r"\text{natural shape}", self.CATENARY_COLOR, width=1.75),
            self.make_card(r"\cosh x", self.HIGHLIGHT_COLOR, width=1.2),
        )
        self.summary.arrange(RIGHT, buff=0.18)
        self.summary.to_edge(DOWN, buff=0.34)

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_show_hanging_chain(self):
        self.play(Create(self.chain_links), FadeIn(self.chain_beads), FadeIn(self.supports), Write(self.chain_label), run_time=3)
        self.wait()

    def step3_write_catenary_formula(self):
        self.play(Write(self.catenary_formula), Write(self.exp_definition), run_time=2)
        self.wait()

    def step4_graph_catenary(self):
        self.play(
            ReplacementTransform(self.chain_links, self.catenary_graph),
            FadeOut(self.chain_beads),
            FadeOut(self.supports),
            FadeIn(self.vertex_dot),
            Write(self.vertex_label),
            Create(self.symmetry_axis),
            run_time=3,
        )
        self.wait()

    def step5_compare_with_parabola(self):
        self.play(Create(self.parabola_graph), Write(self.parabola_label), Write(self.catenary_label), run_time=2)
        self.wait()

    def step6_mark_not_polynomial(self):
        self.play(Write(self.not_polynomial), run_time=2)
        self.wait()

    def step7_show_transcendental_family(self):
        self.play(FadeIn(self.family_cards), run_time=2)
        self.wait()

    def step8_summarize_transcendentals(self):
        self.play(
            FadeOut(self.chain_label),
            FadeOut(self.exp_definition),
            FadeOut(self.not_polynomial),
            FadeOut(self.family_cards),
            FadeOut(self.parabola_label),
            FadeOut(self.catenary_label),
            ReplacementTransform(self.catenary_formula, self.final_statement),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def catenary_function(self, x):
        return np.cosh(x) / 1.65 + 0.35

    def make_graph(self, function, x_start, x_end, color, stroke_width=4):
        points = []
        samples = 180
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            if -0.25 <= y <= 4.45:
                points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=stroke_width)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_card(self, label, color, width=1.2):
        box = RoundedRectangle(
            width=width,
            height=0.5,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.4,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(label, color=color).scale(0.46)
        text.move_to(box)
        return VGroup(box, text)
