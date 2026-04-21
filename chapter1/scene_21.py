from manim import *


class Scene21_LogarithmicFunctions(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    BASE_COLOR = BLUE
    EXP_COLOR = TEAL
    LOG_COLOR = GREEN
    DOMAIN_COLOR = RED
    GUIDE_COLOR = GREY_B
    HIGHLIGHT_COLOR = YELLOW

    def construct(self):
        self.setup_layout()
        self.step1_create_axes()
        self.step2_show_exponential_reference()
        self.step3_show_inverse_line()
        self.step4_reflect_to_logarithm()
        self.step5_write_log_formula()
        self.step6_mark_anchor_point()
        self.step7_mark_domain_boundary()
        self.step8_compare_bases()
        self.step9_summarize_logarithms()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.create_axes()
        self.create_formulas()
        self.create_graphs()
        self.create_inverse_guides()
        self.create_anchor_marker()
        self.create_domain_marker()
        self.create_base_comparison()
        self.create_summary()

    def create_axes(self):
        self.axes = Axes(
            x_range=[-1.2, 5.2, 1],
            y_range=[-2.4, 3.6, 1],
            x_length=6.9,
            y_length=5.2,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([-1.1, -0.1, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.68)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.68)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_formulas(self):
        self.exp_formula = MathTex("y", "=", "2^x", color=WHITE).scale(0.76)
        self.exp_formula.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.exp_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.exp_formula.move_to([3.25, 2.35, 0])

        self.inverse_text = MathTex(r"\text{swap }x\text{ and }y", color=self.HIGHLIGHT_COLOR).scale(0.62)
        self.inverse_text.move_to([3.25, 1.55, 0])

        self.log_formula = MathTex("y", "=", "\\log_2", "x", color=WHITE).scale(0.76)
        self.log_formula.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.log_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.log_formula.set_color_by_tex("\\log_2", self.LOG_COLOR)
        self.log_formula.move_to(self.exp_formula)

        self.domain_formula = MathTex("x", ">", "0", color=WHITE).scale(0.72)
        self.domain_formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.domain_formula.set_color_by_tex("0", self.DOMAIN_COLOR)
        self.domain_formula.move_to([3.35, -0.5, 0])

    def create_graphs(self):
        self.exp_graph = self.make_graph(lambda x: 2**x, -1.0, 1.75, self.EXP_COLOR)
        self.log_graph = self.make_graph(lambda x: np.log2(x), 0.16, 5.0, self.LOG_COLOR)

    def create_inverse_guides(self):
        self.inverse_line = self.make_graph(lambda x: x, -1.0, 3.25, self.GUIDE_COLOR, stroke_width=2.5)
        self.inverse_line.set_opacity(0.8)
        self.inverse_label = MathTex("y", "=", "x", color=WHITE).scale(0.52)
        self.inverse_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.inverse_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.inverse_label.move_to(self.axes.c2p(3.1, 3.0))

        exp_point = self.axes.c2p(1, 2)
        log_point = self.axes.c2p(2, 1)
        self.swap_points = VGroup(
            Dot(exp_point, radius=0.075, color=self.EXP_COLOR),
            Dot(log_point, radius=0.075, color=self.LOG_COLOR),
        )
        self.swap_arrow = CurvedArrow(
            exp_point + UP * 0.08,
            log_point + RIGHT * 0.08,
            color=self.HIGHLIGHT_COLOR,
            stroke_width=3,
            angle=-TAU / 4,
        )
        self.swap_label = MathTex("(1,2)", "\\leftrightarrow", "(2,1)", color=WHITE).scale(0.52)
        self.swap_label.set_color_by_tex("1", self.INPUT_COLOR)
        self.swap_label.set_color_by_tex("2", self.OUTPUT_COLOR)
        self.swap_label.move_to([3.25, -0.05, 0])

    def create_anchor_marker(self):
        self.anchor_dot = Dot(self.axes.c2p(1, 0), radius=0.08, color=self.LOG_COLOR)
        self.anchor_label = MathTex("(1,0)", color=WHITE).scale(0.56)
        self.anchor_label.next_to(self.anchor_dot, DOWN + RIGHT, buff=0.12)

    def create_domain_marker(self):
        self.vertical_boundary = DashedLine(
            self.axes.c2p(0, -2.15),
            self.axes.c2p(0, 3.25),
            color=self.DOMAIN_COLOR,
            stroke_width=2,
            dash_length=0.16,
        )
        self.vertical_boundary.set_opacity(0.8)
        self.domain_ray = Line(
            self.axes.c2p(0.08, -0.42),
            self.axes.c2p(4.35, -0.42),
            color=self.DOMAIN_COLOR,
            stroke_width=3,
        )

    def create_base_comparison(self):
        self.log_three_graph = self.make_graph(lambda x: np.log(x) / np.log(3), 0.16, 5.0, self.BASE_COLOR)
        self.log_ten_graph = self.make_graph(lambda x: np.log10(x), 0.16, 5.0, self.HIGHLIGHT_COLOR)

        self.base_labels = VGroup(
            self.make_curve_label("\\log_2 x", self.LOG_COLOR, [1.12, 1.78, 0]),
            self.make_curve_label("\\log_3 x", self.BASE_COLOR, [2.0, 1.22, 0]),
            self.make_curve_label("\\log_{10} x", self.HIGHLIGHT_COLOR, [2.78, 0.82, 0]),
        )

    def create_summary(self):
        self.summary = VGroup(
            self.make_summary_card("inverse", self.HIGHLIGHT_COLOR, width=1.35),
            self.make_summary_card("(1,0)", self.LOG_COLOR, width=1.25),
            self.make_summary_card("x>0", self.DOMAIN_COLOR, width=1.15),
        )
        self.summary.arrange(RIGHT, buff=0.2)
        self.summary.to_edge(DOWN, buff=0.34)

        self.final_statement = MathTex(r"\text{logs undo exponentials}", color=WHITE).scale(0.54)
        self.final_statement.move_to([3.18, 2.32, 0])

    def step1_create_axes(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step2_show_exponential_reference(self):
        self.play(Write(self.exp_formula), Create(self.exp_graph), run_time=3)
        self.wait()

    def step3_show_inverse_line(self):
        self.play(Create(self.inverse_line), Write(self.inverse_label), Write(self.inverse_text), run_time=2)
        self.wait()

    def step4_reflect_to_logarithm(self):
        self.play(
            ReplacementTransform(self.exp_graph, self.log_graph),
            FadeIn(self.swap_points),
            Create(self.swap_arrow),
            Write(self.swap_label),
            run_time=3,
        )
        self.wait()

    def step5_write_log_formula(self):
        self.play(
            ReplacementTransform(self.exp_formula, self.log_formula),
            FadeOut(self.inverse_text),
            run_time=2,
        )
        self.wait()

    def step6_mark_anchor_point(self):
        self.play(FadeIn(self.anchor_dot), Write(self.anchor_label), run_time=2)
        self.wait()

    def step7_mark_domain_boundary(self):
        self.play(Create(self.vertical_boundary), Create(self.domain_ray), Write(self.domain_formula), run_time=2)
        self.wait()

    def step8_compare_bases(self):
        self.play(Create(self.log_three_graph), Create(self.log_ten_graph), FadeIn(self.base_labels), run_time=3)
        self.wait()

    def step9_summarize_logarithms(self):
        self.play(
            FadeOut(self.swap_arrow),
            FadeOut(self.swap_label),
            FadeOut(self.swap_points),
            FadeOut(self.inverse_label),
            ReplacementTransform(self.log_formula, self.final_statement),
            FadeIn(self.summary),
            run_time=2,
        )
        self.wait()

    def make_graph(self, function, x_start, x_end, color, stroke_width=4):
        points = []
        samples = 180
        for index in range(samples + 1):
            alpha = index / samples
            x = x_start + (x_end - x_start) * alpha
            y = function(x)
            if -2.25 <= y <= 3.35:
                points.append(self.axes.c2p(x, y))

        graph = VMobject(color=color, stroke_width=stroke_width)
        graph.set_points_smoothly(points)
        graph.set_fill(opacity=0)
        return graph

    def make_curve_label(self, label, color, position):
        text = MathTex(label, color=color).scale(0.54)
        text.move_to(position)
        return text

    def make_summary_card(self, label, color, width=1.2):
        box = RoundedRectangle(
            width=width,
            height=0.5,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.4,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(r"\text{" + label + "}" if label == "inverse" else label, color=color).scale(0.5)
        text.move_to(box)
        return VGroup(box, text)
