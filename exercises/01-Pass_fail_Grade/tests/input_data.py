# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["56"],
    ["69"],
    ["82"],
    ["70"],
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
        ["Enter grade: ", "Fail"],
        ["Enter grade: ", "Fail"],
        ["Enter grade: ", "Pass"],
        ["Enter grade: ", "Pass"],
    ]

# List of hints for each test, in case of an error
error_messages = [
        "Less than 70 fails",
        "Less than 70 fails",
        "More than 70 passes",
        "Exactly 70 passes",
        ]
