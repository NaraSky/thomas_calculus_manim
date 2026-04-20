from manim import *


class Scene13_PowerFunctionsPositiveIntegers(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    ODD_COLOR = BLUE
    EVEN_COLOR = GREEN
    HIGHLIGHT_COLOR = YELLOW
    STEEP_COLOR = RED

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_write_power_form()
        self.step3_draw_identity_power()
        self.step4_draw_quadratic_power()
        self.step5_draw_cubic_power()
        self.step6_draw_fourth_and_fifth_powers()
        self.step7_mark_shared_points()
        self.step8_highlight_even_powers()
        self.step9_highlight_odd_powers()
        self.step10_show_flattening_near_origin()
        self.step11_summarize_power_family()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_power_graphs()
        self.create_labels()
        self.create_shared_points()
        self.create_flattening_marker()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-1.35, 1.35, 0.5],
            y_range=[-1.25, 1.35, 0.5],
            x_length=6.3,
            y_length=5.0,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.0, -0.1, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.7)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.7)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_power_graphs(self):
        self.power_graphs = {
            1: self.make_power_graph(1, BLUE),
            2: self.make_power_graph(2, GREEN),
            3: self.make_power_graph(3, TEAL),
            4: self.make_power_graph(4, YELLOW),
            5: self.make_power_graph(5, RED),
        }
        self.odd_graphs = VGroup(self.power_graphs[1], self.power_graphs[3], self.power_graphs[5])
        self.even_graphs = VGroup(self.power_graphs[2], self.power_graphs[4])

    def create_labels(self):
        self.power_form = MathTex("f(x)", "=", "x^n", color=WHITE)
        self.power_form.set_color_by_tex("x", self.INPUT_COLOR)
        self.power_form.set_color_by_tex("n", self.HIGHLIGHT_COLOR)
        self.power_form.move_to([3.75, 2.25, 0])

        self.labels = {
            1: self.make_power_label("x", BLUE, [3.75, 1.45, 0]),
            2: self.make_power_label("x^2", GREEN, [3.75, 1.0, 0]),
            3: self.make_power_label("x^3", TEAL, [3.75, 0.55, 0]),
            4: self.make_power_label("x^4", YELLOW, [3.75, 0.1, 0]),
            5: self.make_power_label("x^5", RED, [3.75, -0.35, 0]),
        }

        self.even_rule = Text("even powers: y-axis symmetry", font_size=26, color=self.EVEN_COLOR)
        self.odd_rule = Text("odd powers: origin symmetry", font_size=26, color=self.ODD_COLOR)
        self.flat_rule = Text("larger n: flatter near 0", font_size=26, color=self.HIGHLIGHT_COLOR)
        for rule in [self.even_rule, self.odd_rule, self.flat_rule]:
            rule.move_to([3.85, -1.25, 0])

    def create_shared_points(self):
        self.origin_dot = Dot(self.axes.c2p(0, 0), radius=0.08, color=self.HIGHLIGHT_COLOR)
        self.one_one_dot = Dot(self.axes.c2p(1, 1), radius=0.08, color=self.HIGHLIGHT_COLOR)
        self.origin_label = MathTex("(0,0)", color=self.HIGHLIGHT_COLOR).scale(0.55)
        self.one_one_label = MathTex("(1,1)", color=self.HIGHLIGHT_COLOR).scale(0.55)
        self.origin_label.next_to(self.origin_dot, DOWN + LEFT, buff=0.22)
        self.one_one_label.next_to(self.one_one_dot, UP + RIGHT, buff=0.1)
        self.shared_points = VGroup(self.origin_dot, self.one_one_dot, self.origin_label, self.one_one_label)

    def create_flattening_marker(self):
        self.flat_window = Rectangle(
            width=1.4,
            height=0.6,
            color=self.HIGHLIGHT_COLOR,
            stroke_width=3,
        )
        self.flat_window.move_to(self.axes.c2p(0, 0.05))
        self.flattening_marker = VGroup(self.flat_window)

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("pass (0,0)", self.HIGHLIGHT_COLOR),
            self.make_summary_card("pass (1,1)", self.HIGHLIGHT_COLOR),
            self.make_summary_card("parity symmetry", BLUE, width=2.05),
        )
        self.summary.arrange(RIGHT, buff=0.22)
        self.summary.to_edge(DOWN, buff=0.3)

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_write_power_form(self):
        self.play(Write(self.power_form), run_time=2)
        self.wait()

    def step3_draw_identity_power(self):
        self.play(Create(self.power_graphs[1]), Write(self.labels[1]), run_time=2)
        self.wait()

    def step4_draw_quadratic_power(self):
        self.play(Create(self.power_graphs[2]), Write(self.labels[2]), run_time=2)
        self.wait()

    def step5_draw_cubic_power(self):
        self.play(Create(self.power_graphs[3]), Write(self.labels[3]), run_time=2)
        self.wait()

    def step6_draw_fourth_and_fifth_powers(self):
        self.play(
            Create(self.power_graphs[4]),
            Write(self.labels[4]),
            Create(self.power_graphs[5]),
            Write(self.labels[5]),
            run_time=3,
        )
        self.wait()

    def step7_mark_shared_points(self):
        self.play(FadeIn(self.shared_points), run_time=2)
        self.wait()

    def step8_highlight_even_powers(self):
        self.play(
            self.odd_graphs.animate.set_stroke(opacity=0.22),
            self.even_graphs.animate.set_stroke(width=6, opacity=1),
            Write(self.even_rule),
            run_time=2,
        )
        self.wait()

    def step9_highlight_odd_powers(self):
        self.play(
            self.even_graphs.animate.set_stroke(width=4, opacity=0.22),
            self.odd_graphs.animate.set_stroke(width=6, opacity=1),
            ReplacementTransform(self.even_rule, self.odd_rule),
            run_time=2,
        )
        self.wait()

    def step10_show_flattening_near_origin(self):
        self.play(
            self.even_graphs.animate.set_stroke(width=4, opacity=1),
            self.odd_graphs.animate.set_stroke(width=4, opacity=1),
            VGroup(self.power_graphs[3], self.power_graphs[4], self.power_graphs[5]).animate.set_stroke(width=6, opacity=1),
            ReplacementTransform(self.odd_rule, self.flat_rule),
            Create(self.flattening_marker),
            run_time=2,
        )
        self.wait()

    def step11_summarize_power_family(self):
        self.play(
            VGroup(self.power_graphs[3], self.power_graphs[4], self.power_graphs[5]).animate.set_stroke(width=4, opacity=1),
            FadeOut(self.flattening_marker),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def make_power_graph(self, power, color):
        points = []
        for i in range(121):
            x = -1.2 + i * 0.02
            y = x**power
            if -1.22 <= y <= 1.3:
                points.append(self.axes.c2p(x, y))
        graph = VMobject(color=color, stroke_width=4)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_power_label(self, formula, color, position):
        label = MathTex("y", "=", formula, color=WHITE).scale(0.62)
        label.set_color_by_tex("y", self.OUTPUT_COLOR)
        label.set_color_by_tex("x", color)
        label.move_to(position)
        return label

    def make_summary_card(self, label, color, width=1.75):
        box = RoundedRectangle(
            width=width,
            height=0.48,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.5,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = Text(label, font_size=19, color=color)
        text.move_to(box)
        return VGroup(box, text)
