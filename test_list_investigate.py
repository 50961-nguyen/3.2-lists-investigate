import inspect
import list_investigate as list_investigate


def test_correct_output(monkeypatch, capsys):
    inputs = ["2", "1"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop())

    list_investigate.main()  # run the program to generate output

    expected = [x**2 for x in range(1, 50)]
    captured = capsys.readouterr()  # capture AFTER output is generated

    assert str(expected) in captured.out


def test_square_numbers_return():
    """Test that square_numbers() returns the correct list of squared values."""
    expected = [x**2 for x in range(1, 50)]
    result = list_investigate.square_numbers()

    assert result == expected, f"Expected {expected}, but got {result}"


def test_header_comments():
    """Test that the module docstring contains required header fields: author and date."""
    source = inspect.getsource(list_investigate)

    assert "author:" in source, "Missing 'author:' in header comments"
    assert "date:" in source, "Missing 'date:' in header comments"