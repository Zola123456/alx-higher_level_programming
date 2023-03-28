#!/usr/bin/python3

def safe_print_list(my_list=[], X=0):
    count = 0

    for i in range(X):
        try:

            print(my_list[i], end=" ")
            count += 1

        except IndexError:
            break

        print()
        return count
