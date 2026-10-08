def median_two_sorted_array(l1,l2):
    added_value = l1 + l2
    print(added_value)
    sort1 = sorted(added_value)
    if len(sort1) % 2 != 0:
        
    middle = len(added_value) // 2
    print(middle)
    return sort1[middle]

l1 = [1,3]
l2 = [2,4]
print(median_two_sorted_array(l1,l2))
