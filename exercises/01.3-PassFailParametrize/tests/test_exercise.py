"""
Evaluating the results of a function

Using Python decorators and parametrize to add multiple independent tests
This allows each test to be evaluated independently
"""

import pytest
from src.main import check_grade

# Decorator to indicate the arguments to the test function
@pytest.mark.parametrize('grade, result, message',
                            # The input, output and message in case of failure
                            [(53, 'Reprobado', 'Less than 70 should fail'),
                             (86, 'Aprobado', 'More than 70 should pass'),
                             (70, 'Aprobado', 'Grade 70 should pass')])
# Simple function to run all the asserts
def test_function(grade, result, message):
    assert check_grade(grade) == result, message
