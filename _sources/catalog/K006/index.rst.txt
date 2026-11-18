:type: item
:order: 6
:canonical_id: K006

.. _gibert-k006:

K006 — Orthocubic
=================

.. enunciation::

   Isogonal pivotal cubic with pole X(6) and pivot X(4) (orthocenter): locus of points M such that M, its isogonal conjugate M*, and X(4) are collinear.

.. figure:: /_static/svg/K006.svg
   :alt: K006 — Orthocubic
   :align: center

   **K006** (*Orthocubic*, pK(X6, X4)) on scalene reference triangle :math:`ABC` with circumcircle guide and verified Kimberling centers.

Catalog Metadata & Concordance
------------------------------

.. list-table::
   :widths: 28 72

   * - **Catalog ID**
     - K006
   * - **CTC Notation**
     - pK(X6, X4)
   * - **Conjugacy Class**
     - isogonal
   * - **Pole / Pivot**
     - :ref:`X(6) <etc:x_6>` / :ref:`X(4) <etc:x_4>`
   * - **Exact SymPy Model**
     - :data:`geometor.gibert.K_SERIES_CUBICS` ("K006")
   * - **GEOMETOR Concordance**
     - `geometor/etc <https://geometor.github.io/etc/>`_, `geometor/elements <https://geometor.github.io/elements/>`_

Homogeneous Barycentric Equation
--------------------------------

.. math::

   \sum_{\text{cyc}} S_B S_C \, x \left(c^2 y^2 - b^2 z^2\right) = 0

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
