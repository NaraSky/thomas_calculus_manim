from manim import *


class Scene23_FunctionsAndGraphsSummary(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    GRAPH_COLOR = TEAL
    DOMAIN_COLOR = RED
    FAMILY_COLOR = BLUE
    TRANSCENDENTAL_COLOR = PURPLE
    GUIDE_COLOR = GREY_B

    def construct(self):
        self.setup_layout()
        self.step1_show_function_rule()
        self.step2_mark_domain_and_range()
        self.step3_turn_pairs_into_graph()
        self.step4_check_function_graph()
        self.step5_group_common_families()
        self.step6_split_algebraic_transcendental()
        self.step7_final_summary()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_rule_diagram()
        self.create_axes()
        self.create_domain_range_marks()
        self.create_graph_objects()
        self.create_vertical_test()
        self.create_family_cards()
        self.create_final_summary()

    def create_rule_diagram(self):
        self.input_card = self.make_card("x", self.INPUT_COLOR, width=0.9)
        self.rule_card = self.make_card("f", self.FAMILY_COLOR, width=0.9)
        self.output_card = self.make_card("f(x)", self.OUTPUT_COLOR, width=1.15)
        self.rule_arrow_1 = Arrow(LEFT, RIGHT, color=self.GUIDE_COLOR, buff=0.16, stroke_width=3)
        self.rule_arrow_2 = Arrow(LEFT, RIGHT, color=self.GUIDE_COLOR, buff=0.16, stroke_width=3)

        self.rule_row = VGroup(
            self.input_card,
            self.rule_arrow_1,
            self.rule_card,
            self.rule_arrow_2,
            self.output_card,
        )
        self.rule_row.arrange(RIGHT, buff=0.18)
        self.rule_row.to_edge(UP, buff=0.55)

        self.rule_label = MathTex(r"\text{one input gives one output}", color=WHITE).scale(0.58)
        self.rule_label.next_to(self.rule_row, DOWN, buff=0.16)

    def create_axes(self):
        self.axes = Axes(
            x_range=[-2.8, 2.8, 1],
            y_range=[-1.4, 3.6, 1],
            x_length=5.7,
            y_length=3.7,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-2.5, -0.35, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.62)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.62)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.1)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.1)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_domain_range_marks(self):
        self.domain_line = Line(
            self.axes.c2p(-2.2, -0.18),
            self.axes.c2p(2.2, -0.18),
            color=self.INPUT_COLOR,
            stroke_width=5,
        )
        self.domain_label = MathTex(r"\text{domain}", color=self.INPUT_COLOR).scale(0.48)
        self.domain_label.next_to(self.domain_line, DOWN, buff=0.1)

        self.range_line = Line(
            self.axes.c2p(-2.55, 0.2),
            self.axes.c2p(-2.55, 2.9),
            color=self.OUTPUT_COLOR,
            stroke_width=5,
        )
        self.range_label = MathTex(r"\text{range}", color=self.OUTPUT_COLOR).scale(0.48)
        self.range_label.next_to(self.range_line, LEFT, buff=0.1)

    def create_graph_objects(self):
        self.graph = self.make_graph(lambda x: 0.45 * x**2 + 0.35, -2.1, 2.1, self.GRAPH_COLOR)
        self.graph_points = VGroup(
            Dot(self.axes.c2p(-1.5, 0.45 * (-1.5) ** 2 + 0.35), radius=0.07, color=self.INPUT_COLOR),
            Dot(self.axes.c2p(0, 0.35), radius=0.07, color=self.INPUT_COLOR),
            Dot(self.axes.c2p(1.4, 0.45 * (1.4) ** 2 + 0.35), radius=0.07, color=self.INPUT_COLOR),
        )
        self.pair_label = MathTex("(x,", "f(x)", ")", color=WHITE).scale(0.58)
        self.pair_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.pair_label.set_color_by_tex("f(x)", self.OUTPUT_COLOR)
        self.pair_label.move_to([2.72, 1.15, 0])
        self.pair_arrow = Arrow(
            self.pair_label.get_left() + LEFT * 0.08,
            self.axes.c2p(1.4, 0.45 * (1.4) ** 2 + 0.35) + RIGHT * 0.1,
            color=self.GUIDE_COLOR,
            buff=0.12,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.12,
        )

    def create_vertical_test(self):
        self.test_line = DashedLine(
            self.axes.c2p(1.2, -0.4),
            self.axes.c2p(1.2, 3.25),
            color=self.DOMAIN_COLOR,
            stroke_width=3,
            dash_length=0.16,
        )
        self.test_dot = Dot(self.axes.c2p(1.2, 0.45 * (1.2) ** 2 + 0.35), radius=0.08, color=self.DOMAIN_COLOR)
        self.test_label = MathTex(r"\text{one hit}", color=self.DOMAIN_COLOR).scale(0.54)
        self.test_label.move_to([2.75, 0.38, 0])

    def create_family_cards(self):
        self.family_header = MathTex(r"\text{common families}", color=WHITE).scale(0.58)
        self.family_header.move_to([2.75, 2.05, 0])

        self.algebraic_cards = VGroup(
            self.make_card(r"\text{linear}", self.FAMILY_COLOR, width=1.2),
            self.make_card(r"\text{power}", self.FAMILY_COLOR, width=1.2),
            self.make_card(r"\text{polynomial}", self.FAMILY_COLOR, width=1.55),
            self.make_card(r"\text{rational}", self.FAMILY_COLOR, width=1.3),
            self.make_card(r"\text{algebraic}", self.FAMILY_COLOR, width=1.45),
        )
        self.algebraic_cards.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        self.algebraic_cards.move_to([2.05, -0.55, 0])

        self.trans_cards = VGroup(
            self.make_card(r"\sin x", self.TRANSCENDENTAL_COLOR, width=1.15),
            self.make_card(r"e^x", self.TRANSCENDENTAL_COLOR, width=1.0),
            self.make_card(r"\log x", self.TRANSCENDENTAL_COLOR, width=1.15),
            self.make_card(r"\cosh x", self.TRANSCENDENTAL_COLOR, width=1.2),
        )
        self.trans_cards.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        self.trans_cards.move_to([3.85, -0.6, 0])

        self.algebraic_label = MathTex(r"\text{algebraic}", color=self.FAMILY_COLOR).scale(0.48)
        self.algebraic_label.next_to(self.algebraic_cards, UP, buff=0.12)
        self.trans_label = MathTex(r"\text{transcendental}", color=self.TRANSCENDENTAL_COLOR).scale(0.48)
        self.trans_label.next_to(self.trans_cards, UP, buff=0.12)

    def create_final_summary(self):
        self.final_cards = VGroup(
            self.make_card(r"\text{rule}", self.FAMILY_COLOR, width=1.0),
            self.make_card(r"\text{domain}", self.INPUT_COLOR, width=1.25),
            self.make_card(r"\text{range}", self.OUTPUT_COLOR, width=1.15),
            self.make_card(r"\text{graph}", self.GRAPH_COLOR, width=1.1),
            self.make_card(r"\text{family}", self.TRANSCENDENTAL_COLOR, width=1.25),
        )
        self.final_cards.arrange(RIGHT, buff=0.16)
        self.final_cards.to_edge(DOWN, buff=0.34)

        self.final_statement = MathTex(r"\text{rules become shapes}", color=WHITE).scale(0.64)
        self.final_statement.move_to([0.75, 2.35, 0])

    def step1_show_function_rule(self):
        self.play(FadeIn(self.rule_row), Write(self.rule_label), run_time=2)
        self.wait()

    def step2_mark_domain_and_range(self):
        self.play(
            Create(self.axes),
            FadeIn(self.axis_labels),
            Create(self.domain_line),
            Write(self.domain_label),
            Create(self.range_line),
            Write(self.range_label),
            run_time=2,
        )
        self.wait()

    def step3_turn_pairs_into_graph(self):
        self.play(FadeIn(self.graph_points), Write(self.pair_label), Create(self.pair_arrow), run_time=2)
        self.wait()
        self.play(Create(self.graph), run_time=3)
        self.wait()

    def step4_check_function_graph(self):
        self.play(Create(self.test_line), FadeIn(self.test_dot), Write(self.test_label), run_time=2)
        self.wait()

    def step5_group_common_families(self):
        self.play(Write(self.family_header), FadeIn(self.algebraic_cards), run_time=2)
        self.wait()

    def step6_split_algebraic_transcendental(self):
        self.play(
            Write(self.algebraic_label),
            FadeIn(self.trans_cards),
            Write(self.trans_label),
            run_time=2,
        )
        self.wait()

    def step7_final_summary(self):
        self.play(
            FadeOut(self.rule_label),
            FadeOut(self.rule_row),
            FadeOut(self.domain_label),
            FadeOut(self.range_label),
            FadeOut(self.pair_label),
            FadeOut(self.pair_arrow),
            FadeOut(self.family_header),
            FadeOut(self.test_label),
            FadeOut(self.algebraic_label),
            FadeOut(self.trans_label),
            FadeIn(self.final_statement),
            run_time=2,
        )
        self.wait()

    def make_graph(self, function, x_start, x_end, color):
        points = []
        samples = 140
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=4)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_card(self, label, color, width=1.2):
        box = RoundedRectangle(
            width=width,
            height=0.46,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.2,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(label, color=color).scale(0.44)
        text.move_to(box)
        return VGroup(box, text)
