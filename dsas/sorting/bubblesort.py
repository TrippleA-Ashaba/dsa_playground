def bubble_sort(items):
    for i in range(len(items)):
        # minus i and 1 to avoid unnecessary comparisons
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


if __name__ == "__main__":
    a = [3, 4, 6, 2, 9, 8, 10, 7, 1, 5]
    # a = ["a", "c", "f", "d", "i", "b", "g", "h", "e"]
    print(bubble_sort(a))
