# test prompt smith client


from promtsmithsdk.prompt_smith import PromptSmith


def test_prompt_smith():
    """
    The basic test for prompt smith client
    :return:
    """
    prompt_smith = PromptSmith("http://localhost:8000", "a")
    # prompt smith get defined
    assert prompt_smith.get_prompt is not None
    # prompt smith get async defined
    assert prompt_smith.get_prompt_async is not None
