#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        nums = 0
        for i in my_list:
            if x == 0:
                break
            print(f"{i}", end="")
            x -= 1
            nums += 1
        print()
        return nums
    except IndexError:
        return nums
