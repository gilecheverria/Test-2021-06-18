# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["0", "0"],
    ["0", "10"],
    ["5.8", "0"],
    ["3.2", "2"],
    ["-1", "4"],
    ["-3", "-0.3"],
    ["6.2", "-4"],
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
        ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: Origin"],
        ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: Y axis"],
        ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: X axis"],
        ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: I"],
        ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: II"],
        ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: III"],
        ["Enter X coordinate of the point: ", "Enter Y coordinate of the point: ", "The point is in quadrant: IV"],
    ]

# List of hints for each test, in case of an error
error_messages = [
        'Both coordinates are at 0',
        'X is equal to 0',
        'Y is equal to 0',
        'First quadrant',
        'Second quadrant',
        'Third quadrant',
        'Fourth quadrant',
        ]
