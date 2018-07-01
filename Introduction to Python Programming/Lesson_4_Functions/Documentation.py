# Quiz: Write a Docstring
# Write a docstring for the readable_timedelta function you defined earlier! Remember the way you write your docstrings
# is pretty flexible! Looks through Python's docstring conventions here and check out this Stack Overflow page for some
# inspiration!

def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days

    Args:
    days: number of days to convert(int)

    Returns:
    string of the number of weeks and days included in days
    """
     weeks = days // 7
     remainder = days % 7
     return "{} week(s) and {} day(s)".format(weeks, remainder)

