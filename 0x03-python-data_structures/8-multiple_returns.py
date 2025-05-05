#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns length and first character of tuple

        Args:
            sentence: Tuple with characters

        Return:
            Length of tuple
            First character of tuple
    """
    length = len(sentence)
    if sentence == "":
        sentence = (None,)

    return length, sentence[0]
