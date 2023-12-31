def merge_sort(list):
    # Sorts a list in ascending order
    # Returns a new sorted list
    # Divide: Find midpoint of the lsit and divide into sublists
    # Conquer: Recursviley sort the sublists created in previous step
    # Combine: Merge the sorted sublists created in previous step
    # takes O(n log n)time

    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    # diviide unsorted list at midpoint into sublist, returns two sublists - left and right
    # takes overall of O(log n)
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    # merges two lists, sorting them in the process returns a new merged list
    # runs in overall linear time O(n)

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 26, 94, 15, 77, 31, 44, 55, 20]

l = merge_sort(alist)

print(verify_sorted(alist))
print(verify_sorted(l))
