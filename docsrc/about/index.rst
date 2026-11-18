:navigation: header
:order: 10

=====
About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

Exact SymPy toolkit and GEOMETOR catalog for Bernard Gibert's Catalogue of Triangle Cubics (CTC)

Exact symbolic mathematical catalog and cross-corpus concordance inspired by *Catalogue of Triangle Cubics* (Bernard Gibert), structured under :ref:`gibert-catalog` with scholarly apparatus in :ref:`persons` and :ref:`bibliography`.


The GEOMETOR Mission
--------------------

The GEOMETOR project, directed by **phi ARCHITECT**, is dedicated to the systematic recovery, exact formalization, and dynamic re-expression of foundational geometric and philosophical knowledge:

- **Extracting Historical Semantic Knowledge**: Recovering the deductive structure of classical geometric, axiomatic, and philosophical treatises—elevating verbatim primary prose, primary-source folio scans (``publish folio``), and calibrated ``.euclid-graphic`` diagrams into addressable semantic graphs.
- **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (``SymPy``) and Rational Trigonometry invariants over closed-form radical fields.
- **Repurposing Knowledge Across Mediums**: Deploying extracted structures across multi-track **Book Codices**, EPUB 3 editions, computable canons, interactive SVG laboratories, and visual broadcasts.

Sources, Provenance & Repository Architecture
---------------------------------------------

- **Python Package**: ``src/geometor/gibert/`` (Python 3.13)
- **Mathematical Catalog**: ``docsrc/catalog/`` (``:layout: book``)
- **Manifest & Concordance**: ``resources/catalog_manifest.json``, ``resources/concordance.json``
- **Automated Verification**: ``tests/`` (``pytest`` + ``ruff``) and ``docsrc/`` (``publish build``)
