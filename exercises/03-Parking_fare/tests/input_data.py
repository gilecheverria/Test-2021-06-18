# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["0", "0"],
    ["0", "10"],
    ["1", "40"],
    ["2", "30"],
    ["3", "1"],
    ["3", "20"],
    ["4", "31"],
    ["6", "50"],
    ]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
        ["Enter number of hours: ", "Enter number of minutes: ", 0],
        ["Enter number of hours: ", "Enter number of minutes: ", 5],
        ["Enter number of hours: ", "Enter number of minutes: ", 5],
        ["Enter number of hours: ", "Enter number of minutes: ", 17],
        ["Enter number of hours: ", "Enter number of minutes: ", 22],
        ["Enter number of hours: ", "Enter number of minutes: ", 25],
        ["Enter number of hours: ", "Enter number of minutes: ", 39],
        ["Enter number of hours: ", "Enter number of minutes: ", 65],
    ]

# List of hints for each test, in case of an error
error_messages = [
        'Pay $0 if there is no time',
        'Pay $5 for the first 2 hours',
        'Pay $5 for the first 2 hours',
        'During the third hour, pay $ 5 + 12',
        'For 3:01, pay $ 5 + 12 + 5',
        'For 3:20, pay $ 5 + 12 + 5 + 3',
        'For 4:31, pay $ 5 + 12 + 12 + 5 + 3 + 2',
        'For 4:31, pay $ 5 + 12 + 12 + 12 + 12 + 5 + 3 + 2 + 2',
        ]
