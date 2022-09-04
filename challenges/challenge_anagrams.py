def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    list1 = list(first_string.lower())
    list2 = list(second_string.lower())

    for i in list1:
        if i in list2:
            list2.remove(i)
        else:
            return False

    return True
