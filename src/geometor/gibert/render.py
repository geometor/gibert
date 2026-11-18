"""Theme-adaptive ``.euclid-graphic`` SVG renderer for K-series triangle cubics."""

from __future__ import annotations

import math
from pathlib import Path

import sympy as sp

from .centers import CENTER_SPECS, a, b, barycentric_to_cartesian, c, x, y, z
from .cubics import K_SERIES_CUBICS, CubicSpec

__all__ = [
    "DEFAULT_SVG_DIR",
    "render_all_cubics",
    "render_cubic_svg",
]

DEFAULT_SVG_DIR = Path(__file__).resolve().parents[3] / "docsrc" / "_static" / "svg"

# Scalene acute reference triangle: B=(0, 0), C=(6, 0), A=(1.8, 4.5)
_VERTICES = ((1.8, 4.5), (0.0, 0.0), (6.0, 0.0))
_X_MIN, _X_MAX = -3.5, 9.5
_Y_MIN, _Y_MAX = -3.5, 8.0


def _triangle_sides(
    verts: tuple[tuple[float, float], tuple[float, float], tuple[float, float]],
) -> tuple[float, float, float]:
    (ax, ay), (bx, by), (cx, cy) = verts
    a_val = math.hypot(cx - bx, cy - by)
    b_val = math.hypot(ax - cx, ay - cy)
    c_val = math.hypot(bx - ax, by - ay)
    return a_val, b_val, c_val


def _marching_squares(
    grid: list[list[float]],
    xs: list[float],
    ys: list[float],
) -> list[tuple[tuple[float, float], tuple[float, float]]]:
    """Extract zero-contour segments on a 2D scalar grid."""
    segments: list[tuple[tuple[float, float], tuple[float, float]]] = []
    ny = len(ys) - 1
    nx = len(xs) - 1

    def interp(
        x1: float, y1: float, v1: float, x2: float, y2: float, v2: float
    ) -> tuple[float, float]:
        denom = v1 - v2
        if abs(denom) < 1e-18:
            return (0.5 * (x1 + x2), 0.5 * (y1 + y2))
        t = v1 / denom
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

    for j in range(ny):
        y0, y1 = ys[j], ys[j + 1]
        row0, row1 = grid[j], grid[j + 1]
        for i in range(nx):
            x0, x1 = xs[i], xs[i + 1]
            v00 = row0[i]
            v10 = row0[i + 1]
            v11 = row1[i + 1]
            v01 = row1[i]

            pts: list[tuple[float, float]] = []
            if (v00 >= 0) != (v10 >= 0):
                pts.append(interp(x0, y0, v00, x1, y0, v10))
            if (v10 >= 0) != (v11 >= 0):
                pts.append(interp(x1, y0, v10, x1, y1, v11))
            if (v11 >= 0) != (v01 >= 0):
                pts.append(interp(x1, y1, v11, x0, y1, v01))
            if (v01 >= 0) != (v00 >= 0):
                pts.append(interp(x0, y1, v01, x0, y0, v00))

            if len(pts) == 2:
                segments.append((pts[0], pts[1]))
            elif len(pts) == 4:
                segments.append((pts[0], pts[1]))
                segments.append((pts[2], pts[3]))
    return segments


def _stitch_segments(
    segments: list[tuple[tuple[float, float], tuple[float, float]]],
) -> list[list[tuple[float, float]]]:
    """Chain adjacent segments into continuous polylines for compact SVG paths."""
    if not segments:
        return []

    def key(pt: tuple[float, float]) -> tuple[int, int]:
        return (round(pt[0] * 10000), round(pt[1] * 10000))

    adj: dict[tuple[int, int], list[int]] = {}
    for idx, (p0, p1) in enumerate(segments):
        adj.setdefault(key(p0), []).append(idx)
        adj.setdefault(key(p1), []).append(idx)

    used = [False] * len(segments)
    polylines: list[list[tuple[float, float]]] = []

    for start_idx in range(len(segments)):
        if used[start_idx]:
            continue
        used[start_idx] = True
        p0, p1 = segments[start_idx]
        chain = [p0, p1]

        # Extend forward from chain[-1]
        while True:
            k = key(chain[-1])
            nxt = next((i for i in adj.get(k, []) if not used[i]), None)
            if nxt is None:
                break
            used[nxt] = True
            q0, q1 = segments[nxt]
            chain.append(q1 if key(q0) == k else q0)

        # Extend backward from chain[0]
        while True:
            k = key(chain[0])
            nxt = next((i for i in adj.get(k, []) if not used[i]), None)
            if nxt is None:
                break
            used[nxt] = True
            q0, q1 = segments[nxt]
            chain.insert(0, q1 if key(q0) == k else q0)

        polylines.append(chain)
    return polylines


