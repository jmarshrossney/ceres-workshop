"""Grades task 1."""
import pathlib
from pprint import pprint

from flake8.api import legacy as flake8

import ceres_workshop.task_1 as task_1
from .common import *


def grade_lint():
    task_1_path = pathlib.Path(task_1.__file__).parent
    errors = lint(task_1_path)
    assert not errors, f"Flake8 found {len(errors)} errors!"
