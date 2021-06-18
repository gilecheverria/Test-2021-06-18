"""
Evaluating multiple inputs in a single test

Not the best way, since a single input failure will make all the test fail
"""

import pytest
import src.main

def test_exercise():
    input_values = ["52", "84", "70"]
    output = []

    # This function will store the strings provided to 'input' within the code
    def mock_input(s):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    # Redefinitions of standard functions (input and print) within the module
    # Make sure to use the name of the source file
    # In this case it is 'src.main'
    src.main.input = mock_input
    src.main.print = lambda s : output.append(s)

    # Call the function once for each input value
    num_tests = len(input_values)
    for _ in range(num_tests):
        src.main.main()

    print(f"PYTEST output: {output}")

    # List all the outputs the program will have, including input prompts
    # After the outputs expected comes a message to clarify the error
    assert output == ['Ingresa calificación: ', 'Reprobado', \
                      'Ingresa calificación: ', 'Aprobado', \
                      'Ingresa calificación: ', 'Aprobado', \
                      ], \
            "Incorrect evaluation of the grades"
