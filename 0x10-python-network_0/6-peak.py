#!/usr/bin/python3
""" Module that return the peak in a list """


def find_peak(list_of_integers):
    """ Method that finds a peak in a list of unsorted integers """
    if list_of_integers is None or list_of_integers == []:
        return None
    lower_value = 0
    length_of_list = len(list_of_integers)
    mid = ((length_of_list - lower_value) // 2) + lower_value
    mid = int(mid)
    if length_of_list == 1:
        return list_of_integers[0]
    if length_of_list == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
         return find_peak(list_of_integers[:mid])
