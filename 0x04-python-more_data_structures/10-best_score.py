#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the highest score

        Args:
            a_dictionary: A dictionary

        Return:
            None if dictionary has no scores
            Highest score otherwise
    """
    if a_dictionary is None or a_dictionary == {}:
        return None
    max_score = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if max_score == value:
            return key
