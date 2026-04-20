from manim import *


class Scene2_FunctionMachine(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    MACHINE_COLOR = WHITE
    ERROR_COLOR = RED

    def construct(self):
        self.setup_layout()
        self.step1_create_machine()
        self.step2_create_first_input()
        self.step3_move_first_input()
        self.step4_show_first_output()
        self.step5_create_second_input()
        self.step6_move_second_input()
        self.step7_show_second_output()
        self.step8_show_invalid_split()
        self.step9_reject_invalid_split()
        self.step10_return_to_valid_rule()
        self.step11_write_notation()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.left_x = -4.7
        self.machine_x = 0
        self.right_x = 4.7
        self.main_y = 0.55
        self.history_y = -2.25

        self.create_machine()
        self.create_lanes()
        self.create_valid_cards()
        self.create_invalid_case()
        self.create_notation()

    def create_machine(self):
        self.machine_box = RoundedRectangle(
            width=2.0,
            height=1.35,
            corner_radius=0.12,
            stroke_color=self.MACHINE_COLOR,
            stroke_width=3,
        )
        self.machine_box.move_to([self.machine_x, self.main_y, 0])
        self.machine_label = MathTex("f", color=self.MACHINE_COLOR).scale(1.55)
        self.machine_label.move_to(self.machine_box)
        self.machine = VGroup(self.machine_box, self.machine_label)

        self.title = Text("Function machine", font_size=34, color=WHITE)
        self.title.next_to(self.machine_box, UP, buff=0.55)

    def create_lanes(self):
        self.input_lane = Arrow(
            [self.left_x + 1.1, self.main_y, 0],
            [self.machine_box.get_left()[0] - 0.2, self.main_y, 0],
            buff=0,
            color=WHITE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12,
        )
        self.output_lane = Arrow(
            [self.machine_box.get_right()[0] + 0.2, self.main_y, 0],
            [self.right_x - 1.1, self.main_y, 0],
            buff=0,
            color=WHITE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12,
        )
        self.lanes = VGroup(self.input_lane, self.output_lane)

    def create_valid_cards(self):
        self.first_input_start = self.make_card("x=1", self.INPUT_COLOR)
        self.first_input_start.move_to([self.left_x, self.main_y, 0])
        self.first_input_in_machine = self.first_input_start.copy().scale(0.75)
        self.first_input_in_machine.move_to(self.machine_box)
        self.first_output = self.make_card("y=3", self.OUTPUT_COLOR)
        self.first_output.move_to([self.right_x, self.main_y, 0])

        self.second_input_start = self.make_card("x=2", self.INPUT_COLOR)
        self.second_input_start.move_to([self.left_x, self.main_y, 0])
        self.second_input_in_machine = self.second_input_start.copy().scale(0.75)
        self.second_input_in_machine.move_to(self.machine_box)
        self.second_output = self.make_card("y=5", self.OUTPUT_COLOR)
        self.second_output.move_to([self.right_x, self.main_y, 0])

        self.first_pair = VGroup(
            self.make_card("x=1", self.INPUT_COLOR),
            self.make_card("y=3", self.OUTPUT_COLOR),
        ).arrange(RIGHT, buff=0.3)
        self.second_pair = VGroup(
            self.make_card("x=2", self.INPUT_COLOR),
            self.make_card("y=5", self.OUTPUT_COLOR),
        ).arrange(RIGHT, buff=0.3)
        self.valid_examples = VGroup(self.first_pair, self.second_pair).arrange(RIGHT, buff=1.0)
        self.valid_examples.move_to([0, self.history_y, 0])
        self.first_pair.move_to([-1.8, self.history_y, 0])
        self.second_pair.move_to([1.8, self.history_y, 0])

        self.valid_rule = VGroup(
            self.make_card("one input", self.INPUT_COLOR, width=1.65),
            Arrow(LEFT, RIGHT, buff=0, color=WHITE).set_width(1.2),
            self.make_card("one output", self.OUTPUT_COLOR, width=1.85),
        ).arrange(RIGHT, buff=0.35)
        self.valid_rule.move_to([0, self.history_y, 0])

    def create_invalid_case(self):
        self.invalid_input = self.make_card("x=4", self.INPUT_COLOR)
        self.invalid_input.move_to([self.left_x + 0.35, -1.0, 0])

        self.invalid_output_a = self.make_card("y=7", self.OUTPUT_COLOR)
        self.invalid_output_b = self.make_card("y=9", self.OUTPUT_COLOR)
        self.invalid_output_a.move_to([self.right_x - 0.35, -0.85, 0])
        self.invalid_output_b.move_to([self.right_x - 0.35, -1.75, 0])

        self.split_arrow_a = Arrow(
            self.invalid_input.get_right(),
            self.invalid_output_a.get_left(),
            buff=0.15,
            color=GREY_B,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.08,
        )
        self.split_arrow_b = Arrow(
            self.invalid_input.get_right(),
            self.invalid_output_b.get_left(),
            buff=0.15,
            color=GREY_B,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.08,
        )
        self.invalid_split = VGroup(
            self.invalid_input,
            self.split_arrow_a,
            self.split_arrow_b,
            self.invalid_output_a,
            self.invalid_output_b,
        )
        self.invalid_split.set_opacity(0.65)

        self.invalid_marker = Cross(self.invalid_split, stroke_color=self.ERROR_COLOR, stroke_width=8)

    def create_notation(self):
        self.notation = MathTex("y", "=", "f", "(", "x", ")", color=WHITE)
        self.notation.scale(1.25)
        self.notation.set_color_by_tex("x", self.INPUT_COLOR)
        self.notation.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.notation.set_color_by_tex("f", self.MACHINE_COLOR)
        self.notation.to_edge(DOWN, buff=0.4)

    def step1_create_machine(self):
        self.play(FadeIn(VGroup(self.title, self.machine, self.lanes)), run_time=2)
        self.wait()

    def step2_create_first_input(self):
        self.play(FadeIn(self.first_input_start), run_time=2)
        self.wait()

    def step3_move_first_input(self):
        self.play(Transform(self.first_input_start, self.first_input_in_machine), run_time=2)
        self.wait()

    def step4_show_first_output(self):
        self.play(ReplacementTransform(self.first_input_start, self.first_output), run_time=2)
        self.wait()

    def step5_create_second_input(self):
        self.play(
            ReplacementTransform(self.first_output, self.first_pair),
            FadeIn(self.second_input_start),
            run_time=2,
        )
        self.wait()

    def step6_move_second_input(self):
        self.play(Transform(self.second_input_start, self.second_input_in_machine), run_time=2)
        self.wait()

    def step7_show_second_output(self):
        self.play(ReplacementTransform(self.second_input_start, self.second_output), run_time=2)
        self.wait()

    def step8_show_invalid_split(self):
        self.play(
            ReplacementTransform(self.second_output, self.second_pair),
            FadeIn(self.invalid_split),
            run_time=2,
        )
        self.wait()

    def step9_reject_invalid_split(self):
        self.play(Indicate(self.invalid_split, color=self.ERROR_COLOR), FadeIn(self.invalid_marker), run_time=2)
        self.wait()

    def step10_return_to_valid_rule(self):
        self.play(
            FadeOut(VGroup(self.invalid_split, self.invalid_marker)),
            run_time=2,
        )
        self.wait()

    def step11_write_notation(self):
        self.play(Write(self.notation), run_time=2)
        self.wait()

    def make_card(self, label, color, width=1.25, height=0.65):
        box = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(label, color=color).scale(0.75)
        text.move_to(box)
        return VGroup(box, text)
