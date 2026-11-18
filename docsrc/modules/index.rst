:navigation: header
:order: 90

=======
Modules
=======

API summary for ``geometor.gibert``:

- :mod:`geometor.gibert` — Public package interface exporting ``__version__`` and :func:`~geometor.gibert.app.run`.
- :mod:`geometor.gibert.app` — Command-line parser (:func:`~geometor.gibert.app.build_parser`) and entry point (:func:`~geometor.gibert.app.main`).
- :mod:`geometor.gibert.catalog` — Typed catalog manifest descriptor (:class:`~geometor.gibert.catalog.CatalogEntrySpec`), loader (:func:`~geometor.gibert.catalog.load_catalog_manifest`), and exact-algebra guard (:func:`~geometor.gibert.catalog.assert_no_floats`).
