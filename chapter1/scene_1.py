from manim import *


class Scene1_FunctionDependency(Scene):
    INPUT_COLOR = YELLOW
    OUTPUT_COLOR = GREEN
    AREA_COLOR = BLUE
    OBJECT_BOX = 1.25
    VISUAL_WIDTH = 1.25
    VISUAL_HEIGHT = 0.95

    def construct(self):
        self.setup_layout()
        self.step1_create_rows()
        self.step2_change_altitude()
        self.step3_change_boiling_point()
        self.step4_change_time()
        self.step5_change_distance()
        self.step6_change_radius()
        self.step7_change_area()
        self.step8_highlight_structure()
        self.step9_transform_to_xy()

    def setup_layout(self):
        self.camera.background_color = BLACK

        self.input_x = -4.35
        self.output_x = 4.35
        self.arrow_start_x = -1.65
        self.arrow_end_x = 1.65
        self.row_y_values = [1.35, -0.55, -2.45]
        self.xy_y = 3.15

        self.create_altitude_input()
        self.create_boiling_point_output()
        self.create_time_input()
        self.create_distance_output()
        self.create_radius_input()
        self.create_area_output()
        self.create_arrows()
        self.create_rows()
        self.create_xy_relation()
        self.create_abstraction_seed()

    def create_altitude_input(self):
        center = self.input_point(0)
        self.altitude_track = Line(LEFT, RIGHT, color=self.INPUT_COLOR).set_width(self.OBJECT_BOX)
        self.altitude_knob = Dot(self.altitude_track.get_left(), color=self.INPUT_COLOR, radius=0.07)
        self.altitude_tick = Line(0.12 * DOWN, 0.12 * UP, color=self.INPUT_COLOR).move_to(self.altitude_knob)
        self.altitude_label = Text("Altitude", font_size=28, color=self.INPUT_COLOR)
        self.altitude_visual = VGroup(self.altitude_track, self.altitude_knob, self.altitude_tick)
        self.fit_visual(self.altitude_visual)
        self.altitude_input = VGroup(self.altitude_visual, self.altitude_label)
        self.altitude_label.next_to(self.altitude_track, DOWN, buff=0.22)
        self.altitude_input.move_to(center)

        self.altitude_indicator = VGroup(self.altitude_knob, self.altitude_tick)
        self.altitude_indicator_target = self.altitude_indicator.copy()
        self.altitude_indicator_target.move_to(self.altitude_track.get_right())

    def create_boiling_point_output(self):
        center = self.output_point(0)
        self.thermometer_body = RoundedRectangle(
            width=0.32,
            height=1.05,
            corner_radius=0.12,
            stroke_color=WHITE,
        )
        self.thermometer_bulb = Circle(
            radius=0.22,
            stroke_color=WHITE,
            fill_color=self.OUTPUT_COLOR,
            fill_opacity=0.85,
        )
        self.thermometer_bulb.next_to(self.thermometer_body, DOWN, buff=-0.07)
        self.thermometer_level = Rectangle(
            width=0.15,
            height=0.78,
            stroke_width=0,
            fill_color=self.OUTPUT_COLOR,
            fill_opacity=0.9,
        )
        self.position_level(self.thermometer_level, 0.78)
        self.boiling_label = Text("Boiling point", font_size=28, color=self.OUTPUT_COLOR)
        self.boiling_visual = VGroup(self.thermometer_body, self.thermometer_bulb, self.thermometer_level)
        self.fit_visual(self.boiling_visual)
        self.boiling_point_output = VGroup(
            self.boiling_visual,
            self.boiling_label,
        )
        self.boiling_label.next_to(self.boiling_visual, DOWN, buff=0.22)
        self.boiling_point_output.move_to(center)

        self.thermometer_level_target = Rectangle(
            width=0.15,
            height=0.28,
            stroke_width=0,
            fill_color=self.OUTPUT_COLOR,
            fill_opacity=0.9,
        )
        self.position_level(self.thermometer_level_target, 0.28)

    def create_time_input(self):
        center = self.input_point(1)
        self.clock_face = Circle(radius=0.45, color=WHITE)
        self.clock_hand = Line(ORIGIN, 0.32 * UP, color=self.INPUT_COLOR)
        self.time_label = Text("Time", font_size=28, color=self.INPUT_COLOR)
        self.time_visual = VGroup(self.clock_face, self.clock_hand)
        self.fit_visual(self.time_visual)
        self.time_input = VGroup(self.time_visual, self.time_label)
        self.time_label.next_to(self.clock_face, DOWN, buff=0.22)
        self.time_input.move_to(center)

        self.clock_hand_target = Line(
            self.clock_face.get_center(),
            self.clock_face.get_center() + 0.32 * RIGHT,
            color=self.INPUT_COLOR,
        )

    def create_distance_output(self):
        center = self.output_point(1)
        self.road = Line(LEFT, RIGHT, color=WHITE).set_width(self.OBJECT_BOX)
        self.distance_bar = Line(self.road.get_left(), self.road.get_left() + 0.08 * RIGHT, color=self.OUTPUT_COLOR)
        self.distance_bar.set_stroke(width=8)
        self.distance_dot = Dot(self.road.get_left(), color=self.OUTPUT_COLOR)
        self.distance_label = Text("Distance", font_size=28, color=self.OUTPUT_COLOR)
        self.distance_indicator = VGroup(self.distance_bar, self.distance_dot)
        self.distance_visual = VGroup(self.road, self.distance_indicator)
        self.fit_visual(self.distance_visual)
        self.distance_output = VGroup(self.distance_visual, self.distance_label)
        self.distance_label.next_to(self.road, DOWN, buff=0.24)
        self.distance_output.move_to(center)

        self.distance_bar_target = Line(self.road.get_left(), self.road.get_right(), color=self.OUTPUT_COLOR)
        self.distance_bar_target.set_stroke(width=8)
        self.distance_dot_target = self.distance_dot.copy().move_to(self.road.get_right())
        self.distance_indicator_target = VGroup(self.distance_bar_target, self.distance_dot_target)

    def create_radius_input(self):
        center = self.input_point(2)
        self.radius_anchor = Dot(color=WHITE).scale(0.6)
        self.radius_segment = Line(
            ORIGIN,
            0.62 * RIGHT,
            color=self.INPUT_COLOR,
        )
        self.radius_label = Text("Radius", font_size=28, color=self.INPUT_COLOR)
        self.radius_visual = VGroup(self.radius_anchor, self.radius_segment)
        self.fit_visual(self.radius_visual)
        self.radius_input = VGroup(self.radius_visual, self.radius_label)
        self.radius_label.next_to(self.radius_visual, DOWN, buff=0.22)
        self.radius_input.move_to(center)

        self.radius_segment_target = Line(
            self.radius_anchor.get_center(),
            self.radius_anchor.get_center() + 1.02 * RIGHT,
            color=self.INPUT_COLOR,
        )

    def create_area_output(self):
        center = self.output_point(2)
        self.area_fill = Circle(radius=0.24, stroke_width=0, fill_color=self.AREA_COLOR, fill_opacity=0.55)
        self.area_boundary = Circle(radius=0.48, color=WHITE)
        self.area_label = Text("Area", font_size=28, color=self.OUTPUT_COLOR)
        self.area_visual = VGroup(self.area_fill, self.area_boundary)
        self.fit_visual(self.area_visual)
        self.area_output = VGroup(self.area_visual, self.area_label)
        self.area_label.next_to(self.area_boundary, DOWN, buff=0.22)
        self.area_output.move_to(center)

        self.area_fill_target = Circle(
            radius=0.48,
            stroke_width=0,
            fill_color=self.AREA_COLOR,
            fill_opacity=0.55,
        ).move_to(self.area_boundary)

    def create_arrows(self):
        self.arrows = VGroup()
        for row_index in range(3):
            y = self.row_y_values[row_index]
            arrow = Arrow(
                start=[self.arrow_start_x, y, 0],
                end=[self.arrow_end_x, y, 0],
                buff=0,
                color=WHITE,
                stroke_width=5,
                max_tip_length_to_length_ratio=0.08,
            )
            self.arrows.add(arrow)

        self.altitude_arrow = self.arrows[0]
        self.time_arrow = self.arrows[1]
        self.radius_arrow = self.arrows[2]

    def create_rows(self):
        self.altitude_row = VGroup(self.altitude_input, self.altitude_arrow, self.boiling_point_output)
        self.time_row = VGroup(self.time_input, self.time_arrow, self.distance_output)
        self.radius_row = VGroup(self.radius_input, self.radius_arrow, self.area_output)
        self.rows = VGroup(self.altitude_row, self.time_row, self.radius_row)

    def create_xy_relation(self):
        self.x_label = MathTex("x", color=self.INPUT_COLOR).scale(1.55)
        self.y_label = MathTex("y", color=self.OUTPUT_COLOR).scale(1.55)
        self.xy_arrow = Arrow(LEFT, RIGHT, buff=0, color=WHITE, stroke_width=7)
        self.xy_relation = VGroup(self.x_label, self.xy_arrow, self.y_label)
        self.xy_relation.arrange(RIGHT, buff=0.45)
        self.xy_relation.move_to([0, self.xy_y, 0])

        self.abstraction_separator = Line(
            [-5.4, 2.45, 0],
            [5.4, 2.45, 0],
            color=GREY_B,
        ).set_stroke(width=1, opacity=0.45)
        self.xy_layer = VGroup(self.xy_relation, self.abstraction_separator)

    def create_abstraction_seed(self):
        self.abstraction_seed = VGroup(*[
            Dot(arrow.get_center(), color=self.INPUT_COLOR).scale(0.55)
            for arrow in self.arrows
        ])

    def step1_create_rows(self):
        self.play(FadeIn(self.rows), run_time=2)
        self.wait()

    def step2_change_altitude(self):
        self.play(Transform(self.altitude_indicator, self.altitude_indicator_target), run_time=3)
        self.wait()

    def step3_change_boiling_point(self):
        self.play(Transform(self.thermometer_level, self.thermometer_level_target), run_time=2)
        self.wait()

    def step4_change_time(self):
        self.play(Transform(self.clock_hand, self.clock_hand_target), run_time=3)
        self.wait()

    def step5_change_distance(self):
        self.play(Transform(self.distance_indicator, self.distance_indicator_target), run_time=3)
        self.wait()

    def step6_change_radius(self):
        self.play(Transform(self.radius_segment, self.radius_segment_target), run_time=3)
        self.wait()

    def step7_change_area(self):
        self.play(Transform(self.area_fill, self.area_fill_target), run_time=3)
        self.wait()

    def step8_highlight_structure(self):
        self.play(Indicate(self.arrows, color=self.INPUT_COLOR), run_time=2)
        self.wait()

    def step9_transform_to_xy(self):
        self.play(
            ReplacementTransform(self.abstraction_seed, self.xy_layer),
            run_time=2,
        )
        self.wait()

    def input_point(self, row_index):
        return np.array([self.input_x, self.row_y_values[row_index], 0])

    def output_point(self, row_index):
        return np.array([self.output_x, self.row_y_values[row_index], 0])

    def fit_visual(self, visual):
        if visual.get_width() > self.VISUAL_WIDTH:
            visual.set_width(self.VISUAL_WIDTH)
        if visual.get_height() > self.VISUAL_HEIGHT:
            visual.set_height(self.VISUAL_HEIGHT)

    def position_level(self, level, height):
        bottom = self.thermometer_body.get_bottom() + 0.06 * UP
        level.move_to(bottom + 0.5 * height * UP)
