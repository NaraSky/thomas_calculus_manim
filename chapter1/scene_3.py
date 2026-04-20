from manim import *


class Scene3_DomainRange(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    SET_COLOR = WHITE
    RANGE_COLOR = BLUE

    def construct(self):
        self.setup_layout()
        self.step1_create_pairs()
        self.step2_separate_inputs()
        self.step3_separate_outputs()
        self.step4_create_domain()
        self.step5_create_output_set()
        self.step6_highlight_range()
        self.step7_draw_assignment_arrows()
        self.step8_add_shared_output_input()
        self.step9_connect_shared_output()
        self.step10_emphasize_range()
        self.step11_write_notation()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.left_x = -3.55
        self.right_x = 3.55
        self.top_y = 1.15
        self.mid_y = 0.25
        self.bottom_y = -0.65

        self.create_cards()
        self.create_sets()
        self.create_arrows()
        self.create_notation()

    def create_cards(self):
        self.x1_start = self.make_card("x=1", self.INPUT_COLOR)
        self.y3_start = self.make_card("y=3", self.OUTPUT_COLOR)
        self.x2_start = self.make_card("x=2", self.INPUT_COLOR)
        self.y5_start = self.make_card("y=5", self.OUTPUT_COLOR)

        self.pair_1 = VGroup(self.x1_start, self.y3_start).arrange(RIGHT, buff=0.25)
        self.pair_2 = VGroup(self.x2_start, self.y5_start).arrange(RIGHT, buff=0.25)
        self.pairs = VGroup(self.pair_1, self.pair_2).arrange(RIGHT, buff=1.1)
        self.pairs.move_to([0, 1.1, 0])

        self.x1_target = self.x1_start.copy().move_to([self.left_x, self.top_y, 0])
        self.x2_target = self.x2_start.copy().move_to([self.left_x, self.mid_y, 0])
        self.x4 = self.make_card("x=4", self.INPUT_COLOR).move_to([self.left_x, self.bottom_y, 0])

        self.y3_target = self.y3_start.copy().move_to([self.right_x, self.top_y, 0])
        self.y5_target = self.y5_start.copy().move_to([self.right_x, self.mid_y, 0])

        self.input_cards = VGroup(self.x1_start, self.x2_start, self.x4)
        self.output_cards = VGroup(self.y3_start, self.y5_start)

    def create_sets(self):
        self.domain_boundary = Ellipse(width=2.2, height=3.1, color=self.SET_COLOR)
        self.domain_boundary.move_to([self.left_x, 0.25, 0])
        self.domain_label = Text("Domain D", font_size=30, color=self.INPUT_COLOR)
        self.domain_label.next_to(self.domain_boundary, UP, buff=0.2)
        self.domain_set = VGroup(self.domain_boundary, self.domain_label)

        self.output_boundary = Ellipse(width=2.75, height=3.7, color=GREY_B)
        self.output_boundary.move_to([self.right_x, 0.1, 0])
        self.output_label = Text("Output set Y", font_size=30, color=GREY_B)
        self.output_label.next_to(self.output_boundary, UP, buff=0.2)
        self.output_set = VGroup(self.output_boundary, self.output_label)

        self.range_boundary = Ellipse(width=2.0, height=1.95, color=self.RANGE_COLOR)
        self.range_boundary.move_to([self.right_x, 0.7, 0])
        self.range_label = Text("Range", font_size=30, color=self.RANGE_COLOR)
        self.range_label.next_to(self.range_boundary, RIGHT, buff=0.2)
        self.range_set = VGroup(self.range_boundary, self.range_label)

    def create_arrows(self):
        self.arrow_x1_y3 = Arrow(
            self.x1_target.get_right(),
            self.y3_target.get_left(),
            buff=0.18,
            color=WHITE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.08,
        )
        self.arrow_x2_y5 = Arrow(
            self.x2_target.get_right(),
            self.y5_target.get_left(),
            buff=0.18,
            color=WHITE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.08,
        )
        self.arrow_x4_y5 = Arrow(
            self.x4.get_right(),
            self.y5_target.get_left(),
            buff=0.18,
            color=WHITE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.08,
        )
        self.assignment_arrows = VGroup(self.arrow_x1_y3, self.arrow_x2_y5)

    def create_notation(self):
        self.notation_1 = MathTex("x", r"\in", "D", color=WHITE)
        self.notation_1.set_color_by_tex("x", self.INPUT_COLOR)
        self.notation_1.set_color_by_tex("D", self.INPUT_COLOR)

        self.notation_2 = MathTex("f(x)", r"\in", "Y", color=WHITE)
        self.notation_2.set_color_by_tex("f(x)", self.OUTPUT_COLOR)
        self.notation_2.set_color_by_tex("Y", GREY_B)

        self.notation_3 = MathTex(r"\text{Range}", "=", r"\{f(x)\mid x\in D\}", color=WHITE)
        self.notation_3.set_color_by_tex("Range", self.RANGE_COLOR)
        self.notation_3.set_color_by_tex("f(x)", self.OUTPUT_COLOR)
        self.notation_3.set_color_by_tex("D", self.INPUT_COLOR)

        self.notation = VGroup(
            self.notation_1,
            self.notation_2,
            self.notation_3,
        )
        self.notation.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        self.notation.scale(0.68)
        self.notation.move_to([0, -3.15, 0])

    def step1_create_pairs(self):
        self.play(FadeIn(self.pairs), run_time=2)
        self.wait()

    def step2_separate_inputs(self):
        self.play(
            Transform(self.x1_start, self.x1_target),
            Transform(self.x2_start, self.x2_target),
            run_time=2,
        )
        self.wait()

    def step3_separate_outputs(self):
        self.play(
            Transform(self.y3_start, self.y3_target),
            Transform(self.y5_start, self.y5_target),
            run_time=2,
        )
        self.wait()

    def step4_create_domain(self):
        self.play(Create(self.domain_set), run_time=2)
        self.wait()

    def step5_create_output_set(self):
        self.play(Create(self.output_set), run_time=2)
        self.wait()

    def step6_highlight_range(self):
        self.play(Create(self.range_set), run_time=2)
        self.wait()

    def step7_draw_assignment_arrows(self):
        self.play(Create(self.assignment_arrows), run_time=2)
        self.wait()

    def step8_add_shared_output_input(self):
        self.play(FadeIn(self.x4), run_time=2)
        self.wait()

    def step9_connect_shared_output(self):
        self.play(Create(self.arrow_x4_y5), run_time=2)
        self.wait()

    def step10_emphasize_range(self):
        self.play(Indicate(self.range_set, color=self.RANGE_COLOR), run_time=2)
        self.wait()

    def step11_write_notation(self):
        self.play(Write(self.notation), run_time=2)
        self.wait()

    def make_card(self, label, color):
        box = RoundedRectangle(
            width=1.15,
            height=0.6,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(label, color=color).scale(0.7)
        text.move_to(box)
        return VGroup(box, text)
