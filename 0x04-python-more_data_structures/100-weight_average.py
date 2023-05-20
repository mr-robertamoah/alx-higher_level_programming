#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or not len(my_list):
        return 0
    num = s_num = s_denum = 0
    denum = 1
    for i in my_list:
        if isinstance(i, tuple):
            if len(i) > 0:
                num = i[0]
            if len(i) > 1:
                denum = i[1]
        s_num += num * denum
        s_denum += denum
        num = 0
        denum = 1
    return s_num / s_denum
