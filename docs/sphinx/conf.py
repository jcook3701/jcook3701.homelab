"""Sphinx Configuration

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Configuration file for the Sphinx documentation builder.
  For the full list of built-in configuration values, see the documentation:
  https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import sys

from nutrimatic.build import add_yaml_front_matter, clean_module_docstring, skip_dupes
from sphinx.application import Sphinx

# -- Path setup --------------------------------------------------------------

# Add the source directory to sys.path so Sphinx can find your package
sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "homelab"
copyright = "2025, Jared Cook"  # noqa: A001
author = "Jared Cook"
release = "1.0.0"

html_context = {
    "copyright": "2025, Jared Cook",
}

# Main Sphinx Entry Point
root_doc = "api"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Mock imports that aren't available in your environment
autodoc_mock_imports: list[str] = []

extensions = [
    "myst_parser",  # MyST for Markdown
    "sphinx.ext.autodoc",  # autodoc for docstrings
    "sphinx.ext.napoleon",  # Supports Google/NumPy style docstrings
    "sphinx.ext.viewcode",  # Adds links to source code
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "sphinx_markdown_builder",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

smartquotes = False
numpydoc_class_members_toctree = False
autosummary_generate = True
autodoc_member_order = "bysource"
autosummary_generate = True
autosummary_generate_dir = "_autosummary_generated"

# Source file suffixes: support both .rst and .md
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Templates and exclusions
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Optional: show class members by default in the sidebar
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}


def setup(app: Sphinx) -> None:
    app.connect("autodoc-skip-member", skip_dupes)
    app.connect("autodoc-process-docstring", clean_module_docstring)
    app.connect("source-read", add_yaml_front_matter)
