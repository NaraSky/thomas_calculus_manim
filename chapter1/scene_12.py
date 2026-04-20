from manim import *


class Scene12_LinearFunctionsFamily(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    LINE_COLOR = BLUE
    SLOPE_COLOR = YELLOW
    INTERCEPT_COLOR = GREEN
    CONSTANT_COLOR = TEAL

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_write_general_form()
        self.step3_draw_identity_line()
        self.step4_change_slope_steeper()
        self.step5_change_slope_flatter()
        self.step6_change_slope_negative()
        self.step7_show_constant_function()
        self.step8_shift_intercept()
        self.step9_summarize_linear_family()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_lines()
        self.create_labels()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2.6, 2.8, 1],
            x_length=7.2,
            y_length=4.8,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.0, -0.15, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.72)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.72)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_lines(self):
        self.current_line = self.make_line(1, 0, self.LINE_COLOR)
        self.steeper_line = self.make_line(2, 0, self.LINE_COLOR)
        self.flatter_line = self.make_line(0.5, 0, self.LINE_COLOR)
        self.negative_line = self.make_line(-1, 0, self.LINE_COLOR)
        self.constant_line = self.make_line(0, 1.5, self.CONSTANT_COLOR)
        self.shifted_line = self.make_line(1, 1, self.LINE_COLOR)

        self.intercept_dot = Dot(self.axes.c2p(0, 1), radius=0.075, color=self.INTERCEPT_COLOR)
        self.constant_dot = Dot(self.axes.c2p(0, 1.5), radius=0.075, color=self.CONSTANT_COLOR)

    def create_labels(self):
        self.general_form = MathTex("f(x)", "=", "mx", "+", "b", color=WHITE)
        self.general_form.set_color_by_tex("x", self.INPUT_COLOR)
        self.general_form.set_color_by_tex("m", self.SLOPE_COLOR)
        self.general_form.set_color_by_tex("b", self.INTERCEPT_COLOR)
        self.general_form.move_to([3.95, 2.15, 0])

        self.identity_label = MathTex("f(x)=x", color=WHITE).scale(0.72)
        self.identity_label.move_to([3.95, 1.15, 0])

        self.steeper_label = MathTex("m=2", color=self.SLOPE_COLOR).scale(0.72)
        self.flatter_label = MathTex(r"m=\frac{1}{2}", color=self.SLOPE_COLOR).scale(0.72)
        self.negative_label = MathTex("m=-1", color=self.SLOPE_COLOR).scale(0.72)
        self.constant_label = MathTex(r"m=0,\ y=\frac{3}{2}", color=self.CONSTANT_COLOR).scale(0.68)
        self.shifted_label = MathTex("b=1", color=self.INTERCEPT_COLOR).scale(0.72)

        for label in [
            self.steeper_label,
            self.flatter_label,
            self.negative_label,
            self.constant_label,
            self.shifted_label,
        ]:
            label.move_to([3.95, 1.15, 0])

        self.slope_arrow = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(1, 1),
            color=self.SLOPE_COLOR,
            stroke_width=4,
            buff=0,
            max_tip_length_to_length_ratio=0.12,
        )
        self.slope_label = Text("slope", font_size=24, color=self.SLOPE_COLOR)
        self.slope_label.next_to(self.slope_arrow, UP + LEFT, buff=0.12)

        self.intercept_label = Text("intercept", font_size=24, color=self.INTERCEPT_COLOR)
        self.intercept_label.next_to(self.intercept_dot, RIGHT, buff=0.14)

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("straight line", self.LINE_COLOR),
            self.make_summary_card("slope m", self.SLOPE_COLOR),
            self.make_summary_card("intercept b", self.INTERCEPT_COLOR),
        )
        self.summary.arrange(RIGHT, buff=0.25)
        self.summary.to_edge(DOWN, buff=0.32)

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_write_general_form(self):
        self.play(Write(self.general_form), run_time=2)
        self.wait()

    def step3_draw_identity_line(self):
        self.play(Create(self.current_line), Write(self.identity_label), run_time=2)
        self.wait()

    def step4_change_slope_steeper(self):
        self.play(
            Transform(self.current_line, self.steeper_line),
            ReplacementTransform(self.identity_label, self.steeper_label),
            Transform(self.slope_arrow, Arrow(
                self.axes.c2p(0, 0),
                self.axes.c2p(0.75, 1.5),
                color=self.SLOPE_COLOR,
                stroke_width=4,
                buff=0,
                max_tip_length_to_length_ratio=0.12,
            )),
            FadeIn(self.slope_label),
            run_time=2,
        )
        self.wait()

    def step5_change_slope_flatter(self):
        self.play(
            Transform(self.current_line, self.flatter_line),
            ReplacementTransform(self.steeper_label, self.flatter_label),
            Transform(self.slope_arrow, Arrow(
                self.axes.c2p(0, 0),
                self.axes.c2p(1.5, 0.75),
                color=self.SLOPE_COLOR,
                stroke_width=4,
                buff=0,
                max_tip_length_to_length_ratio=0.12,
            )),
            run_time=2,
        )
        self.wait()

    def step6_change_slope_negative(self):
        self.play(
            Transform(self.current_line, self.negative_line),
            ReplacementTransform(self.flatter_label, self.negative_label),
            Transform(self.slope_arrow, Arrow(
                self.axes.c2p(0, 0),
                self.axes.c2p(1, -1),
                color=self.SLOPE_COLOR,
                stroke_width=4,
                buff=0,
                max_tip_length_to_length_ratio=0.12,
            )),
            run_time=2,
        )
        self.wait()

    def step7_show_constant_function(self):
        self.play(
            Transform(self.current_line, self.constant_line),
            ReplacementTransform(self.negative_label, self.constant_label),
            FadeOut(VGroup(self.slope_arrow, self.slope_label)),
            FadeIn(self.constant_dot),
            run_time=2,
        )
        self.wait()

    def step8_shift_intercept(self):
        self.play(
            Transform(self.current_line, self.shifted_line),
            ReplacementTransform(self.constant_label, self.shifted_label),
            ReplacementTransform(self.constant_dot, self.intercept_dot),
            Write(self.intercept_label),
            run_time=2,
        )
        self.wait()

    def step9_summarize_linear_family(self):
        self.play(FadeIn(self.summary), Indicate(self.general_form, color=self.LINE_COLOR), run_time=2)
        self.wait()

    def make_line(self, slope, intercept, color):
        points = []
        for i in range(121):
            x = -3 + i * 0.05
            y = slope * x + intercept
            if -2.55 <= y <= 2.7:
                points.append(self.axes.c2p(x, y))
        line = VMobject(color=color, stroke_width=5)
        line.set_points_as_corners(points)
        return line

    def make_summary_card(self, label, color):
        box = RoundedRectangle(
            width=1.8,
            height=0.48,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.5,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = Text(label, font_size=21, color=color)
        text.move_to(box)
        return VGroup(box, text)
