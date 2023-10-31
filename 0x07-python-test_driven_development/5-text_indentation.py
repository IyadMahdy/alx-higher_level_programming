#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = "\n".join([y.strip() for y in text.splitlines()])
    new_text = ".".join([y.strip(" \t") for y in new_text.split(".")])
    new_text = ":".join([y.strip(" \t") for y in new_text.split(":")])
    new_text = "?".join([y.strip(" \t") for y in new_text.split("?")])
    new_text = new_text.replace(".", ".\n\n")
    new_text = new_text.replace(":", ":\n\n")
    new_text = new_text.replace("?", "?\n\n")
    print(new_text, end="")
