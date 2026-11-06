"""Python Readiness Test

Complete the 4 functions below so that each does what its description says.
Replace the line `raise NotImplementedError` with your own code.

- Use only plain Python: no pandas, no other packages.
- Keep the function names and parameters exactly as they are.
- Check your work with:  pytest
- Then commit and push (see README.md).
"""


# Task 1: decisions (if / elif / else)
def classify_amount(amount):
    """Return a risk band for a transaction amount (a number).

    - "High"   if amount is 10,000 or more
    - "Medium" if amount is 1,000 or more, but less than 10,000
    - "Low"    otherwise

    classify_amount(15000)  -> "High"
    classify_amount(1000)   -> "Medium"
    classify_amount(250.5)  -> "Low"
    """
    raise NotImplementedError


# Task 2: loops, tuples and dictionaries
def total_by_type(transactions):
    """Add up amounts by transaction type.

    transactions is a list of (type, amount) tuples. Return a dictionary
    mapping each type to its total.

    total_by_type([("card", 120), ("transfer", 500), ("card", 80)])
        -> {"card": 200, "transfer": 500}
    total_by_type([])  -> {}
    """
    raise NotImplementedError


# Task 3: handling errors (try / except)
def parse_amount(text):
    """Turn text such as "1,250.50" into a float.

    Return None if it is not a number.

    - Remove commas, and spaces at either end, before converting.
    - Don't let the program crash on bad input: catch the error instead.

    parse_amount("1,250.50")  -> 1250.5
    parse_amount(" 300 ")     -> 300.0
    parse_amount("n/a")       -> None
    """
    raise NotImplementedError


# Task 4: reading a file
def read_amounts(path):
    """Read a text file with one amount per line.

    Return the valid amounts as a list of floats.

    Skip lines that are blank or are not numbers: use parse_amount from
    Task 3.
    Open the file with a `with` block.

    For a file containing the lines "100", "1,200.50", "", "unknown", "75":
        read_amounts(path) -> [100.0, 1200.5, 75.0]
    """
    raise NotImplementedError
