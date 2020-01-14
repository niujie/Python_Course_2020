# Collect string / test length

input = raw_input("Please enter a test string: ")

if len(input) < 6:  # Note the code block indentation
    print("Your string is too short.")
    print("Please enter a string with at least 6 characters.")
