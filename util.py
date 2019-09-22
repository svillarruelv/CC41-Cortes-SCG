def split(input_list):
    n = len(input_list)
    m = n // 2
    return input_list[:m], input_list[m:]


def merge_sorted_lists(list_left, list_right):

    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left
    

    index_left = index_right = 0
    list_merged = []
    list_len_target = len(list_left) + len(list_right)

    while len(list_merged) < list_len_target:
        if list_left[index_left].area <= list_right[index_right].area:
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            list_merged.append(list_right[index_right])
            index_right += 1


        if index_right == len(list_right):
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            list_merged += list_right[index_right:]
            break
        
    return list_merged


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)

        return merge_sorted_lists(merge_sort(left), merge_sort(right))