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


def main():
    """ Examples """
    from numpy.random import randint


    test_cases = [
        [],
        [1],
        [1, 2],
        [2, 1],
        [1, 2, 3, 4, 5],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 1, 1, 1],
        [randint(-10, 10) for _ in range(100)],
        [1.5, -3.2, 7, 4.4, 2],
        ["banana", "apple", "cherry", "date"],
        ["zephyr", "zenith", "zodiac", "zombie", "zircon", "zealot",
         "zulu", "zigzag"]
    ]

    for items in test_cases:
        original = items.copy()  # Copy to print before sorting
        merge_sort(items)
        print(f"Original: {original}\nSorted  : {items}\n")


if __name__ == "__main__":
    main()
