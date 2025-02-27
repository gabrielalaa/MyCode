def add(x, y):
    return x + y


def test_my_first_test_add():
    assert (add(2, 3) == 5)


########################################
def convert_seconds_to_hours(seconds):
    return seconds / 3600


# NEVER DO THIS
def test_seconds_to_hours():
    assert (convert_seconds_to_hours(3600) == 1)
    assert (convert_seconds_to_hours(-1) == -1 / 3600)
    # assert (convert_seconds_to_hours(0), 0)
    # assert (convert_seconds_to_hours('cat'))
    assert (convert_seconds_to_hours(42.43) == 42.43 / 3600)


##############################################################
# function to be tested
def capital_case(x):
    if 97 <= ord(x) <= 97 + 26:
        return chr(ord(x) - ord('a') + ord('A'))
    return x


def test_capital_case():
    assert (capital_case('a') == 'A')
    assert (capital_case('A') == 'A')
    assert (capital_case('2') == '2')
    assert (capital_case('#') == '#')