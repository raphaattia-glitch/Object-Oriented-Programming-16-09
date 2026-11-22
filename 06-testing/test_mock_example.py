"""Exo testing / mocking (slide 93) : on remplace un appel API (LLM) par un faux objet."""
from unittest.mock import MagicMock

import pytest


class Assistant:
    """Petite classe qui depend d'un client LLM externe."""

    def __init__(self, client):
        self.client = client

    def answer(self, question):
        if not question.strip():
            raise ValueError("question vide")
        reply = self.client.complete(question)
        return reply.strip().upper()


def test_answer_uses_client_without_real_api_call():
    fake_client = MagicMock()
    fake_client.complete.return_value = "  bonjour  "
    assert Assistant(fake_client).answer("salut") == "BONJOUR"
    fake_client.complete.assert_called_once_with("salut")


def test_empty_question_never_calls_api():
    fake_client = MagicMock()
    with pytest.raises(ValueError):
        Assistant(fake_client).answer("   ")
    fake_client.complete.assert_not_called()


def test_api_failure_is_simulated():
    fake_client = MagicMock()
    fake_client.complete.side_effect = TimeoutError("API down")
    with pytest.raises(TimeoutError):
        Assistant(fake_client).answer("salut")
