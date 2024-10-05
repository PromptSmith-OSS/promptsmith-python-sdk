# test prompt smith client


from python_sdk.prompt_smith import PromptSmith


def test_prompt_smith():
    prompt_smith = PromptSmith("http://localhost:8000", "a")
    # prompt smith get defined
    assert prompt_smith.get_prompt is not None
