"""Exact symbolic barycentric coordinates for Kimberling triangle centers."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from .catalog import assert_no_floats

__all__ = [
    "BarycentricPoint",
    "CENTER_SPECS",
    "CenterSpec",
    "S",
    "S2",
    "SA",
    "SB",
    "SC",
    "a",
    "b",
    "barycentric_to_cartesian",
    "c",
    "evaluate_cubic_at",
    "isogonal_conjugate",
    "isotomic_conjugate",
    "r3",
    "x",
    "y",
    "z",
]

BarycentricPoint = tuple[sp.Expr, sp.Expr, sp.Expr]

a, b, c = sp.symbols("a b c", positive=True)
x, y, z = sp.symbols("x y z")
S = sp.Symbol("S", positive=True)
r3 = sp.Symbol("r3", positive=True)

SA: sp.Expr = (b**2 + c**2 - a**2) / 2
SB: sp.Expr = (c**2 + a**2 - b**2) / 2
SC: sp.Expr = (a**2 + b**2 - c**2) / 2
S2: sp.Expr = sp.expand(SA * SB + SB * SC + SC * SA)


@dataclass(frozen=True, slots=True)
class CenterSpec:
    """Exact symbolic specification of a Kimberling triangle center."""

    index: int
    code: str
    name: str
    barycentric: BarycentricPoint


def _pt(u: sp.Expr | int, v: sp.Expr | int, w: sp.Expr | int) -> BarycentricPoint:
    """Construct a validated exact barycentric triple."""
    triple = (sp.sympify(u), sp.sympify(v), sp.sympify(w))
    for coord in triple:
        assert_no_floats(coord)
    return triple


def isogonal_conjugate(pt: BarycentricPoint) -> BarycentricPoint:
    """Return the exact isogonal conjugate ``(a^2 y z : b^2 z x : c^2 x y)``."""
    u, v, w = pt
    return (
        sp.expand(a**2 * v * w),
        sp.expand(b**2 * w * u),
        sp.expand(c**2 * u * v),
    )


def isotomic_conjugate(pt: BarycentricPoint) -> BarycentricPoint:
    """Return the exact isotomic conjugate ``(y z : z x : x y)``."""
    u, v, w = pt
    return (
        sp.expand(v * w),
        sp.expand(w * u),
        sp.expand(u * v),
    )


def evaluate_cubic_at(poly: sp.Expr, pt: BarycentricPoint) -> bool:
    """Return ``True`` iff ``poly`` vanishes identically at ``pt``.

    Reduces the algebraic extensions ``S^2 = S_A S_B + S_B S_C + S_C S_A`` and
    ``r3^2 = 3`` via exact polynomial division in SymPy.

    Args:
        poly: Homogeneous cubic polynomial in ``(x, y, z)``.
        pt: Exact symbolic barycentric coordinates ``(u, v, w)``.

    Returns:
        ``True`` if ``poly(u, v, w) == 0`` identically over ``Q(a, b, c, S, sqrt(3))``.
    """
    assert_no_floats(poly)
    for coord in pt:
        assert_no_floats(coord)

    expr = sp.expand(poly.subs({x: pt[0], y: pt[1], z: pt[2]}))
    if expr == 0:
        return True
    if expr.has(S):
        expr = sp.rem(sp.Poly(expr, S), sp.Poly(S**2 - S2, S)).as_expr()
    if expr.has(r3):
        expr = sp.rem(sp.Poly(expr, r3), sp.Poly(r3**2 - 3, r3)).as_expr()
    return sp.expand(expr) == 0


_X1 = _pt(a, b, c)
_X2 = _pt(1, 1, 1)
_X3 = _pt(a**2 * SA, b**2 * SB, c**2 * SC)
_X4 = _pt(SB * SC, SC * SA, SA * SB)
_X5 = _pt(S2 + SB * SC, S2 + SC * SA, S2 + SA * SB)
_X6 = _pt(a**2, b**2, c**2)
_X7 = _pt(
    (c + a - b) * (a + b - c),
    (a + b - c) * (b + c - a),
    (b + c - a) * (c + a - b),
)
_X8 = _pt(b + c - a, c + a - b, a + b - c)
_X9 = _pt(a * (b + c - a), b * (c + a - b), c * (a + b - c))
_X10 = _pt(b + c, c + a, a + b)
_X11 = _pt(
    (b - c) ** 2 * (b + c - a),
    (c - a) ** 2 * (c + a - b),
    (a - b) ** 2 * (a + b - c),
)
_X13 = _pt(
    (r3 * SB + S) * (r3 * SC + S),
    (r3 * SC + S) * (r3 * SA + S),
    (r3 * SA + S) * (r3 * SB + S),
)
_X14 = _pt(
    (r3 * SB - S) * (r3 * SC - S),
    (r3 * SC - S) * (r3 * SA - S),
    (r3 * SA - S) * (r3 * SB - S),
)
_X15 = _pt(a**2 * (r3 * SA + S), b**2 * (r3 * SB + S), c**2 * (r3 * SC + S))
_X16 = _pt(a**2 * (r3 * SA - S), b**2 * (r3 * SB - S), c**2 * (r3 * SC - S))
_X17 = _pt(
    (SB + r3 * S) * (SC + r3 * S),
    (SC + r3 * S) * (SA + r3 * S),
    (SA + r3 * S) * (SB + r3 * S),
)
_X18 = _pt(
    (SB - r3 * S) * (SC - r3 * S),
    (SC - r3 * S) * (SA - r3 * S),
    (SA - r3 * S) * (SB - r3 * S),
)
_X20 = _pt(a**2 * SA - SB * SC, b**2 * SB - SC * SA, c**2 * SC - SA * SB)
_X30 = _pt(S2 - 3 * SB * SC, S2 - 3 * SC * SA, S2 - 3 * SA * SB)
_X32 = _pt(a**4, b**4, c**4)
_X40 = _pt(
    (a + b + c) * a**2 * SA - S2 * a,
    (a + b + c) * b**2 * SB - S2 * b,
    (a + b + c) * c**2 * SC - S2 * c,
)
_X54 = isogonal_conjugate(_X5)
_X56 = _pt(
    a**2 * (c + a - b) * (a + b - c),
    b**2 * (a + b - c) * (b + c - a),
    c**2 * (b + c - a) * (c + a - b),
)
_X57 = isogonal_conjugate(_X9)
_X64 = isogonal_conjugate(_X20)
_X69 = _pt(SA, SB, SC)
_X84 = isogonal_conjugate(_X40)
_X99 = _pt(
    (c**2 - a**2) * (a**2 - b**2),
    (a**2 - b**2) * (b**2 - c**2),
    (b**2 - c**2) * (c**2 - a**2),
)
_X110 = _pt(
    a**2 * (c**2 - a**2) * (a**2 - b**2),
    b**2 * (a**2 - b**2) * (b**2 - c**2),
    c**2 * (b**2 - c**2) * (c**2 - a**2),
)
_X316 = _pt(
    b**4 + c**4 - a**4 - b**2 * c**2,
    c**4 + a**4 - b**4 - c**2 * a**2,
    a**4 + b**4 - c**4 - a**2 * b**2,
)
_X67 = isotomic_conjugate(_X316)

CENTER_SPECS: dict[str, CenterSpec] = {
    "X1": CenterSpec(1, "X1", "Incenter", _X1),
    "X2": CenterSpec(2, "X2", "Centroid", _X2),
    "X3": CenterSpec(3, "X3", "Circumcenter", _X3),
    "X4": CenterSpec(4, "X4", "Orthocenter", _X4),
    "X5": CenterSpec(5, "X5", "Nine-Point Center", _X5),
    "X6": CenterSpec(6, "X6", "Symmedian Point", _X6),
    "X7": CenterSpec(7, "X7", "Gergonne Point", _X7),
    "X8": CenterSpec(8, "X8", "Nagel Point", _X8),
    "X9": CenterSpec(9, "X9", "Mittenpunkt", _X9),
    "X10": CenterSpec(10, "X10", "Spieker Center", _X10),
    "X11": CenterSpec(11, "X11", "Feuerbach Point", _X11),
    "X13": CenterSpec(13, "X13", "1st Isogonic Center", _X13),
    "X14": CenterSpec(14, "X14", "2nd Isogonic Center", _X14),
    "X15": CenterSpec(15, "X15", "1st Isodynamic Point", _X15),
    "X16": CenterSpec(16, "X16", "2nd Isodynamic Point", _X16),
    "X17": CenterSpec(17, "X17", "1st Napoleon Point", _X17),
    "X18": CenterSpec(18, "X18", "2nd Napoleon Point", _X18),
    "X20": CenterSpec(20, "X20", "de Longchamps Point", _X20),
    "X30": CenterSpec(30, "X30", "Euler Infinity Point", _X30),
    "X32": CenterSpec(32, "X32", "3rd Brocard Point (Power Point)", _X32),
    "X40": CenterSpec(40, "X40", "Bevan Point", _X40),
    "X54": CenterSpec(54, "X54", "Kosnita Point", _X54),
    "X56": CenterSpec(56, "X56", "Exsimilicenter of Circumcircle & Incircle", _X56),
    "X57": CenterSpec(57, "X57", "Isogonal Conjugate of Mittenpunkt", _X57),
    "X64": CenterSpec(64, "X64", "Isogonal Conjugate of X(20)", _X64),
    "X67": CenterSpec(67, "X67", "Isogonal Conjugate of X(51) / Isotomic of X(316)", _X67),
    "X69": CenterSpec(69, "X69", "Symmedian Point of Anticomplementary Triangle", _X69),
    "X84": CenterSpec(84, "X84", "Isogonal Conjugate of Bevan Point", _X84),
    "X99": CenterSpec(99, "X99", "Steiner Point", _X99),
    "X110": CenterSpec(110, "X110", "Focus of Kiepert Parabola", _X110),
    "X316": CenterSpec(316, "X316", "Isotomic Conjugate of X(67)", _X316),
}


def barycentric_to_cartesian(
    pt: BarycentricPoint,
    a_val: float,
    b_val: float,
    c_val: float,
    vertices: tuple[tuple[float, float], tuple[float, float], tuple[float, float]],
) -> tuple[float, float] | None:
    """Convert symbolic barycentric coordinates to 2D Cartesian coordinates for SVG rendering.

    Returns ``None`` if the point lies at infinity (sum of coordinates is zero).

    Args:
        pt: Symbolic barycentric triple ``(x, y, z)``.
        a_val: Numeric side length ``a = |BC|``.
        b_val: Numeric side length ``b = |CA|``.
        c_val: Numeric side length ``c = |AB|``.
        vertices: Cartesian coordinates ``(A, B, C)`` of the reference triangle.

    Returns:
        ``(X, Y)`` Cartesian coordinates, or ``None`` for points at infinity.
    """
    s_half = 0.5 * (a_val + b_val + c_val)
    area = (s_half * (s_half - a_val) * (s_half - b_val) * (s_half - c_val)) ** 0.5
    subs_map = {a: a_val, b: b_val, c: c_val, S: 2.0 * area, r3: 3.0**0.5}
    u = float(pt[0].subs(subs_map))
    v = float(pt[1].subs(subs_map))
    w = float(pt[2].subs(subs_map))
    total = u + v + w
    if abs(total) < 1e-12:
        return None
    (ax, ay), (bx, by), (cx, cy) = vertices
    return ((u * ax + v * bx + w * cx) / total, (u * ay + v * by + w * cy) / total)
