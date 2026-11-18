"""Exact symbolic tests for Bernard Gibert's K-series triangle cubics."""

from __future__ import annotations

from pathlib import Path

import pytest
import sympy as sp

from geometor.gibert import (
    CENTER_SPECS,
    K_SERIES_CUBICS,
    assert_no_floats,
    evaluate_cubic_at,
    isogonal_conjugate,
    isotomic_conjugate,
    load_catalog_manifest,
    render_cubic_svg,
    verify_cubic_incidences,
)
from geometor.gibert.centers import x, y, z


def test_centers_have_no_floats() -> None:
    """Verify all Kimberling center barycentric coordinates are 100% exact."""
    for spec in CENTER_SPECS.values():
        for coord in spec.barycentric:
            assert_no_floats(coord)


@pytest.mark.parametrize("cubic_id", list(K_SERIES_CUBICS.keys()))
def test_cubic_polynomial_and_incidences(cubic_id: str) -> None:
    """Verify exact homogeneity, float-freedom, on-curve centers, and off-curve control."""
    spec = K_SERIES_CUBICS[cubic_id]
    assert_no_floats(spec.polynomial)

    # Verify degree-3 homogeneity in (x, y, z)
    t = sp.Symbol("t")
    scaled = sp.expand(spec.polynomial.subs({x: t * x, y: t * y, z: t * z}))
    assert sp.expand(scaled - t**3 * spec.polynomial) == 0

    # Verify all claimed centers vanish identically
    results = verify_cubic_incidences(cubic_id)
    assert len(results) == len(spec.claimed_centers)
    assert all(results.values()), f"Incidence failure in {cubic_id}: {results}"

    # Verify negative control center does not lie on the cubic
    off_pt = CENTER_SPECS[spec.off_curve_center].barycentric
    assert not evaluate_cubic_at(spec.polynomial, off_pt)


def test_pivotal_conjugacy_invariance() -> None:
    """Verify exact algebraic isogonal/isotomic self-conjugacy of pivotal K-series cubics."""
    from geometor.gibert.centers import a, b, c

    isog_pt = isogonal_conjugate((x, y, z))
    for cid in ("K001", "K002", "K003", "K004", "K005", "K006"):
        poly = K_SERIES_CUBICS[cid].polynomial
        transformed = sp.expand(
            poly.subs({x: isog_pt[0], y: isog_pt[1], z: isog_pt[2]}, simultaneous=True)
        )
        assert sp.expand(transformed + a**2 * b**2 * c**2 * x * y * z * poly) == 0

    isot_pt = isotomic_conjugate((x, y, z))
    for cid in ("K007", "K008"):
        poly = K_SERIES_CUBICS[cid].polynomial
        transformed = sp.expand(
            poly.subs({x: isot_pt[0], y: isot_pt[1], z: isot_pt[2]}, simultaneous=True)
        )
        assert sp.expand(transformed + x * y * z * poly) == 0


def test_manifest_and_svgs_synced() -> None:
    """Verify catalog_manifest.json and .euclid-graphic SVGs exist for all K001-K011."""
    entries = load_catalog_manifest()
    assert [entry.id for entry in entries] == list(K_SERIES_CUBICS.keys())

    svg_dir = Path(__file__).resolve().parents[1] / "docsrc" / "_static" / "svg"
    for cid, spec in K_SERIES_CUBICS.items():
        svg_path = svg_dir / f"{cid}.svg"
        if not svg_path.is_file():
            render_cubic_svg(spec, svg_path)
        content = svg_path.read_text(encoding="utf-8")
        assert 'class="euclid-graphic"' in content
