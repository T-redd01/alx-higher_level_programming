#!/usr/bin/python3
def multiple_returns(sentence):
    """return length of sentence abd 1st char

        Args:
            sentence: sentence to check lenght and 1st char

        Return:
            tuple with length of sentence and 1st character
    """
    return (len(sentence), None if sentence == "" else sentence[0])
