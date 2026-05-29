#!/usr/bin/env python3

my_list = [1, 2, 3, 4, 5, 6]


def add_item_to_list(list_name):
    list_name.append(7)
    list_name.append(8)
    return list_name


def remove_items_from_list(list_name, items):
    for item in items:
        if item in list_name:
            list_name.remove(item)
    return list_name
