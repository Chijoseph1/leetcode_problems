def add_two_numbers(l1,l2):
    result_1 =[]
    result = 0
    new_list1= "".join(str(x) for x in l1)
    print(new_list1)
    new_list2 = "".join(str(x) for x in l2)
    result = int(new_list1) + int(new_list2)
    print(result)
    result1 = str(result)
    for n in reversed(result1):
        result_1.append(int(n))
    # result2 = result1.split(",")
    print(result_1)
l1 = [2,4,3]
l2 = [5,6,4]
print(add_two_numbers(l1,l2))

