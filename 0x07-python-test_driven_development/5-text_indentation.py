#!/usr/bin/python3
"""function that prints lines of text without
spaces in the beginning and end and
print 2 new lines in specified delims
"""


def text_indentation(text):
    """print text in neat way

    Args:
        text (str): text to format and print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for i in range(len(text)):
        if text[i] in ":?.":
            line += text[i]
            i += 1
            print(f"{line.strip()}\n\n", end='')
            line = ""
        else:
            line += text[i]

    print(line.strip(), end='')
