"""Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""


# def same_structure_as(original, other):
#     list_of_len = []
#     o = [type(i) for i in original]
#     t = [type(u) for u in other]
#     print(count_items(original))
#     print(count_items(other))
#     if o == t and count_items(original) == count_items(other):
#         return True
#
#     elif count_items(original) == count_items(other) and len(original)==len(other):
#         return True
#     else:
#         return False


def same_structure_as(original, other):
    o = []
    t = []
    index = None
    for e in range(len(original)):
        index = e

        for i in original:
            if isinstance(i, list):
                count_items(i)
            o.append(type(i))
        for u in other:
            if isinstance(u, list):
                count_items(u)
            t.append(type(u))
    if len(o) == len(t) and count_items(original[index]) == count_items(other[index]):
        return True
    elif o[index] == t[index] and count_items(original) == count_items(other):
        return True
    else:
        return False


def count_items(array):
    cnt = 0
    l = array
    if not isinstance(array, list):
        l = [array]
    for item in l:
        if isinstance(item, list):
            cnt += count_items(item)
        else:
            cnt += 1
    return cnt


print(same_structure_as([1, [1, 1]], [2, [2, 2]]))  # True
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))  # False
print(same_structure_as([1, [1, 1]], [2, [2]]))  # False
print(same_structure_as([[[], []]], [[1, 1]]))  # False
print(same_structure_as([1, '[', ']'], ['[', ']', 1]))  # True

# print(count_items([1, [1, 1]]))
# print(count_items([[2,2],2]))
# print(count_items(1))
# print(count_items([2,2]))

# print(count_items([1,1]))
# print(count_items([[2]]))




def structure_as(original, other):
    # Base case: if both elements are not lists, return True
    if not isinstance(original, list) and not isinstance(other, list):
        return True
    # If one is a list and the other is not, or their lengths differ, return False
    elif not isinstance(original, list) or not isinstance(other, list) or len(original) != len(other):
        return False
    else:
        # Recursively check the structure of sublists
        return all(structure_as(o1, o2) for o1, o2 in zip(original, other))
print()
print("new")

print(structure_as([1, [1, 1]], [2, [2, 2]]))  # True
print(structure_as([1, [1, 1]], [[2, 2], 2]))  # False
print(structure_as([1, [1, 1]], [2, [2]]))  # False
print(structure_as([[[], []]], [[1, 1]]))  # False
print(structure_as([1, '[', ']'], ['[', ']', 1]))  # True


def structure(original, other):
    # Check if both elements are lists
    if isinstance(original, list) and isinstance(other, list):
        # Check if their lengths are the same
        if len(original) != len(other):
            return False
        # Recursively check the structure of elements in the lists
        for i in range(len(original)):
            if not structure(original[i], other[i]):
                return False
        return True
    # If one is a list and the other is not, return False
    elif isinstance(original, list) or isinstance(other, list):
        return False
    # If neither is a list, return True (they have the same structure)
    else:
        return True


print()
print("new")

print(structure([1, [1, 1]], [2, [2, 2]]))  # True
# print(structure([1, [1, 1]], [[2, 2], 2]))  # False
# print(structure([1, [1, 1]], [2, [2]]))  # False
# print(structure([[[], []]], [[1, 1]]))  # False
# print(structure([1, '[', ']'], ['[', ']', 1]))  # True