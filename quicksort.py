# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy.random import randint


def quicksort(items: list) -> None:
    """
    Sort a list in-place in ascending order using the quicksort algorithm.
    Assumes that the elements of the list can be compared using `<` and `>`

    Parameters:
        * items (list): The list of integers to sort.

    Returns:
        * None: This function sorts the list in-place and returns None.
    """

    def swap(i: int, j: int) -> None:
        """
        Swap two elements in the list `items`.

        Parameters:
            * i, j (int): The indices of the elements to be swapped.
        """
        items[i], items[j] = items[j], items[i]

    def choose_pivot(first: int, last: int) -> int:
        """
        Select a pivot index randomly within the specified range of the
        sublist. Another reasonable (and deterministic) choice would be to take
        the median of the values stored at `first`, `last` and their midpoint.

        Parameters:
            * first (int): The starting index of the subarray.
            * last (int): The ending index of the subarray.

        Returns:
            * (int): The randomly selected index of the pivot element.
        """

        return randint(first, last + 1)

    def partition(pivot: int, start: int, end: int) -> int:
        """
        Partition the list in-place around a pivot element.

        Parameters:
            * pivot (int): The index of the pivot element.
            * start (int): The start index of the sublist to partition.
            * end (int): The end index of the sublist to partition.

        Returns:
            * (int): The final position of the pivot element.
        """
        pivot_value = items[pivot]
        swap(start, pivot)
        i = start + 1
        for j in range(start + 1, end + 1):
            if items[j] < pivot_value:
                if i < j:  # Avoid unnecessary swaps
                    swap(i, j)
                i += 1
        swap(start, i - 1)
        return i - 1

    def quicksort_with_indices(start: int, end: int) -> None:
        """
        Recursively sorts in-place the sublist of `items` defined by the given
        initial and final indices.

        Parameters:
            * start (int): The start index of the sublist to sort.
            * end (int): The end index of the sublist to sort.
        """
        if start >= end:
            return
        else:
            pivot = choose_pivot(start, end)
            mid = partition(pivot, start, end)
            quicksort_with_indices(start, mid - 1)
            quicksort_with_indices(mid + 1, end)

    start = 0
    end = len(items) - 1
    quicksort_with_indices(start, end)


def main():
    test_cases = [
        [],
        [1],
        [1, 2],
        [2, 1],
        [1, 2, 3, 4, 5],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 1, 1, 1],
        [randint(-20, 20) for _ in range(100)],
        [1.5, -3.2, 7, 4.4, 2],
        ["banana", "apple", "cherry", "date"],
        ["zephyr", "zenith", "zodiac", "zombie", "zircon", "zealot",
         "zulu", "zigzag"]
    ]

    for items in test_cases:
        original = items.copy()  # Copy to print before sorting
        quicksort(items)
        print(f"Original: {original}\nSorted  : {items}\n")


if __name__ == "__main__":
    main()
