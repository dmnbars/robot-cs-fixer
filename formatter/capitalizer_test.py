import formatter.capitalizer


def test_simple_capitalizer():
    assert "Test Keyword Capitalized Correctly" == formatter.capitalizer.simple_capitalize("test keyWorD CAPITALIZED Correctly")
