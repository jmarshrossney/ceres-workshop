def test_import():
    """Tests that the package is correctly installed."""
    # NOTE: the 'noqa' flag tells flake8 not to complain about unused import
    import ceres_workshop  # noqa: F401
    import ceres_workshop.task_1  # noqa: F401
