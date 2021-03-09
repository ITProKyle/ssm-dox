"""Sphinx config file.

Configuration file for the Sphinx documentation builder.

This file does only contain a selection of the most common options.
For a full list see the documentation: http://www.sphinx-doc.org/en/master/config

"""
# pylint: skip-file
import os
from pathlib import Path

import sphinx_rtd_theme
import toml

DOC_SRC = Path(__file__).parent
PROJECT_ROOT = DOC_SRC.parent.parent
PYPROJECT_FILE = PROJECT_ROOT / "pyproject.toml"

PYPROJECT = toml.load(PYPROJECT_FILE)
POETRY = PYPROJECT["tool"]["poetry"]

LANGUAGE = os.getenv("READTHEDOCS_LANGUAGE", "en")
PROJECT = os.getenv("READTHEDOCS_PROJECT", POETRY["name"])
READTHEDOCS = os.getenv("READTHEDOCS", None) == "True"
VERSION = os.getenv("READTHEDOCS_VERSION", "latest")


# -- Project information --------------------------------------------------------
author = POETRY["authors"][0]
copyright = "2021, Kyle Finley"
project = PROJECT
release = VERSION
version = VERSION


# -- General configuration ------------------------------------------------------
exclude_patterns = ["_build"]
extensions = [
    "sphinx_search.extension",
    # "sphinx_tabs.tabs",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),  # link to python docs
}
language = LANGUAGE
master_doc = "index"
# needs_sphinx = "3.5"
pygments_style = "sphinx"
source_encoding = "utf-8-sig"
source_suffix = ".rst"
sphinx_tabs_nowarn = True
templates_path = ["_templates"]


# -- Options for HTML output ----------------------------------------------------
html_context = {
    "github_user": "ITProKyle",
    "github_repo": PROJECT,
}
html_css_files = [
    "css/custom.css",
]
html_static_path = ["_static"]
html_title = f"ssm-dox ({VERSION})"
html_theme = "sphinx_rtd_theme"
html_theme_options = {"collapse_navigation": False}
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# -- Options for linkcheck builder ----------------------------------------------
linkcheck_anchors = False
linkcheck_timeout = 10


# -- Options for autodoc  -------------------------------------------------------
autoclass_content = "both"


# -- Options for napoleon  ------------------------------------------------------
napoleon_google_docstring = True
napoleon_include_init_with_doc = False
