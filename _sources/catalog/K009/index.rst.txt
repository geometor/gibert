:type: item
:order: 9
:canonical_id: K009

.. _gibert-k009:

K009 — Lemoine Cubic
====================

.. enunciation::

   Nodal cubic with perpendicular nodal tangents at X(3): locus of points M whose cevians MA, MB, MC meet the perpendicular bisectors of BC, CA, AB in three collinear points.

.. figure:: /_static/svg/K009.svg
   :alt: K009 — Lemoine Cubic
   :align: center

   **K009** (*Lemoine Cubic*, K(O)) on scalene reference triangle :math:`ABC` with circumcircle guide and verified Kimberling centers.

Catalog Metadata & Concordance
------------------------------

.. list-table::
   :widths: 28 72

   * - **Catalog ID**
     - K009
   * - **CTC Notation**
     - K(O)
   * - **Conjugacy Class**
     - general
   * - **Pole / Pivot**
     - — / —
   * - **Exact SymPy Model**
     - :data:`geometor.gibert.K_SERIES_CUBICS` ("K009")
   * - **GEOMETOR Concordance**
     - `geometor/etc <https://geometor.github.io/etc/>`_, `geometor/elements <https://geometor.github.io/elements/>`_

Homogeneous Barycentric Equation
--------------------------------

.. math::

   \sum_{\text{cyc}} a^4 S_A \, y z (y - z) + (a^2 - b^2)(b^2 - c^2)(c^2 - a^2) x y z = 0

Verified Kimberling Center Incidences
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Center
     - Name
     - Symbolic Check
   * - :ref:`X(3) <etc:x_3>`
     - Circumcenter
     - Verified (exact 0)
   * - :ref:`X(4) <etc:x_4>`
     - Orthocenter
     - Verified (exact 0)
   * - :ref:`X(32) <etc:x_32>`
     - 3rd Brocard Point (Power Point)
     - Verified (exact 0)
   * - :ref:`X(56) <etc:x_56>`
     - Exsimilicenter of Circumcircle & Incircle
     - Verified (exact 0)
