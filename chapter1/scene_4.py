from manim import *


class Scene4_UniqueOutput(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    ERROR_COLOR = RED
    VALID_COLOR = BLUE

    def construct(self):
        self.setup_layout()
        self.step1_create_assignment_area()
        self.step2_show_valid_assignment()
        self.step3_show_shared_output()
        self.step4_mark_shared_output_allowed()
        self.step5_create_test_input()
        self.step6_show_split_arrows()
        self.step7_show_conflicting_outputs()
        self.step8_reject_split()
        self.step9_state_rule_visually()
        self.step10_write_formal_rule()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.left_x = -4.2
        self.right_x = 4.2
        self.valid_y1 = 1.7
        self.valid_y2 = 0.8
        self.test_y = -1.25

        self.create_assignment_area()
        self.create_valid_case()
        self.create_invalid_case()
        self.create_rule_summary()
        self.create_formal_rule()

    def create_assignment_area(self):
        self.input_label = Text("inputs", font_size=30, color=self.INPUT_COLOR)
        self.output_label = Text("outputs", font_size=30, color=self.OUTPUT_COLOR)
        self.input_label.move_to([self.left_x, 2.7, 0])
        self.output_label.move_to([self.right_x, 2.7, 0])

        self.center_lane = DashedLine(
            [-1.15, 2.45, 0],
            [1.15, 2.45, 0],
            color=GREY_B,
            dash_length=0.12,
        )
        self.area = VGroup(self.input_label, self.output_label, self.center_lane)

    def create_valid_case(self):
        self.x1 = self.make_card("x=1", self.INPUT_COLOR).move_to([self.left_x, self.valid_y1, 0])
        self.x4_valid = self.make_card("x=4", self.INPUT_COLOR).move_to([self.left_x, self.valid_y2, 0])
        self.y3 = self.make_card("y=3", self.OUTPUT_COLOR).move_to([self.right_x, 1.25, 0])

        self.arrow_x1_y3 = self.make_arrow(self.x1, self.y3)
        self.arrow_x4_y3 = self.make_arrow(self.x4_valid, self.y3)
        self.valid_assignment = VGroup(self.x1, self.arrow_x1_y3, self.y3)
        self.shared_assignment = VGroup(self.x4_valid, self.arrow_x4_y3)

        self.valid_marker = Circle(radius=0.22, color=self.VALID_COLOR)
        self.valid_marker.next_to(self.y3, RIGHT, buff=0.25)
        self.valid_check = MathTex(r"\checkmark", color=self.VALID_COLOR).scale(0.85)
        self.valid_check.move_to(self.valid_marker)
        self.valid_badge = VGroup(self.valid_marker, self.valid_check)

    def create_invalid_case(self):
        self.x2 = self.make_card("x=2", self.INPUT_COLOR).move_to([self.left_x, self.test_y, 0])
        self.y5 = self.make_card("y=5", self.OUTPUT_COLOR).move_to([self.right_x, -0.75, 0])
        self.y7 = self.make_card("y=7", self.OUTPUT_COLOR).move_to([self.right_x, -1.75, 0])

        self.arrow_x2_y5 = self.make_arrow(self.x2, self.y5, color=GREY_B)
        self.arrow_x2_y7 = self.make_arrow(self.x2, self.y7, color=GREY_B)
        self.split_arrows = VGroup(self.arrow_x2_y5, self.arrow_x2_y7)
        self.conflicting_outputs = VGroup(self.y5, self.y7)
        self.invalid_split = VGroup(self.x2, self.split_arrows, self.conflicting_outputs)

        self.invalid_cross = Cross(self.split_arrows, stroke_color=self.ERROR_COLOR, stroke_width=8)

    def create_rule_summary(self):
        self.rule_input = self.make_card("one input", self.INPUT_COLOR, width=1.75)
        self.rule_output = self.make_card("one output", self.OUTPUT_COLOR, width=1.95)
        self.rule_arrow = Arrow(LEFT, RIGHT, buff=0, color=WHITE, stroke_width=5)
        self.rule_arrow.set_width(1.35)
        self.rule_summary = VGroup(self.rule_input, self.rule_arrow, self.rule_output)
        self.rule_summary.arrange(RIGHT, buff=0.4)
        self.rule_summary.move_to([0, -2.55, 0])

    def create_formal_rule(self):
        self.formal_rule = Text(
            "Each input has exactly one output.",
            font_size=32,
            color=WHITE,
        )
        self.formal_rule.to_edge(DOWN, buff=0.35)
        self.formal_rule.set_color_by_t2c({
            "input": self.INPUT_COLOR,
            "one output": self.OUTPUT_COLOR,
        })

    def step1_create_assignment_area(self):
        self.play(FadeIn(self.area), run_time=2)
        self.wait()

    def step2_show_valid_assignment(self):
        self.play(FadeIn(self.valid_assignment), run_time=2)
        self.wait()

    def step3_show_shared_output(self):
        self.play(FadeIn(self.shared_assignment), run_time=2)
        self.wait()

    def step4_mark_shared_output_allowed(self):
        self.play(Indicate(self.y3, color=self.VALID_COLOR), FadeIn(self.valid_badge), run_time=2)
        self.wait()

    def step5_create_test_input(self):
        self.play(FadeIn(self.x2), run_time=2)
        self.wait()

    def step6_show_split_arrows(self):
        self.play(Create(self.split_arrows), run_time=2)
        self.wait()

    def step7_show_conflicting_outputs(self):
        self.play(FadeIn(self.conflicting_outputs), run_time=2)
        self.wait()

    def step8_reject_split(self):
        self.play(Indicate(self.invalid_split, color=self.ERROR_COLOR), FadeIn(self.invalid_cross), run_time=2)
        self.wait()

    def step9_state_rule_visually(self):
        self.play(
            FadeOut(VGroup(self.invalid_split, self.invalid_cross)),
            ReplacementTransform(VGroup(self.x1.copy(), self.y3.copy()), self.rule_summary),
            run_time=2,
        )
        self.wait()

    def step10_write_formal_rule(self):
        self.play(Write(self.formal_rule), run_time=2)
        self.wait()

    def make_card(self, label, color, width=1.15, height=0.6):
        box = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.12,
        )
        if " " in label:
            text = Text(label, font_size=22, color=color, slant=ITALIC)
        else:
            text = MathTex(label, color=color).scale(0.7)
        text.move_to(box)
        return VGroup(box, text)

    def make_arrow(self, start_card, end_card, color=WHITE):
        return Arrow(
            start_card.get_right(),
            end_card.get_left(),
            buff=0.18,
            color=color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.08,
        )
