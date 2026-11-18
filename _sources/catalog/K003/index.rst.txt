:type: item
:order: 3
:canonical_id: K003

.. _gibert-k003:

K003 — McCay Cubic
==================

.. enunciation::

   Isogonal pivotal cubic with pole X(6) and pivot X(3) (circumcenter): locus of points M such that M, its isogonal conjugate M*, and X(3) are collinear; its three real asymptotes concur at X(2) making pairwise angles of 60 degrees.

.. figure:: /_static/svg/K003.svg
   :alt: K003 — McCay Cubic
   :align: center

   **K003** (*McCay Cubic*, pK(X6, X3)) on scalene reference triangle :math:`ABC` with circumcircle guide and verified Kimberling centers.

Catalog Metadata & Concordance
------------------------------

.. list-table::
   :widths: 28 72

   * - **Catalog ID**
     - K003
   * - **CTC Notation**
     - pK(X6, X3)
   * - **Conjugacy Class**
     - isogonal
   * - **Pole / Pivot**
     - :ref:`X(6) <etc:x_6>` / :ref:`X(3) <etc:x_3>`
   * - **Exact SymPy Model**
     - :data:`geometor.gibert.K_SERIES_CUBICS` ("K003")
   * - **GEOMETOR Concordance**
     - `geometor/etc <https://geometor.github.io/etc/>`_, `geometor/elements <https://geometor.github.io/elements/>`_

Homogeneous Barycentric Equation
--------------------------------

.. math::

   \sum_{\text{cyc}} a^2 S_A \, x \left(c^2 y^2 - b^2 z^2\right) = 0

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
