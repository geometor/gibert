:type: item
:order: 4
:canonical_id: K004

.. _gibert-k004:

K004 — Darboux Cubic
====================

.. enunciation::

   Isogonal pivotal cubic with pole X(6) and pivot X(20) (de Longchamps point): central at X(3) and locus of points M whose pedal triangle is a cevian triangle.

.. figure:: /_static/svg/K004.svg
   :alt: K004 — Darboux Cubic
   :align: center

   **K004** (*Darboux Cubic*, pK(X6, X20)) on scalene reference triangle :math:`ABC` with circumcircle guide and verified Kimberling centers.

Catalog Metadata & Concordance
------------------------------

.. list-table::
   :widths: 28 72

   * - **Catalog ID**
     - K004
   * - **CTC Notation**
     - pK(X6, X20)
   * - **Conjugacy Class**
     - isogonal
   * - **Pole / Pivot**
     - :ref:`X(6) <etc:x_6>` / :ref:`X(20) <etc:x_20>`
   * - **Exact SymPy Model**
     - :data:`geometor.gibert.K_SERIES_CUBICS` ("K004")
   * - **GEOMETOR Concordance**
     - `geometor/etc <https://geometor.github.io/etc/>`_, `geometor/elements <https://geometor.github.io/elements/>`_

Homogeneous Barycentric Equation
--------------------------------

.. math::

   \sum_{\text{cyc}} \left(a^2 S_A - S_B S_C\right) x \left(c^2 y^2 - b^2 z^2\right) = 0

Verified Kimberling Center Incidences
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Center
     - Name
     - Symbolic Check
   * - :ref:`X(1) <etc:x_1>`
     - Incenter
     - Verified (exact 0)
   * - :ref:`X(3) <etc:x_3>`
     - Circumcenter
     - Verified (exact 0)
   * - :ref:`X(4) <etc:x_4>`
     - Orthocenter
     - Verified (exact 0)
   * - :ref:`X(20) <etc:x_20>`
     - de Longchamps Point
     - Verified (exact 0)
   * - :ref:`X(40) <etc:x_40>`
     - Bevan Point
     - Verified (exact 0)
   * - :ref:`X(64) <etc:x_64>`
     - Isogonal Conjugate of X(20)
     - Verified (exact 0)
   * - :ref:`X(84) <etc:x_84>`
     - Isogonal Conjugate of Bevan Point
     - Verified (exact 0)
