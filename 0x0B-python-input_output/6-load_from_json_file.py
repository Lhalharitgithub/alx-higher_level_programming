#!/usr/bin/python3
"""A function that definez a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """It createz a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
