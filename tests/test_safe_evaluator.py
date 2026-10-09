import pytest
from safe_evaluator import safe_eval

def test_valid_expressions():
    assert safe_eval("4 * 12") == 48
    assert safe_eval("10 + 5") == 15
    assert safe_eval("20 - 8") == 12
    assert safe_eval("20 / 4") == 5
    assert safe_eval("(10 + 5) * 2") == 30
    assert safe_eval("-5 + 10") == 5

def test_unsafe_expressions():
    with pytest.raises(ValueError):
        safe_eval("__import__('os')")

    with pytest.raises(ValueError):
        safe_eval("open('x')")

    with pytest.raises(ValueError):
        safe_eval("x + 5")

    with pytest.raises(ValueError):
        safe_eval("value.real")

    with pytest.raises(ValueError):
        safe_eval("2 ** 3")

def test_invalid_inputs():
    with pytest.raises(ValueError):
        safe_eval("")

    with pytest.raises(ValueError):
        safe_eval(123)

    with pytest.raises(ValueError):
        safe_eval("10 / 0")

def test_length_limit():
    with pytest.raises(ValueError, match="too long"):
        safe_eval("1+" * 100)

def test_depth_limit():
    with pytest.raises(ValueError, match="Depth limit"):
        safe_eval("-" * 25 + "1")
