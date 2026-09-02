import pytest

def hi(name: str) -> str:
    return f"Hello, {name}!"

def test_hi_returns_correct_greeting():
    assert hi("Alice") == "Hello, Alice!"
    assert hi("Bob") == "Hello, Bob!"

def test_hi_with_empty_string():
    assert hi("") == "Hello, !"