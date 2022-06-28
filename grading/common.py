import pathlib

from flake8.api import legacy as flake8

__all__ = ["lint"]

def lint(*targets):
    style = flake8.get_style_guide()
    report = style.check_files(targets)
    errors = report.get_statistics("E")
    return errors
