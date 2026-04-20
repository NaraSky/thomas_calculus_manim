# Video Production Style Guide

## 1. Purpose

This document defines the production standard for 3Blue1Brown-style mathematical videos in this repository. It is an engineering specification for consistent mathematical design, animation behavior, visual style, scene architecture, and production workflow.

All future videos must follow these rules unless a documented exception is approved for a specific scene.

## 2. Core Principles

### Visual Before Symbolic

- Description: Introduce ideas with concrete visual objects before formulas.
- Rationale: Viewers should understand what a symbol refers to before reading it.
- Example: Show a growing area before writing `A(x)`.

### One Concept Per Scene

- Description: Each scene must communicate one primary mathematical idea.
- Rationale: Scene boundaries should reduce cognitive load.
- Example: One scene introduces Riemann rectangles; a later scene introduces the derivative of the area function.

### Preserve Object Identity

- Description: When an object changes role, transform it instead of replacing it abruptly.
- Rationale: Continuity helps viewers track meaning.
- Example: Transform a ring into a rectangle, then into a rectangle under a graph.

### Transform Instead of Replace

- Description: Prefer `Transform`, `ReplacementTransform`, and `MoveToTarget` for semantic transitions.
- Rationale: Motion should show conceptual equivalence.
- Example: Move `dx` from a graph sliver into an equation term.

### Geometry Maps to Notation

- Description: Every visual object used in a derivation must correspond to symbolic notation.
- Rationale: Formulas must feel extracted from the picture.
- Example: A thin area sliver maps to `dA`; its width maps to `dx`.

### Every Animation Represents Meaning

- Description: Animations must encode a mathematical, narrative, or attention-guiding purpose.
- Rationale: Decorative motion weakens precision.
- Example: Use `Indicate(dx_label)` to focus attention before dividing by `dx`.

## 3. Mathematical Design Rules

### Concept Introduction Rule

- Rule: Start from a concrete object, problem, or measurable quantity before showing formulas.
- Allowed patterns: circle before `pi R^2`; shaded region before integral notation; moving point before derivative notation.
- Forbidden patterns: starting with a formal definition without visual context.
- Example: Show concentric rings before writing `int_0^R 2 pi r dr`.

### Approximation Rule

- Rule: Approximation must be refined step by step.
- Allowed patterns: thick rectangles to thin rectangles; finite `dx` to smaller `dx`; rough ring strip to rectangle-ish strip.
- Forbidden patterns: jumping directly from rough visual to exact formula.
- Example: Animate `dx = 0.25`, then `0.125`, then smaller values.

### Mapping Rule

- Rule: Visual objects must be explicitly mapped to symbolic expressions.
- Allowed patterns: arrows, braces, color matching, `ReplacementTransform` from geometry to notation.
- Forbidden patterns: formulas that appear unrelated to visible objects.
- Example: Transform a highlighted sliver into `dA`.

### Generalization Rule

- Rule: General concepts must emerge from at least one concrete case.
- Allowed patterns: circle area -> arbitrary area under `f(x)`; `x^2` example -> general `f(x)`.
- Forbidden patterns: abstract generalization before intuition.
- Example: Derive `dA/dx approx x^2`, then generalize to `dA/dx approx f(x)`.

## 4. Animation Design Rules

### Timing

- Default semantic animation: `run_time = 2`.
- Complex geometry morph: `run_time = 3` to `5`.
- Fast label or emphasis animation: `run_time = 1`.
- Pause after each semantic step: required.

### Transform Rules

- Prefer: `Transform`, `ReplacementTransform`, `MoveToTarget`, `UpdateFromAlphaFunc`.
- Allowed: `FadeIn`, `FadeOut`, `Write`, `ShowCreation`, `GrowFromCenter`, `Indicate`.
- Avoid: sudden deletion, unrelated object swaps, cuts that break object identity.

### Attention Guidance

- Use color, arrows, braces, highlights, and `Indicate` to direct focus.
- Introduce labels close to the object they describe.
- Remove temporary guides after they have served their purpose.

### Sequencing

- Draw geometry first.
- Attach measurement labels second.
- Introduce symbolic notation third.
- Refine or generalize last.

## 5. Visual Style Rules

### Background

- Required background: black.
- Primary text and axes: white or light gray.

### Color Mapping

- Area or accumulated quantity: blue / green.
- Small change (`dx`, `dr`, `dA` marker): yellow.
- Error, cancellation, or invalid idea: red.
- Function graph: blue, green, or cyan, consistent within the scene.

