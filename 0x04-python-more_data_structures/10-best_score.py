#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_pair = max(a_dictionary.items(), key=lambda item: item[1])
    return max_pair[0]
