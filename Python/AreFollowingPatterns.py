# https://codefights.com/interview-practice/task/3PcnSKuRkqzp8F6BN
from collections import defaultdict


def areFollowingPatterns(strings, patterns):
    dict_strings = defaultdict(list)
    if len(strings) != len(patterns):
        return False

    i = 0
    for s in strings:
        dict_strings[s].append(patterns[i])
        i = i + 1
        pattern = dict_strings[s]
        # Make sure you're only adding the same element from patterns for the same key
        if len(set(pattern)) > 1:
            return False

    list_pattern = []
    # Now we know the values for dict_strings is only a list of the same elements
    for key, val in dict_strings.items():
        set_values = set(val)
        # Each key in dict should be associated with only 1 pattern element
        if set_values in list_pattern:
            return False
        else:
            list_pattern.append(set_values)

    return True

areFollowingPatterns(["cat", "dog", "dog"], ["a", "b", "b"])
areFollowingPatterns(["cat", "dog", "dogg"], ["a", "b", "b"])