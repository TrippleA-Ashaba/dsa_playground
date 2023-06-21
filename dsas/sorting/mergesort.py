# [6, 9, 5, 4, 2, 7, 1, 0, 3, 8]


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


if __name__ == "__main__":
    # a = ["abaa", "c", "aaa", "b", "d", "j", "abba", "k"]
    a = [44, 16, 23, 83, 7, 67, 21, 34, 45, 10]

    print(merge_sort(a))
