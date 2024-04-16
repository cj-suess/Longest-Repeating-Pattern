def find_possible_windows(list):
    "this finds all the valid windows to check"
    possible_windows = []
    for i in range(1, len(list)):
        if len(list) % i == 0:
            possible_windows.append(i)
    return possible_windows


def find_patterns(list, possible_windows):
    "this finds any repeating patterns using the valid windows"
    patterns_found = []
    for windows in possible_windows:
        pattern = list[0:windows]
        found = all(
            list[i:i + windows] == pattern for i in range(0, len(list), windows)
        )
        if found:
            patterns_found.append(pattern)
    return patterns_found


def repeat(list):
    # checks for invalid lists
    if list is None or len(list) < 2:
        return None

    # first find the windows to be checked
    possible_windows = find_possible_windows(list)
    # then find the patterns that those windows produce if any
    patterns_found = find_patterns(list, possible_windows)

    # if patterns_found is empty then no valid patterns exist
    if len(patterns_found) == 0:
        return None
    else:
        return max(patterns_found, key=len)
