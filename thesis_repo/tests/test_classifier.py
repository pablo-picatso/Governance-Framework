import pytest

from src.nlp.classifier import classify_category


def test_classify_category():
    assert classify_category("IT infrastructure") == "digital"
    assert classify_category("Personnel costs digital") == "personnel"
    assert classify_category("Outsourcing services") == "outsourcing"
    assert classify_category("Other administration") == "other"