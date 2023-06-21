# [5,6,4,8,9,2,3,1]


def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1

        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = key

    return items


if __name__ == "__main__":
    a = [5, 6, 4, 8, 9, 2, 3, 1]

    print(insertion_sort(a))
