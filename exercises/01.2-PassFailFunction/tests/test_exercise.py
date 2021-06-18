"""
Evaluating the results of a function

Much simpler to implement, but still marks the single test as failed
if one case is wrong
"""

import pytest
from src.main import check_grade


def test_function_1():
    assert check_grade(53) == 'Reprobado', "Grades below 70 should fail"
    assert check_grade(86) == 'Aprobado', "Grades greater than 70 should pass"
    assert check_grade(70) == 'Aprobado', "Grades equal to 70 should pass"
