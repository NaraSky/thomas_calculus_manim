from manim import *


class Scene19_TrigonometricFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    CURVE_COLOR = TEAL
    COS_COLOR = BLUE
    PERIOD_COLOR = RED
    GUIDE_COLOR = GREY_B

    def construct(self):
        self.setup_layout()
        self.step1_create_reference_frames()
        self.step2_show_angle_input()
        self.step3_show_height_output()
        self.step4_write_sine_formula()
        self.step5_draw_sine_wave()
        self.step6_mark_period()
        self.step7_transform_to_cosine()
        self.step8_summarize_trig_functions()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.theta = PI / 3
        self.circle_center = LEFT * 3.75 + UP * 0.5
        self.circle_radius = 1.15

        self.create_unit_circle()
        self.create_graph_axes()
        self.create_angle_objects()
        self.create_height_objects()
        self.create_formulas()
        self.create_graphs()
        self.create_period_marker()
        self.create_summary()

    def create_unit_circle(self):
        self.circle = Circle(radius=self.circle_radius, color=GREY_B, stroke_width=2)
        self.circle.move_to(self.circle_center)

        self.circle_x_axis = Line(
            self.circle_center + LEFT * 1.45,
            self.circle_center + RIGHT * 1.45,
            color=GREY_B,
            stroke_width=2,
        )
        self.circle_y_axis = Line(
            self.circle_center + DOWN * 1.45,
            self.circle_center + UP * 1.45,
            color=GREY_B,
            stroke_width=2,
        )
        self.circle_axes = VGroup(self.circle_x_axis, self.circle_y_axis)

    def create_graph_axes(self):
        self.axes = Axes(
            x_range=[-PI, 3 * PI, PI],
            y_range=[-1.4, 1.4, 1],
            x_length=7.0,
            y_length=3.8,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([1.45, -0.3, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.6)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.6)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.1)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.1)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

        self.pi_labels = VGroup(
            self.make_x_label(-PI, "-\\pi"),
            self.make_x_label(PI, "\\pi"),
            self.make_x_label(2 * PI, "2\\pi"),
            self.make_x_label(3 * PI, "3\\pi"),
        )

    def create_angle_objects(self):
        endpoint = self.circle_point(self.theta)
        self.radius_line = Line(self.circle_center, endpoint, color=self.INPUT_COLOR, stroke_width=4)
        self.angle_arc = Arc(
            radius=0.42,
            start_angle=0,
            angle=self.theta,
            arc_center=self.circle_center,
            color=self.INPUT_COLOR,
            stroke_width=4,
        )
        self.angle_label = MathTex("\\theta", color=self.INPUT_COLOR).scale(0.65)
        self.angle_label.move_to(self.circle_center + RIGHT * 0.62 + UP * 0.27)
        self.circle_dot = Dot(endpoint, radius=0.08, color=self.INPUT_COLOR)

    def create_height_objects(self):
        endpoint = self.circle_point(self.theta)
        projection = self.circle_center + UP * (self.circle_radius * np.sin(self.theta))

        self.height_line = Line(self.circle_center, projection, color=self.OUTPUT_COLOR, stroke_width=5)
        self.projection_line = DashedLine(endpoint, projection, color=self.GUIDE_COLOR, stroke_width=2, dash_length=0.12)
        self.projection_dot = Dot(projection, radius=0.07, color=self.OUTPUT_COLOR)
        self.height_label = MathTex("y", "=", "\\sin", "\\theta", color=WHITE).scale(0.58)
        self.height_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.height_label.set_color_by_tex("\\theta", self.INPUT_COLOR)
        self.height_label.next_to(self.height_line, LEFT, buff=0.14)

    def create_formulas(self):
        self.sine_formula = MathTex("f(\\theta)", "=", "\\sin", "\\theta", color=WHITE).scale(0.76)
        self.sine_formula.set_color_by_tex("\\theta", self.INPUT_COLOR)
        self.sine_formula.set_color_by_tex("\\sin", self.CURVE_COLOR)
        self.sine_formula.move_to([1.45, 2.55, 0])

        self.cosine_formula = MathTex("f(\\theta)", "=", "\\cos", "\\theta", color=WHITE).scale(0.76)
        self.cosine_formula.set_color_by_tex("\\theta", self.INPUT_COLOR)
        self.cosine_formula.set_color_by_tex("\\cos", self.COS_COLOR)
        self.cosine_formula.move_to(self.sine_formula)

    def create_graphs(self):
        self.sine_graph = self.make_graph(lambda x: np.sin(x), -PI, 3 * PI, self.CURVE_COLOR)
        self.cosine_graph = self.make_graph(lambda x: np.cos(x), -PI, 3 * PI, self.COS_COLOR)
        self.final_sine_graph = self.make_graph(lambda x: np.sin(x), -PI, 3 * PI, self.CURVE_COLOR)

        self.graph_dot = Dot(self.axes.c2p(self.theta, np.sin(self.theta)), radius=0.075, color=self.INPUT_COLOR)
        self.graph_guide = DashedLine(
            self.axes.c2p(self.theta, 0),
            self.axes.c2p(self.theta, np.sin(self.theta)),
            color=self.GUIDE_COLOR,
            stroke_width=2,
            dash_length=0.12,
        )

        self.cos_start_dot = Dot(self.axes.c2p(0, 1), radius=0.08, color=self.COS_COLOR)
        self.cos_start_label = MathTex("\\cos 0", "=", "1", color=WHITE).scale(0.52)
        self.cos_start_label.set_color_by_tex("\\cos", self.COS_COLOR)
        self.cos_start_label.next_to(self.cos_start_dot, UP, buff=0.12)

    def create_period_marker(self):
        y = -1.18
        self.period_arrow = DoubleArrow(
            self.axes.c2p(0, y),
            self.axes.c2p(2 * PI, y),
            color=self.PERIOD_COLOR,
            stroke_width=3,
            buff=0,
            max_tip_length_to_length_ratio=0.06,
        )
        self.period_label = MathTex("2\\pi", color=self.PERIOD_COLOR).scale(0.6)
        self.period_label.next_to(self.period_arrow, DOWN, buff=0.08)

        self.zero_dots = VGroup(
            Dot(self.axes.c2p(0, 0), radius=0.055, color=self.PERIOD_COLOR),
            Dot(self.axes.c2p(PI, 0), radius=0.055, color=self.PERIOD_COLOR),
            Dot(self.axes.c2p(2 * PI, 0), radius=0.055, color=self.PERIOD_COLOR),
        )

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("angle", self.INPUT_COLOR, width=1.2),
            self.make_summary_card("wave", self.OUTPUT_COLOR, width=1.2),
            self.make_summary_card("period", self.PERIOD_COLOR, width=1.2),
        )
        self.summary.arrange(RIGHT, buff=0.18)
        self.summary.to_edge(DOWN, buff=0.34)

        self.final_statement = Text("trig functions repeat", font_size=25, color=WHITE)
        self.final_statement.move_to([1.45, 2.35, 0])

    def step1_create_reference_frames(self):
        self.play(
            Create(self.circle),
            Create(self.circle_axes),
            Create(self.axes),
            FadeIn(self.axis_labels),
            FadeIn(self.pi_labels),
            run_time=2,
        )
        self.wait()

    def step2_show_angle_input(self):
        self.play(Create(self.radius_line), Create(self.angle_arc), Write(self.angle_label), FadeIn(self.circle_dot), run_time=2)
        self.wait()

    def step3_show_height_output(self):
        self.play(
            Create(self.height_line),
            Create(self.projection_line),
            FadeIn(self.projection_dot),
            Write(self.height_label),
            run_time=2,
        )
        self.wait()

    def step4_write_sine_formula(self):
        self.play(Write(self.sine_formula), run_time=2)
        self.wait()

    def step5_draw_sine_wave(self):
        self.play(Create(self.sine_graph), Create(self.graph_guide), FadeIn(self.graph_dot), run_time=3)
        self.wait()

    def step6_mark_period(self):
        self.play(Create(self.period_arrow), Write(self.period_label), FadeIn(self.zero_dots), run_time=2)
        self.wait()

    def step7_transform_to_cosine(self):
        self.play(
            ReplacementTransform(self.sine_formula, self.cosine_formula),
            ReplacementTransform(self.sine_graph, self.cosine_graph),
            FadeOut(self.height_line),
            FadeOut(self.projection_line),
            FadeOut(self.projection_dot),
            FadeOut(self.height_label),
            FadeOut(self.graph_guide),
            FadeOut(self.graph_dot),
            FadeIn(self.cos_start_dot),
            Write(self.cos_start_label),
            run_time=3,
        )
        self.wait()

    def step8_summarize_trig_functions(self):
        self.play(
            ReplacementTransform(self.cosine_graph, self.final_sine_graph),
            FadeOut(self.cos_start_dot),
            FadeOut(self.cos_start_label),
            FadeIn(self.height_line),
            FadeIn(self.projection_line),
            FadeIn(self.projection_dot),
            FadeIn(self.height_label),
            FadeIn(self.graph_guide),
            FadeIn(self.graph_dot),
            ReplacementTransform(self.cosine_formula, self.final_statement),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def circle_point(self, theta):
        return self.circle_center + self.circle_radius * (np.cos(theta) * RIGHT + np.sin(theta) * UP)

    def make_graph(self, function, x_start, x_end, color):
        points = []
        samples = 220
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=4)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_x_label(self, x, label):
        mark = MathTex(label, color=self.INPUT_COLOR).scale(0.42)
        mark.next_to(self.axes.c2p(x, 0), DOWN, buff=0.12)
        return mark

    def make_summary_card(self, label, color, width=1.55):
        box = RoundedRectangle(
            width=width,
            height=0.5,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.4,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(r"\text{" + label + "}", color=color).scale(0.48)
        text.move_to(box)
        return VGroup(box, text)
