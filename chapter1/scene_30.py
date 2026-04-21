from manim import *


class Scene30_CompositeDomainCondition(Scene):
    INPUT_COLOR = YELLOW
    G_COLOR = GREEN
    F_COLOR = TEAL
    DOMAIN_COLOR = BLUE
    RESULT_COLOR = BLUE
    WARNING_COLOR = RED
    GUIDE_COLOR = GREY_B
    QUICK_TIME = 0.55
    DEFAULT_TIME = 0.85
    EMPHASIS_TIME = 1.25
    PAUSE_TIME = 0.18

    def construct(self):
        self.setup_layout()
        self.step1_show_composition_rule()
        self.step2_show_input_line()
        self.step3_show_g_line()
        self.step4_show_g_rule()
        self.step5_show_shift_arrow()
        self.step6_show_f_domain_region()
        self.step7_show_f_domain_formula()
        self.step8_highlight_f_domain_formula()
        self.step9_choose_invalid_input()
        self.step10_map_invalid_input()
        self.step11_block_invalid_output()
        self.step12_choose_boundary_input()
        self.step13_map_boundary_input()
        self.step14_accept_boundary_output()
        self.step15_choose_valid_input()
        self.step16_map_valid_input()
        self.step17_accept_valid_output()
        self.step18_mark_allowed_input_region()
        self.step19_declutter_samples()
        self.step20_write_domain_condition()
        self.step21_write_domain_result()
        self.step22_summarize_domain_condition()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.create_formula_objects()
        self.create_number_lines()
        self.create_mapping_objects()
        self.create_domain_objects()
        self.create_summary_objects()

    def create_formula_objects(self):
        self.composition_formula = MathTex(
            "(f\\circ g)(x)",
            "=",
            "f(g(x))",
            color=WHITE,
        ).scale(0.7)
        self.composition_formula.set_color_by_tex("f", self.F_COLOR)
        self.composition_formula.set_color_by_tex("g", self.G_COLOR)
        self.composition_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.composition_formula.move_to([-3.6, 2.55, 0])

        self.g_formula = MathTex("g(x)", "=", "x+1", color=WHITE).scale(0.62)
        self.g_formula.set_color_by_tex("g", self.G_COLOR)
        self.g_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.g_formula.move_to([2.9, 2.55, 0])

        self.f_domain_formula = MathTex("D_f", "=", "[0,\\infty)", color=WHITE).scale(0.62)
        self.f_domain_formula.set_color_by_tex("D_f", self.F_COLOR)
        self.f_domain_formula.set_color_by_tex("[0,\\infty)", self.DOMAIN_COLOR)
        self.f_domain_formula.move_to([2.9, 1.88, 0])
        self.f_domain_formula_highlight = SurroundingRectangle(
            self.f_domain_formula,
            color=self.DOMAIN_COLOR,
            buff=0.1,
            stroke_width=2.5,
        )

        self.domain_result = MathTex("D_{f\\circ g}", "=", "[-1,\\infty)", color=WHITE).scale(0.68)
        self.domain_result.set_color_by_tex("D_{f\\circ g}", self.RESULT_COLOR)
        self.domain_result.set_color_by_tex("[-1,\\infty)", self.INPUT_COLOR)
        self.domain_result.move_to([2.85, -1.82, 0])

        self.condition_formula = MathTex("g(x)", "\\in", "D_f", color=WHITE).scale(0.58)
        self.condition_formula.set_color_by_tex("g", self.G_COLOR)
        self.condition_formula.set_color_by_tex("D_f", self.F_COLOR)
        self.condition_formula.move_to([-3.7, -1.82, 0])

    def create_number_lines(self):
        self.x_line = NumberLine(
            x_range=[-3, 3, 1],
            length=5.6,
            color=self.GUIDE_COLOR,
            include_numbers=False,
        )
        self.x_line.move_to([-1.2, 0.55, 0])

        self.g_line = NumberLine(
            x_range=[-2, 4, 1],
            length=5.6,
            color=self.GUIDE_COLOR,
            include_numbers=False,
        )
        self.g_line.move_to([-1.2, -0.75, 0])

        self.x_line_label = MathTex("x", color=self.INPUT_COLOR).scale(0.62)
        self.x_line_label.next_to(self.x_line, LEFT, buff=0.28)
        self.g_line_label = MathTex("g(x)", color=self.G_COLOR).scale(0.58)
        self.g_line_label.next_to(self.g_line, LEFT, buff=0.22)

        self.g_arrow = Arrow(
            self.x_line.n2p(0) + DOWN * 0.16,
            self.g_line.n2p(1) + UP * 0.16,
            color=self.G_COLOR,
            stroke_width=4,
            buff=0.05,
            max_tip_length_to_length_ratio=0.12,
        )
        self.g_arrow_label = MathTex("+1", color=self.G_COLOR).scale(0.54)
        self.g_arrow_label.next_to(self.g_arrow, RIGHT, buff=0.08)

    def create_mapping_objects(self):
        self.invalid_x_dot = Dot(self.x_line.n2p(-2), radius=0.08, color=self.WARNING_COLOR)
        self.invalid_x_label = MathTex("-2", color=self.WARNING_COLOR).scale(0.46)
        self.invalid_x_label.next_to(self.invalid_x_dot, UP, buff=0.12)
        self.invalid_g_dot = Dot(self.g_line.n2p(-1), radius=0.08, color=self.WARNING_COLOR)
        self.invalid_g_label = MathTex("g(-2)=-1", color=self.WARNING_COLOR).scale(0.44)
        self.invalid_g_label.next_to(self.invalid_g_dot, DOWN, buff=0.18)
        self.invalid_arrow = self.make_mapping_arrow(self.invalid_x_dot, self.invalid_g_dot, self.WARNING_COLOR)

        self.boundary_x_dot = Dot(self.x_line.n2p(-1), radius=0.08, color=self.INPUT_COLOR)
        self.boundary_x_label = MathTex("-1", color=self.INPUT_COLOR).scale(0.46)
        self.boundary_x_label.next_to(self.boundary_x_dot, UP, buff=0.12)
        self.boundary_g_dot = Dot(self.g_line.n2p(0), radius=0.08, color=self.DOMAIN_COLOR)
        self.boundary_g_label = MathTex("g(-1)=0", color=self.DOMAIN_COLOR).scale(0.44)
        self.boundary_g_label.next_to(self.boundary_g_dot, DOWN, buff=0.18)
        self.boundary_arrow = self.make_mapping_arrow(self.boundary_x_dot, self.boundary_g_dot, self.DOMAIN_COLOR)

        self.valid_x_dot = Dot(self.x_line.n2p(1), radius=0.08, color=self.INPUT_COLOR)
        self.valid_x_label = MathTex("1", color=self.INPUT_COLOR).scale(0.46)
        self.valid_x_label.next_to(self.valid_x_dot, UP, buff=0.12)
        self.valid_g_dot = Dot(self.g_line.n2p(2), radius=0.08, color=self.DOMAIN_COLOR)
        self.valid_g_label = MathTex("g(1)=2", color=self.DOMAIN_COLOR).scale(0.44)
        self.valid_g_label.next_to(self.valid_g_dot, DOWN, buff=0.18)
        self.valid_arrow = self.make_mapping_arrow(self.valid_x_dot, self.valid_g_dot, self.DOMAIN_COLOR)

    def create_domain_objects(self):
        self.f_domain_region = Line(
            self.g_line.n2p(0),
            self.g_line.n2p(4),
            color=self.DOMAIN_COLOR,
            stroke_width=7,
        )
        self.f_domain_start = Dot(self.g_line.n2p(0), radius=0.08, color=self.DOMAIN_COLOR)
        self.f_domain_label = MathTex("[0,\\infty)", color=self.DOMAIN_COLOR).scale(0.5)
        self.f_domain_label.next_to(self.f_domain_region, UP, buff=0.18)

        self.invalid_gate = VGroup(
            Line(LEFT * 0.13 + UP * 0.13, RIGHT * 0.13 + DOWN * 0.13, color=self.WARNING_COLOR, stroke_width=5),
            Line(LEFT * 0.13 + DOWN * 0.13, RIGHT * 0.13 + UP * 0.13, color=self.WARNING_COLOR, stroke_width=5),
        )
        self.invalid_gate.move_to(self.invalid_g_dot.get_center() + RIGHT * 0.42)

        self.accept_boundary = self.make_check(self.boundary_g_dot.get_center() + RIGHT * 0.42, self.DOMAIN_COLOR)
        self.accept_valid = self.make_check(self.valid_g_dot.get_center() + RIGHT * 0.42, self.DOMAIN_COLOR)

        self.allowed_x_region = Line(
            self.x_line.n2p(-1),
            self.x_line.n2p(3),
            color=self.INPUT_COLOR,
            stroke_width=7,
        )
        self.allowed_x_start = Dot(self.x_line.n2p(-1), radius=0.08, color=self.INPUT_COLOR)
        self.allowed_x_label = MathTex("[-1,\\infty)", color=self.INPUT_COLOR).scale(0.5)
        self.allowed_x_label.next_to(self.allowed_x_region, UP, buff=0.18)

    def create_summary_objects(self):
        self.summary_cards = VGroup(
            self.make_card("choose x", self.INPUT_COLOR, width=1.1),
            self.make_card("compute g(x)", self.G_COLOR, width=1.45),
            self.make_card("fit domain", self.F_COLOR, width=1.35),
        )
        self.summary_cards.arrange(RIGHT, buff=0.16)
        self.summary_cards.to_edge(DOWN, buff=0.35)

    def step1_show_composition_rule(self):
        self.play(Write(self.composition_formula), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def step2_show_input_line(self):
        self.play(Create(self.x_line), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.x_line_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step3_show_g_line(self):
        self.play(Create(self.g_line), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.g_line_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step4_show_g_rule(self):
        self.play(Write(self.g_formula), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def step5_show_shift_arrow(self):
        self.play(Create(self.g_arrow), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.g_arrow_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step6_show_f_domain_region(self):
        self.play(Create(self.f_domain_region), run_time=self.EMPHASIS_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(FadeIn(self.f_domain_start), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.f_domain_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step7_show_f_domain_formula(self):
        self.play(Write(self.f_domain_formula), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def step8_highlight_f_domain_formula(self):
        self.play(Create(self.f_domain_formula_highlight), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(FadeOut(self.f_domain_formula_highlight), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step9_choose_invalid_input(self):
        self.play(FadeIn(self.invalid_x_dot), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.invalid_x_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step10_map_invalid_input(self):
        self.play(Create(self.invalid_arrow), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(FadeIn(self.invalid_g_dot), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.invalid_g_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step11_block_invalid_output(self):
        self.play(FadeIn(self.invalid_gate), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def step12_choose_boundary_input(self):
        self.play(FadeIn(self.boundary_x_dot), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.boundary_x_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step13_map_boundary_input(self):
        self.play(Create(self.boundary_arrow), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(FadeIn(self.boundary_g_dot), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.boundary_g_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step14_accept_boundary_output(self):
        self.play(Create(self.accept_boundary), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def step15_choose_valid_input(self):
        self.play(FadeIn(self.valid_x_dot), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.valid_x_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step16_map_valid_input(self):
        self.play(Create(self.valid_arrow), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(FadeIn(self.valid_g_dot), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.valid_g_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step17_accept_valid_output(self):
        self.play(Create(self.accept_valid), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def step18_mark_allowed_input_region(self):
        self.play(Create(self.allowed_x_region), run_time=self.EMPHASIS_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(FadeIn(self.allowed_x_start), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)
        self.play(Write(self.allowed_x_label), run_time=self.QUICK_TIME)
        self.wait(self.PAUSE_TIME)

    def step19_declutter_samples(self):
        sample_annotations = VGroup(
            self.invalid_g_label,
            self.boundary_g_label,
            self.valid_g_label,
            self.invalid_gate,
            self.accept_boundary,
            self.accept_valid,
        )
        self.play(FadeOut(sample_annotations), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def step20_write_domain_condition(self):
        self.play(Write(self.condition_formula), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def step21_write_domain_result(self):
        self.play(Write(self.domain_result), run_time=self.EMPHASIS_TIME)
        self.wait(self.PAUSE_TIME)

    def step22_summarize_domain_condition(self):
        self.play(FadeIn(self.summary_cards), run_time=self.DEFAULT_TIME)
        self.wait(self.PAUSE_TIME)

    def make_mapping_arrow(self, start_dot, end_dot, color):
        return Arrow(
            start_dot.get_center() + DOWN * 0.08,
            end_dot.get_center() + UP * 0.08,
            color=color,
            stroke_width=3.5,
            buff=0.06,
            max_tip_length_to_length_ratio=0.12,
        )

    def make_check(self, center, color):
        check = VMobject(color=color, stroke_width=5)
        check.set_points_as_corners([
            center + LEFT * 0.13 + DOWN * 0.01,
            center + LEFT * 0.03 + DOWN * 0.11,
            center + RIGHT * 0.16 + UP * 0.12,
        ])
        return check

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
        text = MathTex(r"\text{" + label + "}", color=color).scale(0.42)
        text.move_to(box)
        return VGroup(box, text)
