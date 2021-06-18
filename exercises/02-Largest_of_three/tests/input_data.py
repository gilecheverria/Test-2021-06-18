# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["5", "3", "8"],
    ["2", "4", "8"],
    ["5", "3", "1"],
    ["5", "3", "4"],
    ["2", "6", "1"],
    ["5", "6", "3"],
    ["2", "2", "2"],
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
        ["Enter first number: ", "Enter second number: ", "Enter third number: ", 8],
        ["Enter first number: ", "Enter second number: ", "Enter third number: ", 8],
        ["Enter first number: ", "Enter second number: ", "Enter third number: ", 5],
        ["Enter first number: ", "Enter second number: ", "Enter third number: ", 5],
        ["Enter first number: ", "Enter second number: ", "Enter third number: ", 6],
        ["Enter first number: ", "Enter second number: ", "Enter third number: ", 6],
        ["Enter first number: ", "Enter second number: ", "Enter third number: ", 2],
    ]

# List of hints for each test, in case of an error
error_messages = [
        "Last number is the largest",
        "Last number is the largest",
        "First number is the largest",
        "First number is the largest",
        "Second number is the largest",
        "Second number is the largest",
        "All numbers are equal",
        ]
