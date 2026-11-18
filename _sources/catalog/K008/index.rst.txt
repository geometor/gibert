:type: item
:order: 8
:canonical_id: K008

.. _gibert-k008:

K008 — Droussent Cubic
======================

.. enunciation::

   Circular isotomic pivotal cubic with pole X(2) and pivot X(316) (isotomic conjugate of X(67)).

.. figure:: /_static/svg/K008.svg
   :alt: K008 — Droussent Cubic
   :align: center

   **K008** (*Droussent Cubic*, pK(X2, X316)) on scalene reference triangle :math:`ABC` with circumcircle guide and verified Kimberling centers.

Catalog Metadata & Concordance
------------------------------

.. list-table::
   :widths: 28 72

   * - **Catalog ID**
     - K008
   * - **CTC Notation**
     - pK(X2, X316)
   * - **Conjugacy Class**
     - isotomic
   * - **Pole / Pivot**
     - :ref:`X(2) <etc:x_2>` / :ref:`X(316) <etc:x_316>`
   * - **Exact SymPy Model**
     - :data:`geometor.gibert.K_SERIES_CUBICS` ("K008")
   * - **GEOMETOR Concordance**
     - `geometor/etc <https://geometor.github.io/etc/>`_, `geometor/elements <https://geometor.github.io/elements/>`_

Homogeneous Barycentric Equation
--------------------------------

.. math::

   \sum_{\text{cyc}} \left(b^4 + c^4 - a^4 - b^2 c^2\right) x \left(y^2 - z^2\right) = 0

Verified Kimberling Center Incidences
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Center
     - Name
     - Symbolic Check
   * - :ref:`X(2) <etc:x_2>`
     - Centroid
     - Verified (exact 0)
   * - :ref:`X(67) <etc:x_67>`
     - Isogonal Conjugate of X(51) / Isotomic of X(316)
     - Verified (exact 0)
   * - :ref:`X(316) <etc:x_316>`
     - Isotomic Conjugate of X(67)
     - Verified (exact 0)
