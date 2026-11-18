:type: item
:order: 11
:canonical_id: K011

.. _gibert-k011:

K011 — Tucker Cubic
===================

.. enunciation::

   Original Tucker cubic: locus of points M whose cevian triangle has the same signed area as the orthic triangle of ABC.

.. figure:: /_static/svg/K011.svg
   :alt: K011 — Tucker Cubic
   :align: center

   **K011** (*Tucker Cubic*, Tucker) on scalene reference triangle :math:`ABC` with circumcircle guide and verified Kimberling centers.

Catalog Metadata & Concordance
------------------------------

.. list-table::
   :widths: 28 72

   * - **Catalog ID**
     - K011
   * - **CTC Notation**
     - Tucker
   * - **Conjugacy Class**
     - general
   * - **Pole / Pivot**
     - — / —
   * - **Exact SymPy Model**
     - :data:`geometor.gibert.K_SERIES_CUBICS` ("K011")
   * - **GEOMETOR Concordance**
     - `geometor/etc <https://geometor.github.io/etc/>`_, `geometor/elements <https://geometor.github.io/elements/>`_

Homogeneous Barycentric Equation
--------------------------------

.. math::

   a^2 b^2 c^2 x y z - S_A S_B S_C (y + z)(z + x)(x + y) = 0

Verified Kimberling Center Incidences
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Center
     - Name
     - Symbolic Check
   * - :ref:`X(4) <etc:x_4>`
     - Orthocenter
     - Verified (exact 0)
   * - :ref:`X(69) <etc:x_69>`
     - Symmedian Point of Anticomplementary Triangle
     - Verified (exact 0)
