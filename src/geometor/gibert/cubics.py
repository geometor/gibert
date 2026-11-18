"""Exact symbolic definitions and incidence verification for Gibert's K-series cubics."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from .catalog import assert_no_floats
from .centers import (
    CENTER_SPECS,
    SA,
    SB,
    SC,
    BarycentricPoint,
    a,
    b,
    c,
    evaluate_cubic_at,
    x,
    y,
    z,
)

__all__ = [
    "CubicSpec",
    "K_SERIES_CUBICS",
    "lemoine_cubic_polynomial",
    "pk_isogonal",
    "pk_isotomic",
    "simson_cubic_polynomial",
    "tucker_cubic_polynomial",
    "verify_cubic_incidences",
]


@dataclass(frozen=True, slots=True)
class CubicSpec:
    """Exact symbolic specification of a Bernard Gibert K-series triangle cubic."""

    id: str
    order: int
    name: str
    classification: str
    conjugacy: str
    pole: str | None
    pivot: str | None
    claimed_centers: tuple[str, ...]
    off_curve_center: str
    equation_latex: str
    description: str
    polynomial: sp.Expr


def pk_isogonal(pivot: BarycentricPoint) -> sp.Expr:
    """Return the exact homogeneous barycentric polynomial for ``pK(X6, P)``.

    Defined as ``det(M, M*, P) = 0``, where ``M = (x : y : z)`` and
    ``M* = (a^2 y z : b^2 z x : c^2 x y)`` is the isogonal conjugate of ``M``.

    Args:
        pivot: Exact barycentric coordinates ``(u, v, w)`` of the pivot ``P``.

    Returns:
        Expanded homogeneous cubic polynomial in ``(x, y, z)``.
    """
    u, v, w = pivot
    poly = sp.expand(
        u * x * (c**2 * y**2 - b**2 * z**2)
        + v * y * (a**2 * z**2 - c**2 * x**2)
        + w * z * (b**2 * x**2 - a**2 * y**2)
    )
    assert_no_floats(poly)
    return poly


def pk_isotomic(pivot: BarycentricPoint) -> sp.Expr:
    """Return the exact homogeneous barycentric polynomial for ``pK(X2, P)``.

    Defined as ``det(M, M^tau, P) = 0``, where ``M = (x : y : z)`` and
    ``M^tau = (y z : z x : x y)`` is the isotomic conjugate of ``M``.

    Args:
        pivot: Exact barycentric coordinates ``(u, v, w)`` of the pivot ``P``.

    Returns:
        Expanded homogeneous cubic polynomial in ``(x, y, z)``.
    """
    u, v, w = pivot
    poly = sp.expand(
        u * x * (y**2 - z**2)
        + v * y * (z**2 - x**2)
        + w * z * (x**2 - y**2)
    )
    assert_no_floats(poly)
    return poly


def lemoine_cubic_polynomial() -> sp.Expr:
    """Return the exact homogeneous barycentric polynomial for K009 (Lemoine cubic).

    Locus of ``M = (x : y : z)`` whose cevians ``MA, MB, MC`` meet the
    perpendicular bisectors of ``BC, CA, AB`` in three collinear points.
    """
    poly = sp.expand(
        a**4 * SA * y * z * (y - z)
        + b**4 * SB * z * x * (z - x)
        + c**4 * SC * x * y * (x - y)
        + (a**2 - b**2) * (b**2 - c**2) * (c**2 - a**2) * x * y * z
    )
    assert_no_floats(poly)
    return poly


def simson_cubic_polynomial() -> sp.Expr:
    """Return the exact homogeneous barycentric polynomial for K010 (Simson cubic).

    Locus of the tripoles (trilinear poles) of the Simson lines of ``ABC``.
    """
    poly = sp.expand(
        2 * SA * x * (y**2 + z**2)
        + 2 * SB * y * (z**2 + x**2)
        + 2 * SC * z * (x**2 + y**2)
        - 2 * (a**2 + b**2 + c**2) * x * y * z
    )
    assert_no_floats(poly)
    return poly


def tucker_cubic_polynomial() -> sp.Expr:
    """Return the exact homogeneous barycentric polynomial for K011 (Original Tucker cubic).

    Locus of ``M = (x : y : z)`` whose cevian triangle has the same signed area
    as the orthic triangle of ``ABC``.
    """
    poly = sp.expand(
        a**2 * b**2 * c**2 * x * y * z
        - SA * SB * SC * (y + z) * (z + x) * (x + y)
    )
    assert_no_floats(poly)
    return poly


def _c(code: str) -> BarycentricPoint:
    return CENTER_SPECS[code].barycentric


K_SERIES_CUBICS: dict[str, CubicSpec] = {
    "K001": CubicSpec(
        id="K001",
        order=1,
        name="Neuberg Cubic",
        classification="pK(X6, X30)",
        conjugacy="isogonal",
        pole="X6",
        pivot="X30",
        claimed_centers=("X1", "X3", "X4", "X13", "X14", "X15", "X16", "X30"),
        off_curve_center="X2",
        equation_latex=(
            r"\sum_{\text{cyc}} \left(S^2 - 3 S_B S_C\right) "
            r"x \left(c^2 y^2 - b^2 z^2\right) = 0"
        ),
        description=(
            "Isogonal pivotal cubic with pole X(6) and pivot X(30) (Euler infinity point): "
            "locus of points M such that M, its isogonal conjugate M*, and X(30) are collinear, "
            "equivalently MM* is parallel to the Euler line."
        ),
        polynomial=pk_isogonal(_c("X30")),
    ),
    "K002": CubicSpec(
        id="K002",
        order=2,
        name="Thomson Cubic",
        classification="pK(X6, X2)",
        conjugacy="isogonal",
        pole="X6",
        pivot="X2",
        claimed_centers=("X1", "X2", "X3", "X4", "X6", "X9", "X57"),
        off_curve_center="X5",
        equation_latex=r"\sum_{\text{cyc}} x \left(c^2 y^2 - b^2 z^2\right) = 0",
        description=(
            "Isogonal pivotal cubic with pole X(6) and pivot X(2) (centroid): "
            "locus of points M such that M, its isogonal conjugate M*, and X(2) are collinear."
        ),
        polynomial=pk_isogonal(_c("X2")),
    ),
    "K003": CubicSpec(
        id="K003",
        order=3,
        name="McCay Cubic",
        classification="pK(X6, X3)",
        conjugacy="isogonal",
        pole="X6",
        pivot="X3",
        claimed_centers=("X1", "X3", "X4"),
        off_curve_center="X2",
        equation_latex=(
            r"\sum_{\text{cyc}} a^2 S_A \, x \left(c^2 y^2 - b^2 z^2\right) = 0"
        ),
        description=(
            "Isogonal pivotal cubic with pole X(6) and pivot X(3) (circumcenter): "
            "locus of points M such that M, its isogonal conjugate M*, and X(3) are collinear; "
            "its three real asymptotes concur at X(2) making pairwise angles of 60 degrees."
        ),
        polynomial=pk_isogonal(_c("X3")),
    ),
    "K004": CubicSpec(
        id="K004",
        order=4,
        name="Darboux Cubic",
        classification="pK(X6, X20)",
        conjugacy="isogonal",
        pole="X6",
        pivot="X20",
        claimed_centers=("X1", "X3", "X4", "X20", "X40", "X64", "X84"),
        off_curve_center="X2",
        equation_latex=(
            r"\sum_{\text{cyc}} \left(a^2 S_A - S_B S_C\right) "
            r"x \left(c^2 y^2 - b^2 z^2\right) = 0"
        ),
        description=(
            "Isogonal pivotal cubic with pole X(6) and pivot X(20) (de Longchamps point): "
            "central at X(3) and locus of points M whose pedal triangle is a cevian triangle."
        ),
        polynomial=pk_isogonal(_c("X20")),
    ),
    "K005": CubicSpec(
        id="K005",
        order=5,
        name="Napoleon–Feuerbach Cubic",
        classification="pK(X6, X5)",
        conjugacy="isogonal",
        pole="X6",
        pivot="X5",
        claimed_centers=("X1", "X3", "X4", "X5", "X17", "X18", "X54"),
        off_curve_center="X2",
        equation_latex=(
            r"\sum_{\text{cyc}} \left(S^2 + S_B S_C\right) "
            r"x \left(c^2 y^2 - b^2 z^2\right) = 0"
        ),
        description=(
            "Isogonal pivotal cubic with pole X(6) and pivot X(5) (nine-point center): "
            "passes through the Napoleon points X(17), X(18) and Kosnita point X(54)."
        ),
        polynomial=pk_isogonal(_c("X5")),
    ),
    "K006": CubicSpec(
        id="K006",
        order=6,
        name="Orthocubic",
        classification="pK(X6, X4)",
        conjugacy="isogonal",
        pole="X6",
        pivot="X4",
        claimed_centers=("X1", "X3", "X4"),
        off_curve_center="X2",
        equation_latex=(
            r"\sum_{\text{cyc}} S_B S_C \, x \left(c^2 y^2 - b^2 z^2\right) = 0"
        ),
        description=(
            "Isogonal pivotal cubic with pole X(6) and pivot X(4) (orthocenter): "
            "locus of points M such that M, its isogonal conjugate M*, and X(4) are collinear."
        ),
        polynomial=pk_isogonal(_c("X4")),
    ),
    "K007": CubicSpec(
        id="K007",
        order=7,
        name="Lucas Cubic",
        classification="pK(X2, X69)",
        conjugacy="isotomic",
        pole="X2",
        pivot="X69",
        claimed_centers=("X2", "X4", "X7", "X8", "X20", "X69"),
        off_curve_center="X1",
        equation_latex=r"\sum_{\text{cyc}} S_A \, x \left(y^2 - z^2\right) = 0",
        description=(
            "Isotomic pivotal cubic with pole X(2) and pivot X(69) (isotomic conjugate of X(4)): "
            "locus of points M whose cevian triangle is orthologic to ABC."
        ),
        polynomial=pk_isotomic(_c("X69")),
    ),
    "K008": CubicSpec(
        id="K008",
        order=8,
        name="Droussent Cubic",
        classification="pK(X2, X316)",
        conjugacy="isotomic",
        pole="X2",
        pivot="X316",
        claimed_centers=("X2", "X67", "X316"),
        off_curve_center="X1",
        equation_latex=(
            r"\sum_{\text{cyc}} \left(b^4 + c^4 - a^4 - b^2 c^2\right) "
            r"x \left(y^2 - z^2\right) = 0"
        ),
        description=(
            "Circular isotomic pivotal cubic with pole X(2) and pivot X(316) "
            "(isotomic conjugate of X(67))."
        ),
        polynomial=pk_isotomic(_c("X316")),
    ),
    "K009": CubicSpec(
        id="K009",
        order=9,
        name="Lemoine Cubic",
        classification="K(O)",
        conjugacy="general",
        pole=None,
        pivot=None,
        claimed_centers=("X3", "X4", "X32", "X56"),
        off_curve_center="X2",
        equation_latex=(
            r"\sum_{\text{cyc}} a^4 S_A \, y z (y - z) "
            r"+ (a^2 - b^2)(b^2 - c^2)(c^2 - a^2) x y z = 0"
        ),
        description=(
            "Nodal cubic with perpendicular nodal tangents at X(3): locus of points M "
            "whose cevians MA, MB, MC meet the perpendicular bisectors of BC, CA, AB "
            "in three collinear points."
        ),
        polynomial=lemoine_cubic_polynomial(),
    ),
    "K010": CubicSpec(
        id="K010",
        order=10,
        name="Simson Cubic",
        classification="cK(#X2, X69)",
        conjugacy="general",
        pole=None,
        pivot=None,
        claimed_centers=("X2",),
        off_curve_center="X3",
        equation_latex=(
            r"\sum_{\text{cyc}} 2 S_A \, x \left(y^2 + z^2\right) "
            r"- 2 \left(a^2 + b^2 + c^2\right) x y z = 0"
        ),
        description=(
            "Locus of the tripoles (trilinear poles) of the Simson lines of the reference "
            "triangle ABC, with an acnode at the centroid X(2)."
        ),
        polynomial=simson_cubic_polynomial(),
    ),
    "K011": CubicSpec(
        id="K011",
        order=11,
        name="Tucker Cubic",
        classification="Tucker",
        conjugacy="general",
        pole=None,
        pivot=None,
        claimed_centers=("X4", "X69"),
        off_curve_center="X2",
        equation_latex=r"a^2 b^2 c^2 x y z - S_A S_B S_C (y + z)(z + x)(x + y) = 0",
        description=(
            "Original Tucker cubic: locus of points M whose cevian triangle has the "
            "same signed area as the orthic triangle of ABC."
        ),
        polynomial=tucker_cubic_polynomial(),
    ),
}


def verify_cubic_incidences(cubic_id: str) -> dict[str, bool]:
    """Verify exact symbolic vanishing of a K-series cubic at all claimed centers.

    Args:
        cubic_id: Identifier such as ``"K001"``.

    Returns:
        Mapping from each claimed Kimberling center code to ``True`` if verified.
    """
    spec = K_SERIES_CUBICS[cubic_id]
    return {
        center_code: evaluate_cubic_at(spec.polynomial, CENTER_SPECS[center_code].barycentric)
        for center_code in spec.claimed_centers
    }
