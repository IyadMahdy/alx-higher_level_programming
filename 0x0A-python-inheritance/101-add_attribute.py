#!/usr/bin/python3
"""Advanced Task 1"""


def add_attribute(obj_name, attr_name, value):
    """adds a new attribute to an object if it’s possible"""
    if hasattr(obj_name, '__dict__'):
        setattr(obj_name, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
