#!/usr/bin/python3
"""Advanced Task 1"""


def add_attribute(obj_name, attr_name, value):
    if hasattr(obj_name, attr_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj_name, attr_name, value)
