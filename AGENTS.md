# Repository Guidelines

## Project Structure & Module Organization

This repository contains Manim-based Thomas Calculus materials organized by textbook chapter. `chapter1/` stores section PDFs and Markdown notes for Chapter 1. `chapter2/docx/` stores Chapter 2 section PDFs and Markdown notes. Keep new section materials next to related chapter content, using the existing pattern such as `Thomas_Calculus_2_6.md` and `Thomas Calculus 14th Edition-2.6.pdf`.

`pyproject.toml` defines the Python project metadata and dependencies. `uv.lock` pins the resolved environment. `.venv/`, `media/`, `.idea/`, and `videos-master-3b1b/` are ignored local or reference directories and should not be committed.

## Build, Test, and Development Commands

- `uv sync`: create or update the Python 3.12 environment from `pyproject.toml` and `uv.lock`.
- `uv run manim --version`: verify Manim is installed and available.
- `uv run manim -pql chapter2/section_2_1.py SceneName`: render a scene in low quality and preview it. Replace the path and scene class as needed.
- `uv run python -m compileall chapter1 chapter2`: check Python files for syntax errors when scene files are added.

Rendered videos and images are written under `media/`; treat them as generated output unless a contributor explicitly requests otherwise.

## Coding Style & Naming Conventions

Use Python 3.12 syntax, 4-space indentation, and clear Manim scene class names in `PascalCase`. Name scene files by chapter and section, for example `section_2_6.py`. Prefer small helper functions for repeated graph, axis, label, or animation setup. Keep mathematical notation consistent with the local Markdown notes and source PDFs.

Markdown files should use concise headings, readable formulas, and section-oriented filenames matching the existing `Thomas_Calculus_<chapter>_<section>.md` pattern.

## Testing Guidelines

There is no dedicated test suite yet. For Python scene changes, run `uv run python -m compileall chapter1 chapter2` and render at least one affected scene with Manim in low quality (`-ql`). For visual changes, inspect the preview for layout, label overlap, timing, and mathematical correctness before submitting.

## Commit & Pull Request Guidelines

Recent commits use short, imperative, lowercase summaries, for example `add section 2.6 on limits involving infinity and asymptotes`. Follow that style and keep each commit focused on one chapter section or infrastructure change.

Pull requests should describe the affected section(s), list render commands used for validation, and note any generated artifacts intentionally included. Link related issues when available and include screenshots or short preview clips for visual scene changes.

## Agent-Specific Instructions

Do not modify ignored vendored/reference content unless explicitly asked. Avoid committing `__pycache__/`, `.venv/`, IDE files, or Manim `media/` output.
