#!/usr/bin/python3
def multiple_returns(sentence):
    """
        If the sentence is empty, the first character should be equal to None
        You are not allowed to import any module
    """
    s_len = 0
    f_char = None
    if isinstance(sentence, str):
        s_len = len(sentence)
        if s_len > 0:
            f_char = sentence[0]
    return (s_len, f_char)
