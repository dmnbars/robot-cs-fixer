import formatter.capitalizer


def test_simple_capitalizer():
    assert "Test Keyword Capitalized Correctly" == formatter.capitalizer.simple_capitalize("test keyWorD CAPITALIZED Correctly")


def test_only_first_capitalizer():
    assert "Test KeyWorD CAPITALIZED Correctly" == formatter.capitalizer.only_first_capitalizer("test keyWorD CAPITALIZED Correctly")


def test_first_letter_to_upper():
    assert "TeSt" == formatter.capitalizer.first_letter_to_upper("teSt")