### Typography

- Use LaTeX for mathematical notation.
- Use concise text labels.
- Keep labels readable and aligned with their referenced objects.

### Layout

- Align related objects by edges or centers.
- Keep equations near the geometry that generated them.
- Avoid overlap between labels, arrows, graphs, and animated objects.
- Use braces and arrows only when they clarify a mathematical mapping.

## 6. Scene Architecture Rules

Scene architecture should follow this pattern:

```text
Scene
-> ConceptScene
-> setup helpers
-> construct()
-> semantic helper methods
```

Each scene must represent one core idea. `construct()` should read like a storyboard and delegate to named helper methods.

Required scene method style:

```python
def construct(self):
    self.show_concrete_object()
    self.identify_measurements()
    self.map_to_notation()
    self.refine_or_generalize()
```

Reusable components should be implemented as helper methods or base scene classes when they appear in multiple scenes, such as graph setup, Riemann rectangles, ring construction, label creation, or endpoint animation.

## 7. Reusable Animation Templates

### Integral Animation Template

```python
self.setup_axes()
graph = self.get_graph(f)
rects = self.get_riemann_rectangles(graph, x_min=a, x_max=b, dx=dx)

self.play(ShowCreation(graph), run_time=2)
self.play(DrawBorderThenFill(rects, lag_ratio=0.5), run_time=2)
self.wait()

for smaller_dx in dx_values:
    new_rects = self.get_riemann_rectangles(graph, x_min=a, x_max=b, dx=smaller_dx)
    self.play(Transform(rects, new_rects, lag_ratio=0.5), run_time=2)
    self.wait()

self.play(Write(Tex(r"\int_a^b f(x)\,dx")), run_time=2)
self.wait()
```

### Derivative Animation Template

```python
self.move_endpoint_to(x)
self.move_endpoint_to(x + dx)
self.play(FadeIn(dx_group), FadeIn(dA_sliver), run_time=2)
self.wait()

self.play(Write(Tex(r"dA \approx f(x)\,dx")), run_time=2)
self.wait()

self.play(ReplacementTransform(..., Tex(r"{dA \over dx} \approx f(x)")), run_time=2)
self.wait()

self.transition_to_alt_config(deriv_dx=dx / 4, transformation_kwargs={"run_time": 2})
self.wait()
```

### Geometry-to-Notation Template

```python
self.play(ShowCreation(geometric_object), run_time=2)
self.play(GrowFromCenter(brace), Write(label), run_time=2)
self.wait()
self.play(ReplacementTransform(label.copy(), equation_part), run_time=2)
self.wait()
```

## 8. Timing and Rhythm Standards

- Concept animation: 2 seconds.
- Geometry morph: 3-5 seconds.
- Formula writing: 1-2 seconds.
- Attention indication: 1 second.
- Pause after idea: required.
- Pause after major derivation step: 1-3 seconds.
- Avoid long uninterrupted animation sequences without semantic checkpoints.

## 9. Production Workflow

Use this pipeline for every video:

```text
Concept
-> mathematical objective
-> visual metaphor
-> scene design
-> animation implementation
-> low-quality render review
-> timing and layout fixes
-> final render
```

Each scene must have a stated mathematical objective before implementation. The visual metaphor must be chosen before writing equations or animations.

## 10. Pre-Render Checklist

- Concept is defined.
- Scene has one primary idea.
- Visual metaphor is defined.
- Each visual object maps to notation or narrative purpose.
- Color mapping is consistent.
- Animation timing follows the standard.
- Pause exists after each semantic step.
- Labels are aligned and readable.
- No labels overlap animated objects.
- Transform continuity is preserved.
- Temporary guides are removed after use.
- Scene transition is prepared.
- Low-quality preview render has been inspected.
- Mathematical statements are correct.

## 11. Anti-Patterns

- Decorative animation without meaning.
- Multiple unrelated concepts in one scene.
- Inconsistent color usage.
- Sudden object deletion during conceptual transitions.
- Formula-first explanations without visual grounding.
- Symbols that do not correspond to visible objects.
- Dense equations introduced all at once.
- Labels far from referenced objects.
- Long animations without pauses or attention checkpoints.
- Reusing a color for conflicting meanings in the same scene.
- Treating approximation as exact before showing refinement.
- Introducing general notation before a concrete example.

