# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge_sort(items: list):
    """
    Sorts a list of items using the merge sort algorithm.
    Parameters:
        * items (list): The list of items to be sorted.

    Returns:
        * (list): A sorted list of items.
    """
    # Base case:
    n = len(items)
    if n <= 1:
        return items

    mid = n // 2
    left_half = merge_sort(items[:mid])
    right_half = merge_sort(items[mid:])
    return merge(left_half, right_half)


def merge(left_half: list, right_half: list):
    """
    Merges two sorted lists into a single sorted list.
    Parameters:
        * left_half (list): The first sorted list.
        * right_half (list): The second sorted list.

    Returns:
        * merged_list (list): The merged and sorted list.
    """
    i = j = 0
    merged_list = []

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_list.append(left_half[i])
            i += 1
        else:
            merged_list.append(right_half[j])
            j += 1

    # Concatenate the result with what remains of the halves:
    merged_list += left_half[i:] + right_half[j:]
    return merged_list


# Examples:
if __name__ == "__main__":
    test_cases = [
        [34, 19, 11, 109, 3, 56],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [],
        [8],
        ["banana", "apple", "cherry", "date"]
    ]

    for i, test_case in enumerate(test_cases, start=1):
        sorted_list = merge_sort(test_case)
        print(f"Test Case {i}: {test_case} -> {sorted_list}")
