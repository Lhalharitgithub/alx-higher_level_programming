#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [] 
    for i in range(len(my_list)):
    if my_list:
        for num in my_list:
            new_list.append(False if num % 2 else True)
        return new_list
