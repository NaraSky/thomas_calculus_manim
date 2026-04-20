from manim import *


class Scene5_InputOutputPairsBecomePoints(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    POINT_COLOR = BLUE
    GRAPH_COLOR = BLUE

    def construct(self):
        self.setup_layout()
        self.step1_create_mappings()
        self.step2_highlight_one_mapping()
        self.step3_convert_mapping_to_pair()
        self.step4_create_coordinate_plane()
        self.step5_place_first_point()
        self.step6_place_remaining_points()
        self.step7_connect_points()
        self.step8_write_graph_definition()
        self.step9_emphasize_graph_as_collection()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.samples = [(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)]
        self.left_input_x = -5.7
        self.left_output_x = -4.15
        self.row_ys = [1.7, 0.95, 0.2, -0.55, -1.3]

        self.create_formula()
        self.create_mapping_rows()
        self.create_axes()
        self.create_points()
        self.create_graph()
        self.create_definition()

    def create_formula(self):
        self.formula = MathTex("y", "=", "x^2", color=WHITE)
        self.formula.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.formula.set_color_by_tex("x", self.INPUT_COLOR)
        self.formula.to_edge(UP, buff=0.35)

    def create_mapping_rows(self):
        self.input_label = Text("inputs", font_size=24, color=self.INPUT_COLOR)
        self.output_label = Text("outputs", font_size=24, color=self.OUTPUT_COLOR)
        self.input_label.move_to([self.left_input_x, 2.45, 0])
        self.output_label.move_to([self.left_output_x, 2.45, 0])

        self.input_cards = VGroup()
        self.output_cards = VGroup()
        self.mapping_arrows = VGroup()
        self.mapping_rows = VGroup()

        for index, ((x_value, y_value), row_y) in enumerate(zip(self.samples, self.row_ys)):
            input_card = self.make_card(f"x={x_value}", self.INPUT_COLOR, width=0.92)
            output_card = self.make_card(f"y={y_value}", self.OUTPUT_COLOR, width=0.92)
            input_card.move_to([self.left_input_x, row_y, 0])
            output_card.move_to([self.left_output_x, row_y, 0])
            arrow = Arrow(
                input_card.get_right(),
                output_card.get_left(),
                buff=0.12,
                color=WHITE,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.12,
            )

            setattr(self, f"input_card_{index}", input_card)
            setattr(self, f"output_card_{index}", output_card)
            setattr(self, f"mapping_arrow_{index}", arrow)

            self.input_cards.add(input_card)
            self.output_cards.add(output_card)
            self.mapping_arrows.add(arrow)
            self.mapping_rows.add(VGroup(input_card, arrow, output_card))

        self.mapping_area = VGroup(
            self.formula,
            self.input_label,
            self.output_label,
            self.mapping_rows,
        )

    def create_axes(self):
        self.axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[0, 4.5, 1],
            x_length=5.2,
            y_length=4.0,
            axis_config={
                "color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            },
            tips=True,
        )
        self.axes.move_to([2.0, -0.3, 0])

        self.x_axis_label = MathTex("x", color=self.INPUT_COLOR).scale(0.75)
        self.y_axis_label = MathTex("y", color=self.OUTPUT_COLOR).scale(0.75)
        self.x_axis_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        self.y_axis_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.axis_labels = VGroup(self.x_axis_label, self.y_axis_label)

    def create_points(self):
        self.graph_points = VGroup()
        self.coordinate_labels = VGroup()

        for index, (x_value, y_value) in enumerate(self.samples):
            point = Dot(
                self.axes.c2p(x_value, y_value),
                radius=0.065,
                color=self.POINT_COLOR,
            )
            label = MathTex(f"({x_value},{y_value})", color=WHITE).scale(0.48)
            label.next_to(point, UP, buff=0.08)

            setattr(self, f"graph_point_{index}", point)
            setattr(self, f"coordinate_label_{index}", label)

            self.graph_points.add(point)
            self.coordinate_labels.add(label)

        self.selected_coordinate = MathTex("(1,1)", color=WHITE).scale(0.75)
        self.selected_coordinate.move_to([-1.15, -2.25, 0])

    def create_graph(self):
        self.graph_curve = self.axes.plot(
            lambda x: x**2,
            x_range=[-2.08, 2.08],
            color=self.GRAPH_COLOR,
            stroke_width=4,
        )
        self.graph_label = MathTex("y=x^2", color=WHITE).scale(0.7)
        self.graph_label.set_color_by_tex("y", self.OUTPUT_COLOR)
        self.graph_label.set_color_by_tex("x", self.INPUT_COLOR)
        self.graph_label.next_to(self.graph_curve, RIGHT, buff=0.2)

    def create_definition(self):
        self.definition = MathTex(
            r"\text{graph}",
            "=",
            r"\{(x,f(x))\mid x\in D\}",
            color=WHITE,
        )
        self.definition.set_color_by_tex("graph", self.GRAPH_COLOR)
        self.definition.set_color_by_tex("x", self.INPUT_COLOR)
        self.definition.set_color_by_tex("f(x)", self.OUTPUT_COLOR)
        self.definition.scale(0.6)
        self.definition.move_to([1.25, -3.05, 0])

    def step1_create_mappings(self):
        self.play(FadeIn(self.mapping_area), run_time=2)
        self.wait()

    def step2_highlight_one_mapping(self):
        self.play(Indicate(self.mapping_rows[3], color=self.POINT_COLOR), run_time=2)
        self.wait()

    def step3_convert_mapping_to_pair(self):
        source = VGroup(self.input_card_3.copy(), self.output_card_3.copy())
        self.play(ReplacementTransform(source, self.selected_coordinate), run_time=2)
        self.wait()

    def step4_create_coordinate_plane(self):
        self.play(Create(self.axes), FadeIn(self.axis_labels), run_time=2)
        self.wait()

    def step5_place_first_point(self):
        self.play(
            ReplacementTransform(self.selected_coordinate, self.graph_point_3),
            FadeIn(self.coordinate_label_3),
            run_time=2,
        )
        self.wait()

    def step6_place_remaining_points(self):
        animations = []
        for index in [0, 1, 2, 4]:
            source = VGroup(self.input_cards[index].copy(), self.output_cards[index].copy())
            target = VGroup(self.graph_points[index], self.coordinate_labels[index])
            animations.append(ReplacementTransform(source, target))
        self.play(LaggedStart(*animations, lag_ratio=0.22), run_time=4)
        self.wait()

    def step7_connect_points(self):
        self.play(Create(self.graph_curve), FadeIn(self.graph_label), run_time=3)
        self.wait()

    def step8_write_graph_definition(self):
        self.play(Write(self.definition), run_time=2)
        self.wait()

    def step9_emphasize_graph_as_collection(self):
        self.play(
            Indicate(VGroup(self.graph_points, self.graph_curve), color=self.GRAPH_COLOR),
            Indicate(self.definition, color=self.GRAPH_COLOR),
            run_time=2,
        )
        self.wait()

    def make_card(self, label, color, width=1.15, height=0.48):
        box = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.5,
            fill_color=color,
            fill_opacity=0.12,
        )
        text = MathTex(label, color=color).scale(0.55)
        text.move_to(box)
        return VGroup(box, text)
