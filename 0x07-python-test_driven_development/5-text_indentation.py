#!/usr/bin/python3

def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    elif text is None:
        raise TypeError("text must be a string")
    else:
        text = text.replace(".", ".\n").replace("?", "?\n").replace(":", ":\n")
        lines = text.splitlines() # returns array of each line
        for index, line in enumerate(lines): #line = each line in the array
            line = line.strip()  # remove leading and trailing white spaces
            print(line, end="\n\n" if index != len(lines) - 1 else'')
