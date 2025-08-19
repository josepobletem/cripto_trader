from unittest.mock import patch

from trading.gpt_helper import GPTExplainer


@patch("openai.ChatCompletion.create")
def test_explain(mock_create):
    mock_create.return_value.choices = [
        type(
            "obj",
            (object,),
            {
                "message": type(
                    "obj", (object,), {"content": "Compra porque el precio es bajo."}
                )
            },
        )()
    ]
    explainer = GPTExplainer()
    explanation = explainer.explain("buy", 29000)
    assert "Compra" in explanation
