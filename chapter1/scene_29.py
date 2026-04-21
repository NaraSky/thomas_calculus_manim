from manim import *


class Scene29_CompositeFunctionPipeline(Scene):
    INPUT_COLOR = YELLOW
    G_COLOR = GREEN
    F_COLOR = TEAL
    RESULT_COLOR = BLUE
    GUIDE_COLOR = GREY_B

    def construct(self):
        self.setup_layout()
        self.step1_create_input()
        self.step2_send_input_to_g()
        self.step3_show_g_output()
        self.step4_mark_g_output_as_next_input()
        self.step5_feed_g_output_to_f()
        self.step6_show_final_output()
        self.step7_highlight_final_output()
        self.step8_write_operation_label()
        self.step9_write_composition_notation()
        self.step10_show_reading_order()
        self.step11_summarize_pipeline()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.create_pipeline_objects()
        self.create_formula_objects()
        self.create_summary_objects()

    def create_pipeline_objects(self):
        self.input_value = self.make_value_box("x", self.INPUT_COLOR)
        self.input_value.move_to([-5.0, 0.72, 0])

        self.g_machine = self.make_machine("g", self.G_COLOR)
        self.g_machine.move_to([-2.55, 0.72, 0])

        self.middle_value = self.make_value_box("g(x)", self.G_COLOR, width=1.35)
        self.middle_value.move_to([-0.1, 0.72, 0])

        self.f_machine = self.make_machine("f", self.F_COLOR)
        self.f_machine.move_to([2.35, 0.72, 0])

        self.final_value = self.make_value_box("f(g(x))", self.RESULT_COLOR, width=1.64, text_scale=0.56)
        self.final_value.move_to([4.95, 0.72, 0])

        self.arrow_x_to_g = self.make_arrow(self.input_value, self.g_machine, self.INPUT_COLOR)
        self.arrow_g_to_middle = self.make_arrow(self.g_machine, self.middle_value, self.G_COLOR)
        self.arrow_middle_to_f = self.make_arrow(self.middle_value, self.f_machine, self.G_COLOR)
        self.arrow_f_to_result = self.make_arrow(self.f_machine, self.final_value, self.RESULT_COLOR)

        self.inner_input_highlight = SurroundingRectangle(
            self.middle_value,
            color=self.INPUT_COLOR,
            buff=0.08,
            stroke_width=3,
        )
        self.final_highlight = SurroundingRectangle(
            self.final_value,
            color=self.RESULT_COLOR,
            buff=0.08,
            stroke_width=3,
        )

    def create_formula_objects(self):
        self.operation_label = MathTex(r"\text{output of }g\text{ becomes input of }f", color=WHITE).scale(0.6)
        self.operation_label.set_opacity(0.92)
        self.operation_label.move_to([0, -0.58, 0])

        self.composition_formula = MathTex(
            "(f\\circ g)(x)",
            "=",
            "f(g(x))",
            color=WHITE,
        ).scale(0.74)
        self.composition_formula.set_color_by_tex("g", self.G_COLOR)
        self.composition_formula.set_color_by_tex("f", self.F_COLOR)
        self.composition_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.composition_formula.move_to([0, -1.45, 0])

        self.order_note = MathTex(r"\text{read from inside out}", color=self.GUIDE_COLOR).scale(0.5)
        self.order_note.next_to(self.composition_formula, DOWN, buff=0.24)

    def create_summary_objects(self):
        self.summary_cards = VGroup(
            self.make_card("start with x", self.INPUT_COLOR, width=1.34),
            self.make_card("apply g", self.G_COLOR, width=1.08),
            self.make_card("then f", self.F_COLOR, width=1.08),
            self.make_card("output", self.RESULT_COLOR, width=1.08),
        )
        self.summary_cards.arrange(RIGHT, buff=0.14)
        self.summary_cards.scale(0.9)
        self.summary_cards.to_edge(DOWN, buff=0.34)

    def step1_create_input(self):
        self.play(FadeIn(self.input_value), run_time=2)
        self.wait()

    def step2_send_input_to_g(self):
        self.play(Create(self.arrow_x_to_g), FadeIn(self.g_machine), run_time=2)
        self.wait()

    def step3_show_g_output(self):
        self.play(Create(self.arrow_g_to_middle), FadeIn(self.middle_value), run_time=2)
        self.wait()

    def step4_mark_g_output_as_next_input(self):
        self.play(Create(self.inner_input_highlight), run_time=2)
        self.wait()

    def step5_feed_g_output_to_f(self):
        self.play(Create(self.arrow_middle_to_f), FadeIn(self.f_machine), run_time=2)
        self.wait()

    def step6_show_final_output(self):
        self.play(Create(self.arrow_f_to_result), FadeIn(self.final_value), run_time=2)
        self.wait()

    def step7_highlight_final_output(self):
        self.play(ReplacementTransform(self.inner_input_highlight, self.final_highlight), run_time=2)
        self.wait()

    def step8_write_operation_label(self):
        self.play(Write(self.operation_label), run_time=2)
        self.wait()

    def step9_write_composition_notation(self):
        self.play(Write(self.composition_formula), run_time=2)
        self.wait()

    def step10_show_reading_order(self):
        self.play(Write(self.order_note), run_time=2)
        self.wait()

    def step11_summarize_pipeline(self):
        self.play(FadeIn(self.summary_cards), run_time=1.5)
        self.wait()

    def make_machine(self, label, color):
        box = RoundedRectangle(
            width=1.25,
            height=0.82,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.14,
        )
        text = MathTex(label, color=color).scale(0.78)
        text.move_to(box)
        return VGroup(box, text)

    def make_value_box(self, label, color, width=1.1, text_scale=0.62):
        box = RoundedRectangle(
            width=width,
            height=0.62,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.6,
            fill_color=color,
            fill_opacity=0.1,
        )
        text = MathTex(label, color=color).scale(text_scale)
        text.move_to(box)
        return VGroup(box, text)

    def make_arrow(self, left_object, right_object, color):
        return Arrow(
            left_object.get_right(),
            right_object.get_left(),
            buff=0.18,
            color=color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.16,
        )

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