def _circumcircle(
    verts: tuple[tuple[float, float], tuple[float, float], tuple[float, float]],
) -> tuple[float, float, float]:
    (ax, ay), (bx, by), (cx, cy) = verts
    d = 2.0 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = (
        (ax * ax + ay * ay) * (by - cy)
        + (bx * bx + by * by) * (cy - ay)
        + (cx * cx + cy * cy) * (ay - by)
    ) / d
    uy = (
        (ax * ax + ay * ay) * (cx - bx)
        + (bx * bx + by * by) * (ax - cx)
        + (cx * cx + cy * cy) * (bx - ax)
    ) / d
    r = math.hypot(ax - ux, ay - uy)
    return ux, uy, r


def render_cubic_svg(spec: CubicSpec, output_path: Path | None = None, grid_n: int = 200) -> Path:
    """Render a theme-adaptive ``.euclid-graphic`` SVG for a K-series cubic.

    Args:
        spec: Cubic specification from :data:`K_SERIES_CUBICS`.
        output_path: Destination SVG file path. Defaults to ``docsrc/_static/svg/<id>.svg``.
        grid_n: Grid resolution per axis for contour extraction.

    Returns:
        Path to the written SVG file.
    """
    target = output_path or (DEFAULT_SVG_DIR / f"{spec.id}.svg")
    target.parent.mkdir(parents=True, exist_ok=True)

    a_val, b_val, c_val = _triangle_sides(_VERTICES)
    (ax, ay), (bx, by), (cx, cy) = _VERTICES

    poly_num = spec.polynomial.subs({a: a_val, b: b_val, c: c_val})
    fn = sp.lambdify((x, y, z), poly_num, modules="math")

    # Signed area 2*Delta for Cartesian -> barycentric conversion
    det_t = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)

    xs = [_X_MIN + (_X_MAX - _X_MIN) * i / grid_n for i in range(grid_n + 1)]
    ys = [_Y_MIN + (_Y_MAX - _Y_MIN) * j / grid_n for j in range(grid_n + 1)]

    grid: list[list[float]] = []
    for py in ys:
        row: list[float] = []
        for px in xs:
            u = ((bx - px) * (cy - py) - (cx - px) * (by - py)) / det_t
            v = ((cx - px) * (ay - py) - (ax - px) * (cy - py)) / det_t
            w = 1.0 - u - v
            row.append(float(fn(u, v, w)))
        grid.append(row)

    segments = _marching_squares(grid, xs, ys)
    polylines = _stitch_segments(segments)

    vb_x = _X_MIN
    vb_y = -_Y_MAX
    vb_w = _X_MAX - _X_MIN
    vb_h = _Y_MAX - _Y_MIN

    ox, oy, rad = _circumcircle(_VERTICES)

    path_elems: list[str] = []
    for chain in polylines:
        d_parts = [f"M {chain[0][0]:.4f} {-chain[0][1]:.4f}"]
        for px, py in chain[1:]:
            d_parts.append(f"L {px:.4f} {-py:.4f}")
        path_elems.append(f'    <path class="cubic-curve" d="{" ".join(d_parts)}" />')

    center_elems: list[str] = []
    label_elems: list[str] = []
    for code in spec.claimed_centers:
        c_spec = CENTER_SPECS[code]
        pt_xy = barycentric_to_cartesian(c_spec.barycentric, a_val, b_val, c_val, _VERTICES)
        if pt_xy is None:
            continue
        px, py = pt_xy
        if not (_X_MIN + 0.3 <= px <= _X_MAX - 0.3 and _Y_MIN + 0.3 <= py <= _Y_MAX - 0.3):
            continue
        center_elems.append(
            f'    <circle class="center-point" cx="{px:.4f}" cy="{-py:.4f}" r="0.11">'
            f"<title>{code}: {c_spec.name}</title></circle>"
        )
        label_elems.append(
            f'    <text class="center-label" x="{px + 0.16:.4f}" y="{-py - 0.14:.4f}">'
            f"{code}</text>"
        )

    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
        (
            f'<svg class="euclid-graphic" xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{vb_x:.2f} {vb_y:.2f} {vb_w:.2f} {vb_h:.2f}" '
            f'preserveAspectRatio="xMidYMid meet">'
        ),
        "  <style>",
        "    :root {",
        "      --background-color: #121212;",
        "      --text-color: #e0e0e0;",
        "      --accent-color: #161616;",
        "      --border-color: #333333;",
        "      --select-color: #00e5ff;",
        "    }",
        "    svg.euclid-graphic {",
        "      width: 100%;",
        "      height: auto;",
        "      max-height: 520px;",
        "      background-color: var(--accent-color);",
        "      border: 1px solid var(--border-color);",
        "      border-radius: 4px;",
        "      display: block;",
        "    }",
        "    .guide {",
        "      fill: none;",
        "      stroke: var(--border-color);",
        "      stroke-width: 1.2;",
        "      stroke-dasharray: 4 4;",
        "      vector-effect: non-scaling-stroke;",
        "    }",
        "    .triangle {",
        "      fill: none;",
        "      stroke: var(--text-color);",
        "      stroke-width: 1.8;",
        "      vector-effect: non-scaling-stroke;",
        "      opacity: 0.75;",
        "    }",
        "    .cubic-curve {",
        "      fill: none;",
        "      stroke: var(--select-color);",
        "      stroke-width: 2.2;",
        "      stroke-linecap: round;",
        "      stroke-linejoin: round;",
        "      vector-effect: non-scaling-stroke;",
        "    }",
        "    .vertex-point {",
        "      fill: #66ff66;",
        "      stroke: var(--background-color);",
        "      stroke-width: 1.5;",
        "      vector-effect: non-scaling-stroke;",
        "    }",
        "    .center-point {",
        "      fill: #ffaa33;",
        "      stroke: var(--background-color);",
        "      stroke-width: 1.5;",
        "      vector-effect: non-scaling-stroke;",
        "    }",
        "    .vertex-label, .center-label {",
        "      font-family: system-ui, -apple-system, sans-serif;",
        "      font-size: 0.42px;",
        "      font-weight: 600;",
        "      fill: var(--text-color);",
        "    }",
        "    .center-label {",
        "      fill: #ffcc77;",
        "    }",
        "  </style>",
        '  <g id="guides">',
        f'    <circle class="guide" cx="{ox:.4f}" cy="{-oy:.4f}" r="{rad:.4f}" />',
        (
            f'    <polygon class="triangle" '
            f'points="{ax:.4f},{-ay:.4f} {bx:.4f},{-by:.4f} {cx:.4f},{-cy:.4f}" />'
        ),
        "  </g>",
        '  <g id="cubic">',
        *path_elems,
        "  </g>",
        '  <g id="points">',
        f'    <circle class="vertex-point" cx="{ax:.4f}" cy="{-ay:.4f}" r="0.12" />',
        f'    <circle class="vertex-point" cx="{bx:.4f}" cy="{-by:.4f}" r="0.12" />',
        f'    <circle class="vertex-point" cx="{cx:.4f}" cy="{-cy:.4f}" r="0.12" />',
        *center_elems,
        "  </g>",
        '  <g id="labels">',
        f'    <text class="vertex-label" x="{ax - 0.12:.4f}" y="{-ay - 0.22:.4f}">A</text>',
        f'    <text class="vertex-label" x="{bx - 0.45:.4f}" y="{-by + 0.40:.4f}">B</text>',
        f'    <text class="vertex-label" x="{cx + 0.18:.4f}" y="{-cy + 0.40:.4f}">C</text>',
        *label_elems,
        "  </g>",
        "</svg>",
        "",
    ]

    target.write_text("\n".join(svg_lines), encoding="utf-8")
    return target


def render_all_cubics(output_dir: Path | None = None) -> list[Path]:
    """Render SVG diagrams for all registered K-series cubics.

    Args:
        output_dir: Optional directory override for generated SVGs.

    Returns:
        List of paths to the generated SVG files.
    """
    base = output_dir or DEFAULT_SVG_DIR
    return [render_cubic_svg(spec, base / f"{spec.id}.svg") for spec in K_SERIES_CUBICS.values()]
