from linked_list import LinkedList


def merge_sort(linked_list):
    # sorts a linked list in ascending order
    # recursivley divide the linked list into sublists containing a single node
    # repeatedly merge the sublists to produce sorted sublists unitl one remains
    # returns a sorted list

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
