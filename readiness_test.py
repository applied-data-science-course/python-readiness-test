"""Python Readiness Test

Complete each function below so that it does what its description says.
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


# Task 2: functions with default values
def monthly_fee(balance, rate=0.01, minimum=2.0):
    """Return the monthly account fee.

    The fee is balance * rate, but never less than minimum.
    Round the result to 2 decimal places.

    monthly_fee(5000)               -> 50.0
    monthly_fee(100)                -> 2.0    (1.0 is below the minimum)
    monthly_fee(5000, rate=0.005)   -> 25.0
    """
    raise NotImplementedError


# Task 3: loops that stop early
def first_over_limit(amounts, limit):
    """Return the position (index) of the first amount greater than limit.

    Stop looking as soon as you find one. Return -1 if no amount is over the limit.

    first_over_limit([200, 450, 9000, 300, 12000], 5000)  -> 2
    first_over_limit([200, 450], 5000)                    -> -1
    """
    raise NotImplementedError


# Task 4: tuples and dictionaries
def total_by_type(transactions):
    """Add up amounts by transaction type.

    transactions is a list of (type, amount) tuples. Return a dictionary
    mapping each type to its total.

    total_by_type([("card", 120), ("transfer", 500), ("card", 80)])
        -> {"card": 200, "transfer": 500}
    total_by_type([])  -> {}
    """
    raise NotImplementedError


# Task 5: sets
def branches_in_common(branches_a, branches_b):
    """Return the branches that appear in BOTH lists, as a sorted list with no repeats.

    branches_in_common(["Orchard", "Jurong", "Orchard"], ["Jurong", "Tampines", "Orchard"])
        -> ["Jurong", "Orchard"]
    """
    raise NotImplementedError


# Task 6: handling errors (try / except)
def parse_amount(text):
    """Turn text such as "1,250.50" into a float. Return None if it is not a number.

    - Remove commas and spaces at either end before converting.
    - Do not let the program crash on bad input: catch the error instead.

    parse_amount("1,250.50")  -> 1250.5
    parse_amount(" 300 ")     -> 300.0
    parse_amount("n/a")       -> None
    parse_amount("")          -> None
    """
    raise NotImplementedError


# Task 7: reading a file
def read_amounts(path):
    """Read a text file with one amount per line and return the valid amounts as a list of floats.

    Skip lines that are blank or are not numbers. Use parse_amount from Task 6.
    Open the file with a `with` block.

    For a file containing the lines  "100", "1,200.50", "", "unknown", "75"
        read_amounts(path) -> [100.0, 1200.5, 75.0]
    """
    raise NotImplementedError


# Task 8: writing a file
def write_summary(path, totals):
    """Write totals (a dictionary of type -> total) to a text file, one line per type.

    - Each line looks like:  card: 200.00
    - Lines are in alphabetical order of type.
    - Totals always show 2 decimal places.
    - Open the file with a `with` block.

    write_summary("summary.txt", {"transfer": 500, "card": 200})
    creates summary.txt containing:
        card: 200.00
        transfer: 500.00
    """
    raise NotImplementedError
