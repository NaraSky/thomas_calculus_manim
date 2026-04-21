from manim import *


class Scene31_NumericalTableToScatterplot(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    POINT_COLOR = BLUE
    CURVE_COLOR = TEAL
    GUIDE_COLOR = GREY_B
    HIGHLIGHT_COLOR = YELLOW

    def construct(self):
        self.setup_layout()
        self.step1_show_title()
        self.step2_create_table()
        self.step3_create_axes()
        self.step4_highlight_first_row()
        self.step5_plot_first_point()
        self.step6_highlight_more_rows()
        self.step7_plot_remaining_points()
        self.step8_trace_suggested_curve()
        self.step9_write_scatterplot_label()
        self.step10_summarize_numerical_representation()

    def setup_layout(self):
        self.camera.background_color = BLACK
        self.data = [
            (0.9, -0.08),
            (1.3, 0.48),
            (1.8, 0.84),
            (2.7, -0.14),
            (3.6, 0.22),
            (4.2, 0.81),
            (5.1, 0.08),
            (5.6, -0.35),
        ]
        self.create_title()
        self.create_table()
        self.create_axes()
        self.create_points()
        self.create_summary()

    def create_title(self):
        self.title = MathTex(r"\text{a table can represent a function}", color=WHITE).scale(0.7)
        self.title.to_edge(UP, buff=0.42)

    def create_table(self):
        self.table_header = VGroup(
            self.make_cell("t", self.INPUT_COLOR, width=0.82),
            self.make_cell("p", self.OUTPUT_COLOR, width=0.82),
        )
        self.table_header.arrange(RIGHT, buff=0.06)

        self.table_rows = VGroup()
        for time, pressure in self.data:
            row = VGroup(
                self.make_cell(f"{time:.1f}", self.INPUT_COLOR, width=0.82, scale=0.38),
                self.make_cell(f"{pressure:.2f}", self.OUTPUT_COLOR, width=0.82, scale=0.38),
            )
            row.arrange(RIGHT, buff=0.06)
            self.table_rows.add(row)

        self.table = VGroup(self.table_header, self.table_rows)
        self.table_rows.arrange(DOWN, buff=0.06)
        self.table.arrange(DOWN, buff=0.08)
        self.table.move_to([-4.15, -0.1, 0])

        self.first_row_highlight = SurroundingRectangle(
            self.table_rows[0],
            color=self.HIGHLIGHT_COLOR,
            buff=0.06,
            stroke_width=2.5,
        )
        self.more_rows_highlight = SurroundingRectangle(
            VGroup(*self.table_rows[1:]),
            color=self.HIGHLIGHT_COLOR,
            buff=0.07,
            stroke_width=2.5,
        )

    def create_axes(self):
        self.axes = Axes(
            x_range=[0, 6.2, 1],
            y_range=[-0.8, 1.05, 0.5],
            x_length=6.2,
            y_length=3.85,
            axis_config={
                "color": self.GUIDE_COLOR,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([1.35, -0.12, 0])

        self.x_label = MathTex("t", color=self.INPUT_COLOR).scale(0.6)
        self.y_label = MathTex("p", color=self.OUTPUT_COLOR).scale(0.6)
        self.x_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.08)
        self.y_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.08)
        self.axis_labels = VGroup(self.x_label, self.y_label)

        self.point_formula = MathTex("(t,", "p", ")", color=WHITE).scale(0.58)
        self.point_formula.set_color_by_tex("t", self.INPUT_COLOR)
        self.point_formula.set_color_by_tex("p", self.OUTPUT_COLOR)
        self.point_formula.move_to([4.6, 1.95, 0])

        self.scatterplot_label = MathTex(r"\text{scatterplot}", color=self.POINT_COLOR).scale(0.58)
        self.scatterplot_label.move_to([4.55, -2.25, 0])

    def create_points(self):
        self.points = VGroup()
        for time, pressure in self.data:
            self.points.add(Dot(self.axes.c2p(time, pressure), radius=0.065, color=self.POINT_COLOR))

        self.first_point_guide_x = DashedLine(
            self.axes.c2p(self.data[0][0], 0),
            self.axes.c2p(self.data[0][0], self.data[0][1]),
            color=self.INPUT_COLOR,
            stroke_width=2,
            dash_length=0.08,
        )
        self.first_point_guide_y = DashedLine(
            self.axes.c2p(0, self.data[0][1]),
            self.axes.c2p(self.data[0][0], self.data[0][1]),
            color=self.OUTPUT_COLOR,
            stroke_width=2,
            dash_length=0.08,
        )

        self.suggested_curve = self.make_smooth_curve()

    def create_summary(self):
        self.summary_cards = VGroup(
            self.make_card("input column", self.INPUT_COLOR, width=1.45),
            self.make_card("output column", self.OUTPUT_COLOR, width=1.5),
            self.make_card("point cloud", self.POINT_COLOR, width=1.32),
            self.make_card("possible graph", self.CURVE_COLOR, width=1.6),
        )
        self.summary_cards.arrange(RIGHT, buff=0.16)
        self.summary_cards.to_edge(DOWN, buff=0.32)

    def step1_show_title(self):
        self.play(Write(self.title), run_time=1.5)
        self.wait(0.5)

    def step2_create_table(self):
        self.play(FadeIn(self.table_header), run_time=1.2)
        self.wait(0.35)
        self.play(FadeIn(self.table_rows), run_time=1.8)
        self.wait(0.5)

    def step3_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait(0.5)

    def step4_highlight_first_row(self):
        self.play(Create(self.first_row_highlight), run_time=1.2)
        self.wait(0.45)

    def step5_plot_first_point(self):
        self.play(Create(self.first_point_guide_x), run_time=0.9)
        self.wait(0.25)
        self.play(Create(self.first_point_guide_y), run_time=0.9)
        self.wait(0.25)
        self.play(FadeIn(self.points[0]), Write(self.point_formula), run_time=1.4)
        self.wait(0.5)

    def step6_highlight_more_rows(self):
        self.play(ReplacementTransform(self.first_row_highlight, self.more_rows_highlight), run_time=1.2)
        self.wait(0.45)

    def step7_plot_remaining_points(self):
        self.play(LaggedStart(*[FadeIn(point) for point in self.points[1:]], lag_ratio=0.18), run_time=2.2)
        self.wait(0.5)

    def step8_trace_suggested_curve(self):
        self.play(Create(self.suggested_curve), run_time=2.5)
        self.wait(0.5)

    def step9_write_scatterplot_label(self):
        self.play(Write(self.scatterplot_label), run_time=1.2)
        self.wait(0.45)

    def step10_summarize_numerical_representation(self):
        self.play(FadeOut(self.more_rows_highlight), FadeIn(self.summary_cards), run_time=1.5)
        self.wait(0.5)

    def make_smooth_curve(self):
        graph = VMobject(color=self.CURVE_COLOR, stroke_width=3.5)
        points = [self.axes.c2p(time, pressure) for time, pressure in self.data]
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_cell(self, label, color, width=0.82, height=0.34, scale=0.44):
        box = Rectangle(
            width=width,
            height=height,
            stroke_color=color,
            stroke_width=1.8,
            fill_color=color,
            fill_opacity=0.08,
        )
        text = MathTex(label, color=color).scale(scale)
        text.move_to(box)
        return VGroup(box, text)

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
        text = MathTex(r"\text{" + label + "}", color=color).scale(0.4)
        text.move_to(box)
        return VGroup(box, text)
