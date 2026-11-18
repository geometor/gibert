"""Public package interface for ``geometor.gibert``."""

from __future__ import annotations

from .app import main, run
from .catalog import CatalogEntrySpec, assert_no_floats, load_catalog_manifest
from .centers import (
    CENTER_SPECS,
    CenterSpec,
    evaluate_cubic_at,
    isogonal_conjugate,
    isotomic_conjugate,
)
from .cubics import (
    K_SERIES_CUBICS,
    CubicSpec,
    pk_isogonal,
    pk_isotomic,
    verify_cubic_incidences,
)
from .render import render_all_cubics, render_cubic_svg

__version__ = "0.1.0"

__all__ = [
    "CENTER_SPECS",
    "CatalogEntrySpec",
    "CenterSpec",
    "CubicSpec",
    "K_SERIES_CUBICS",
    "__version__",
    "assert_no_floats",
    "evaluate_cubic_at",
    "isogonal_conjugate",
    "isotomic_conjugate",
    "load_catalog_manifest",
    "main",
    "pk_isogonal",
    "pk_isotomic",
    "render_all_cubics",
    "render_cubic_svg",
    "run",
    "verify_cubic_incidences",
]
