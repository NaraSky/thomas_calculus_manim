from manim import *


class Scene6_ReadValuesFromGraph(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    GRAPH_COLOR = BLUE
    GUIDE_COLOR = GREY_B
    POINT_COLOR = BLUE

    def construct(self):
        self.setup_layout()
        self.step1_create_graph()
        self.step2_place_input_marker()
        self.step3_draw_vertical_guide()
        self.step4_highlight_graph_point()
        self.step5_draw_output_guide()
        self.step6_label_output_value()
        self.step7_move_input_marker()
        self.step8_transform_vertical_guide()
        self.step9_transform_point_and_output()
        self.step10_emphasize_one_height()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.x_first = 1
        self.x_second = 2
        self.create_axes()
        self.create_graph()
        self.create_first_reading()
        self.create_second_reading()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-0.5, 3.5, 1],
            y_range=[0, 4.5, 1],
            x_length=8.0,
            y_length=4.8,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([0, -0.25, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.75)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.75)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_graph(self):
        graph_points = [self.axes.c2p(x / 20, self.func(x / 20)) for x in range(0, 64)]
        self.graph_curve = VMobject(color=self.GRAPH_COLOR, stroke_width=4)
        self.graph_curve.set_points_smoothly(graph_points)
        self.graph_label = MathTex("y=f(x)", color=WHITE).scale(0.8)
        self.graph_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.graph_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.graph_label.move_to([0, 3.15, 0])

    def create_first_reading(self):
        self.input_dot = Dot(self.x_axis_point(self.x_first), color=self.INPUT_COLOR, radius=0.07)
        self.input_label = MathTex("x=1", color=self.INPUT_COLOR).scale(0.7)
        self.input_label.next_to(self.input_dot, DOWN, buff=0.2)

        self.vertical_guide = self.make_vertical_guide(self.x_first)
        self.graph_point = Dot(self.graph_point_at(self.x_first), color=self.POINT_COLOR, radius=0.08)
        self.point_label = MathTex("(1,f(1))", color=WHITE).scale(0.62)
        self.point_label.next_to(self.graph_point, UP + RIGHT, buff=0.12)

        self.horizontal_guide = self.make_horizontal_guide(self.x_first)
        self.output_dot = Dot(self.y_axis_point(self.x_first), color=self.OUTPUT_COLOR, radius=0.07)
        self.output_label = MathTex("f(1)", color=self.OUTPUT_COLOR).scale(0.7)
        self.output_label.next_to(self.output_dot, LEFT, buff=0.18)

    def create_second_reading(self):
        self.next_input_dot = Dot(self.x_axis_point(self.x_second), color=self.INPUT_COLOR, radius=0.07)
        self.next_input_label = MathTex("x=2", color=self.INPUT_COLOR).scale(0.7)
        self.next_input_label.next_to(self.next_input_dot, DOWN, buff=0.2)

        self.next_vertical_guide = self.make_vertical_guide(self.x_second)
        self.next_graph_point = Dot(self.graph_point_at(self.x_second), color=self.POINT_COLOR, radius=0.08)
        self.next_point_label = MathTex("(2,f(2))", color=WHITE).scale(0.62)
        self.next_point_label.next_to(self.next_graph_point, UP + RIGHT, buff=0.12)

        self.next_horizontal_guide = self.make_horizontal_guide(self.x_second)
        self.next_output_dot = Dot(self.y_axis_point(self.x_second), color=self.OUTPUT_COLOR, radius=0.07)
        self.next_output_label = MathTex("f(2)", color=self.OUTPUT_COLOR).scale(0.7)
        self.next_output_label.next_to(self.next_output_dot, LEFT, buff=0.18)

    def create_summary(self):
        self.summary = MathTex(
            r"\text{choose }x",
            r"\longrightarrow",
            r"\text{read one height }f(x)",
            color=WHITE,
        )
        self.summary.set_color_by_tex("x", self.INPUT_COLOR)
        self.summary.set_color_by_tex("f(x)", self.OUTPUT_COLOR)
        self.summary.scale(0.68)
        self.summary.to_edge(DOWN, buff=0.35)

    def step1_create_graph(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()
        self.play(Create(self.graph_curve), Write(self.graph_label), run_time=2)
        self.wait()

    def step2_place_input_marker(self):
        self.play(FadeIn(VGroup(self.input_dot, self.input_label)), run_time=2)
        self.wait()

    def step3_draw_vertical_guide(self):
        self.play(Create(self.vertical_guide), run_time=2)
        self.wait()

    def step4_highlight_graph_point(self):
        self.play(FadeIn(self.graph_point), Write(self.point_label), run_time=2)
        self.wait()

    def step5_draw_output_guide(self):
        self.play(Create(self.horizontal_guide), FadeIn(self.output_dot), run_time=2)
        self.wait()

    def step6_label_output_value(self):
        self.play(Write(self.output_label), run_time=2)
        self.wait()

    def step7_move_input_marker(self):
        self.play(
            Transform(self.input_dot, self.next_input_dot),
            Transform(self.input_label, self.next_input_label),
            run_time=2,
        )
        self.wait()

    def step8_transform_vertical_guide(self):
        self.play(Transform(self.vertical_guide, self.next_vertical_guide), run_time=2)
        self.wait()

    def step9_transform_point_and_output(self):
        self.play(
            Transform(self.graph_point, self.next_graph_point),
            Transform(self.point_label, self.next_point_label),
            Transform(self.horizontal_guide, self.next_horizontal_guide),
            Transform(self.output_dot, self.next_output_dot),
            Transform(self.output_label, self.next_output_label),
            run_time=3,
        )
        self.wait()

    def step10_emphasize_one_height(self):
        self.play(
            Write(self.summary),
            Indicate(VGroup(self.vertical_guide, self.graph_point, self.output_label), color=self.OUTPUT_COLOR),
            run_time=2,
        )
        self.wait()

    def func(self, x):
        return 0.45 * (x - 0.25) ** 2 + 0.45

    def graph_point_at(self, x_value):
        return self.axes.c2p(x_value, self.func(x_value))

    def x_axis_point(self, x_value):
        return self.axes.c2p(x_value, 0)

    def y_axis_point(self, x_value):
        return self.axes.c2p(0, self.func(x_value))

    def make_vertical_guide(self, x_value):
        return DashedLine(
            self.x_axis_point(x_value),
            self.graph_point_at(x_value),
            color=self.GUIDE_COLOR,
            dash_length=0.12,
            stroke_width=3,
        )

    def make_horizontal_guide(self, x_value):
        return DashedLine(
            self.graph_point_at(x_value),
            self.y_axis_point(x_value),
            color=self.OUTPUT_COLOR,
            dash_length=0.12,
            stroke_width=3,
        )
